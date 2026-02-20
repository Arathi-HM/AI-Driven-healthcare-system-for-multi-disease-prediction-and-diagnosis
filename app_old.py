# app.py
from flask import Flask, send_from_directory, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from email.message import EmailMessage
import smtplib, ssl, random, os, json, threading, socket, traceback
from PyPDF2 import PdfReader


app = Flask(__name__, static_url_path='', static_folder='.')

# ===================== SMTP SETTINGS (EDIT) =====================
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))   # primary (TLS)
SMTP_EMAIL = os.environ.get("SMTP_EMAIL", "d900327@gmail.com")   # sender/login
SMTP_APP_PASSWORD = os.environ.get("SMTP_APP_PASSWORD", "qggh nmrn dbyb uqod")
SENDER_NAME = os.environ.get("SENDER_NAME", "MedPredict")
SMTP_DEBUG = int(os.environ.get("SMTP_DEBUG", "0"))   # set 1 to print SMTP debug logs to console
# ================================================================

USERS_FILE   = "users.json"
RESULTS_FILE = "results.json"

OTP_STORE = {}  # email -> {"otp": "123456", "expires": dt, "last_sent": dt, "verified": False}
OTP_EXP_MINUTES = 10
OTP_RATE_LIMIT_SECONDS = 60

lock = threading.Lock()

# ---------------- JSON tiny DB ----------------
def _read_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def _write_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

def get_users(): return _read_json(USERS_FILE, {})
def save_users(x): _write_json(USERS_FILE, x)
def get_results_store(): return _read_json(RESULTS_FILE, {})
def save_results_store(x): _write_json(RESULTS_FILE, x)

# Simple dataset-based prediction support (k-NN over JSON dataset)
def _load_dataset(path="dataset.json"):
    return _read_json(path, [])

# ML model artifacts (populated by `train_model.py`)
MODEL_FILE = os.path.join(os.path.dirname(__file__), 'model.joblib')
VOCAB_FILE  = os.path.join(os.path.dirname(__file__), 'vocab.json')

_MODEL = None
_VOCAB = None
try:
    if os.path.exists(MODEL_FILE) and os.path.exists(VOCAB_FILE):
        from joblib import load as joblib_load
        _MODEL = joblib_load(MODEL_FILE)
        with open(VOCAB_FILE, 'r', encoding='utf-8') as _f:
            _VOCAB = json.load(_f)
        print(f"Loaded ML model from {MODEL_FILE} with {len(_VOCAB)} features")
    else:
        print("No ML model found (model.joblib). Using dataset k-NN fallback.")
except Exception as e:
    print("Failed to load ML model:", e)
    _MODEL = None
    _VOCAB = None

    # Minimal disease recommendations mapping used by `age_adjusted_recommendations`.
    # Populate with domain-specific guidance as needed. Kept empty to avoid runtime errors.
    DISEASE_RECOMMENDATIONS = {}

def age_adjusted_recommendations(disease, age, symptoms):
    """Return recommendations for a disease adjusted by age and specific symptoms.
    Keeps base recommendations from DISEASE_RECOMMENDATIONS and adds age- or symptom-specific advice.
    """
    recs = []
    base = DISEASE_RECOMMENDATIONS.get(disease, [])
    recs.extend(base)

    try:
        age_num = int(age) if age is not None and str(age).isdigit() else None
    except Exception:
        age_num = None

    # Age-based additions
    if age_num is not None:
        if age_num >= 65:
            recs.insert(0, "Elderly patient: seek medical attention early; consider urgent evaluation for severe symptoms.")
        elif age_num <= 12:
            recs.insert(0, "For children: monitor hydration closely and consult pediatric care if symptoms worsen.")
        elif 13 <= age_num <= 18:
            recs.insert(0, "For adolescents: ensure rest and see GP if persistent high fever.")

    # Symptom-specific advice
    sset = set(symptoms or [])
    if 'fever' in sset:
        recs.append('Monitor temperature regularly; seek care if fever > 38.5°C or persists >48 hours.')
    if 'chest pain' in sset or 'palpitations' in sset:
        recs.insert(0, 'If chest pain is severe/radiating or associated with breathlessness, seek emergency care immediately.')
    if 'thirst' in sset or 'urination' in sset:
        recs.append('Check blood sugar and hydrate; seek diabetes testing if symptoms persist.')

    # Deduplicate while preserving order
    seen = set(); out = []
    for r in recs:
        if r and r not in seen:
            out.append(r); seen.add(r)
    return out


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """Predict disease using the dataset k-NN (Jaccard-weighted) approach.
    This implementation always uses `dataset.json` for prediction and normalizes
    symptom tokens to improve matching (lowercase, strip, spaces -> underscores).
    Returns disease, confidence, risk and age-adjusted recommendations.
    """
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify(success=False, message="Invalid JSON payload.")

    symptoms = data.get('symptoms') or []
    if not isinstance(symptoms, list):
        return jsonify(success=False, message="`symptoms` must be a list of symptom keys.")

    # Normalize symptom tokens to match dataset formatting
    def _normalize(s):
        try:
            return str(s).lower().strip().replace(' ', '_')
        except Exception:
            return str(s).lower().strip()

    norm_symptoms = [_normalize(s) for s in symptoms if s and str(s).strip()]
    if not norm_symptoms:
        return jsonify(success=False, message="No symptoms provided.")

    ds = _load_dataset()
    if not ds:
        return jsonify(success=False, message="No dataset available on server (dataset.json missing).")

    # compute Jaccard similarity between two symptom lists
    def jaccard(a, b):
        sa = set(a or [])
        sb = set(b or [])
        if not sa and not sb:
            return 0.0
        inter = sa.intersection(sb)
        union = sa.union(sb)
        return float(len(inter)) / float(len(union)) if union else 0.0

    # prepare dataset records with normalized symptom tokens
    records = []
    for r in ds:
        rs = r.get('symptoms') or []
        rn = [_normalize(x) for x in rs if x and str(x).strip()]
        records.append({'disease': r.get('disease') or 'Unknown', 'symptoms': rn, 'raw': r})

    # compute similarity for each record
    sims = []
    for rec in records:
        sim = jaccard(norm_symptoms, rec['symptoms'])
        sims.append((rec, sim))

    # select top-k neighbors by similarity
    k = min(5, max(1, len(sims)))
    sims_sorted = sorted(sims, key=lambda x: x[1], reverse=True)
    neighbors = sims_sorted[:k]

    # If no similarity at all, still try to pick best match by shared symptom count
    if all(sim <= 0.0 for (_r, sim) in neighbors):
        # fallback: pick record(s) with largest intersection size
        def inter_size(a, b):
            return len(set(a).intersection(set(b)))
        scored = [(rec, inter_size(norm_symptoms, rec['symptoms'])) for rec in records]
        scored_sorted = sorted(scored, key=lambda x: x[1], reverse=True)
        neighbors = [(r, 0.0 if s == 0 else float(s)) for (r, s) in scored_sorted[:k]]

    # weighted voting by similarity (use small epsilon so zero-sim neighbors still contribute minimally)
    votes = {}
    weights = {}
    for rec, sim in neighbors:
        w = sim if isinstance(sim, float) else float(sim)
        # small epsilon to prefer records with any overlap
        if w == 0.0:
            w += 0.001
        lab = rec.get('disease') or 'Unknown'
        votes[lab] = votes.get(lab, 0.0) + w
        weights[lab] = weights.get(lab, 0.0) + w

    if not votes:
        return jsonify(success=False, message="Unable to predict from dataset.")

    # pick disease with highest total weight
    pred = max(votes.items(), key=lambda x: x[1])[0]
    total = sum(votes.values()) or 1.0
    confidence = int(round(100.0 * (votes.get(pred, 0.0) / total)))
    if confidence >= 70:
        risk = 'High'
    elif confidence >= 40:
        risk = 'Moderate'
    else:
        risk = 'Low'

    age = (data.get('patient') or {}).get('age')
    recs = age_adjusted_recommendations(pred, age, norm_symptoms)

    # build neighbor info to return (disease, similarity, symptoms)
    neighbors_out = []
    for rec, sim in neighbors:
        neighbors_out.append({'disease': rec.get('disease'), 'similarity': float(sim), 'symptoms': rec.get('symptoms')})

    return jsonify(success=True, disease=pred, confidence=confidence, risk=risk, recommendations=recs, neighbors=neighbors_out)


# ---------------- SMTP helpers (replaced after accidental edit)
def _build_message(to_email: str, subject: str, body: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body, charset="utf-8")
    return msg

def _send_tls(host, port, user, pwd, to_email, msg: EmailMessage):
    context = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=25) as server:
        if SMTP_DEBUG: server.set_debuglevel(1)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(user, pwd)
        server.send_message(msg)

def _send_ssl(host, port, user, pwd, to_email, msg: EmailMessage):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context, timeout=25) as server:
        if SMTP_DEBUG: server.set_debuglevel(1)
        server.login(user, pwd)
        server.send_message(msg)

def send_mail(to_email: str, subject: str, body: str):
    msg = _build_message(to_email, subject, body)
    tls_err = None
    try:
        _send_tls(SMTP_HOST, SMTP_PORT, SMTP_EMAIL, SMTP_APP_PASSWORD, to_email, msg)
        return
    except Exception as e:
        tls_err = e
    try:
        _send_ssl(SMTP_HOST, 465, SMTP_EMAIL, SMTP_APP_PASSWORD, to_email, msg)
        return
    except Exception as ssl_err:
        raise RuntimeError(
            f"TLS({SMTP_HOST}:{SMTP_PORT}) failed: {type(tls_err).__name__}: {tls_err} | "
            f"SSL({SMTP_HOST}:465) failed: {type(ssl_err).__name__}: {ssl_err}"
        ) from ssl_err

def send_otp_email(to_email: str, otp: str):
    body = (
        f"Hello,\n\n"
        f"Your One-Time Password (OTP) is: {otp}\n\n"
        f"It expires in {OTP_EXP_MINUTES} minutes.\n"
        f"If you did not request this, please ignore this email.\n\n"
        f"Thanks,\n{SENDER_NAME}\n"
    )
    send_mail(to_email, "Your OTP Code", body)

# ---------------- UI ----------------
@app.route("/")
def root():
    return send_from_directory(".", "index.html")

# ---------------- Auth ----------------
@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()
    username = (data.get("username") or "").strip()
    phone = (data.get("phone") or "").strip()
    address = (data.get("address") or "").strip()
    if not email or not password:
        return jsonify(success=False, message="Email and password are required.")

    with lock:
        users = get_users()
        if email in users:
            return jsonify(success=False, message="Email already exists.")
        users[email] = {
            "email": email,
            "password_hash": generate_password_hash(password),
            "username": username,
            "phone": phone,
            "address": address,
            "created_at": datetime.utcnow().isoformat()
        }
        save_users(users)
    return jsonify(success=True, message="Account created successfully.")

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()
    with lock:
        users = get_users()
        user = users.get(email)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify(success=False, message="Invalid credentials.")
    profile = {
        "email": email,
        "username": user.get("username") or "",
        "phone": user.get("phone") or "",
        "address": user.get("address") or ""
    }
    return jsonify(success=True, user=profile)

# ---------------- OTP / Reset ----------------
@app.route("/api/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    if not email:
        return jsonify(success=False, message="Email required.")

    with lock:
        now = datetime.utcnow()
        info = OTP_STORE.get(email)
        if info and info.get("last_sent") and (now - info["last_sent"]).total_seconds() < OTP_RATE_LIMIT_SECONDS:
            return jsonify(success=False, message="Please wait before requesting another OTP.")
        otp = f"{random.randint(0, 999999):06d}"
        OTP_STORE[email] = {
            "otp": otp,
            "expires": now + timedelta(minutes=OTP_EXP_MINUTES),
            "last_sent": now,
            "verified": False
        }

    try:
        send_otp_email(email, otp)
        return jsonify(success=True, message="OTP sent to your email.")
    except smtplib.SMTPAuthenticationError as e:
        return jsonify(success=False, message="SMTP authentication failed. Check SMTP_EMAIL and SMTP_APP_PASSWORD.", detail=str(e))
    except smtplib.SMTPConnectError as e:
        return jsonify(success=False, message=f"SMTP connect error to {SMTP_HOST}.", detail=str(e))
    except smtplib.SMTPServerDisconnected as e:
        return jsonify(success=False, message="SMTP server disconnected unexpectedly.", detail=str(e))
    except smtplib.SMTPRecipientsRefused as e:
        return jsonify(success=False, message="Recipient refused by SMTP server.", detail=str(e.recipients))
    except (socket.timeout, TimeoutError) as e:
        return jsonify(success=False, message=f"SMTP timeout when contacting {SMTP_HOST}.", detail=str(e))
    except Exception as e:
        # include both types and traceback tail for quick debugging
        tb = traceback.format_exc(limit=2)
        return jsonify(success=False, message=f"Send failed: {type(e).__name__}", detail=f"{e}", trace=tb)

@app.route("/api/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    otp = (data.get("otp") or "").strip()
    if not email or not otp:
        return jsonify(success=False, message="Email and OTP required.")

    with lock:
        info = OTP_STORE.get(email)
        if not info:
            return jsonify(success=False, message="No OTP issued for this email.")
        if datetime.utcnow() > info["expires"]:
            return jsonify(success=False, message="OTP expired. Request a new one.")
        if otp != info["otp"]:
            return jsonify(success=False, message="Invalid OTP.")
        info["verified"] = True
        OTP_STORE[email] = info

    return jsonify(success=True, message="OTP verified.")

@app.route("/api/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    new_password = (data.get("new_password") or "").strip()
    if not email or not new_password:
        return jsonify(success=False, message="Email and new password required.")

    with lock:
        info = OTP_STORE.get(email)
        if not info or not info.get("verified"):
            return jsonify(success=False, message="OTP not verified.")
        users = get_users()
        if email not in users:
            return jsonify(success=False, message="No account for this email.")
        users[email]["password_hash"] = generate_password_hash(new_password)
        save_users(users)
        OTP_STORE.pop(email, None)

    return jsonify(success=True, message="Password reset successfully.")


# ---------------- Report Parsing (PDF) ----------------
import re as _re

def _extract_number(labels, text):
    """
    Find the first numeric value appearing near any of the given labels.
    Returns the matched numeric string or "" if not found.
    Improved: handles various spacing and line breaks.
    """
    if not text:
        return ""
    for label in labels:
        # Try multiple pattern variations to handle different PDF layouts
        patterns = [
            rf"{label}\s*[:\-]?\s*([0-9]+(?:\.[0-9]+)?)",  # label: number
            rf"{label}[^0-9\-\.]{0,40}([0-9]+(?:\.[0-9]+)?)",  # label followed by up to 40 chars then number
            rf"{label}[^\n]*?([0-9]+(?:\.[0-9]+)?)",  # label, then any chars until number on same/next line
        ]
        for pattern in patterns:
            m = _re.search(pattern, text, flags=_re.IGNORECASE | _re.DOTALL)
            if m:
                return m.group(1)
    return ""

def parse_lab_text(test_key, text):
    """
    Improved heuristic parser that looks for common words in the PDF text
    and extracts lab values. Handles various PDF formatting and spacing issues.
    """
    if not isinstance(text, str):
        text = text.decode("utf-8", errors="ignore") if hasattr(text, "decode") else str(text)
    lower = text.lower()
    data = {}

    if test_key == "cbc":
        # Complete Blood Count
        data["platelets"]  = _extract_number(["platelet", "plt", "thrombocyte"], lower)
        data["wbc"]        = _extract_number(["wbc", "white blood cell", "white blood", "leukocyte"], lower)
        data["hemoglobin"] = _extract_number(["hemoglobin", "hb", "hgb"], lower)

    elif test_key == "blood_sugar":
        # Blood Glucose Test
        data["fasting"] = _extract_number(["fasting blood", "fbs", "fasting glucose", "fasting plasma"], lower)
        data["pp"]      = _extract_number(["pp", "post prandial", "postprandial", "post-prandial", "2 hours"], lower)

    elif test_key == "kidney_function":
        # Kidney Function Test
        data["creatinine"] = _extract_number(["creatinine", "serum creatinine"], lower)
        data["egfr"]       = _extract_number(["egfr", "gfr", "estimated gfr"], lower)

    elif test_key == "dengue_ns1":
        # Dengue NS1 Antigen - look for positive/negative across multiple patterns
        patterns_pos = [
            r"ns1[^\n]{0,50}(positive|reactive|detected)",
            r"dengue[^\n]{0,50}(positive|reactive|detected)",
            r"antigen[^\n]{0,50}(positive|reactive|detected)",
        ]
        patterns_neg = [
            r"ns1[^\n]{0,50}(negative|non.?reactive|not detected)",
            r"dengue[^\n]{0,50}(negative|non.?reactive|not detected)",
            r"antigen[^\n]{0,50}(negative|non.?reactive|not detected)",
        ]
        
        is_positive = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_pos)
        is_negative = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_neg)
        
        if is_positive:
            data["ns1"] = "positive"
        elif is_negative:
            data["ns1"] = "negative"
        else:
            data["ns1"] = ""

    elif test_key == "malaria_test":
        # Malaria Test - look for multiple patterns
        patterns_pos = [
            r"(malaria|plasmodium)[^\n]{0,50}(positive|detected|present)",
            r"blood\s*smear[^\n]{0,50}(positive|detected)",
        ]
        patterns_neg = [
            r"(malaria|plasmodium)[^\n]{0,50}(negative|not detected|absent)",
            r"blood\s*smear[^\n]{0,50}(negative|not detected)",
        ]
        
        is_positive = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_pos)
        is_negative = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_neg)
        
        if is_positive:
            data["parasite"] = "positive"
        elif is_negative:
            data["parasite"] = "negative"
        else:
            data["parasite"] = ""

    elif test_key == "widal":
        # Widal Test - look for titers like 1:80, 1:160, 1:320
        patterns = [
            r"1\s*:\s*(40|80|160|320)",
            r"(40|80|160|320)(?=\s*$|\s*\n|\s*;)",  # titer alone on a line
        ]
        for pattern in patterns:
            m = _re.search(pattern, lower)
            if m:
                data["titer"] = m.group(0).replace(" ", "")
                break
        if "titer" not in data:
            data["titer"] = ""

    elif test_key == "ecg":
        # ECG interpretation
        patterns_abnormal = [
            r"ecg[^\n]{0,50}(abnormal|ischemia|infarct|st.?t\s*changes|arrhythmia)",
            r"(abnormal|ischemia|infarct|arrhythmia).*ecg",
        ]
        patterns_normal = [
            r"ecg[^\n]{0,50}(normal|no acute)",
            r"normal.*ecg",
        ]
        
        is_abnormal = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_abnormal)
        is_normal = any(_re.search(p, lower, _re.IGNORECASE) for p in patterns_normal)
        
        if is_abnormal:
            data["abnormal"] = "abnormal"
        elif is_normal:
            data["abnormal"] = "normal"
        else:
            data["abnormal"] = ""

    return data


# ---------------- Report Analysis API ----------------
@app.route("/api/analyze-reports", methods=["POST"])
def analyze_reports():
    """
    Accepts uploaded PDF files for the recommended tests, extracts basic values
    using PyPDF2, and returns a JSON object mapping each test key to a simple
    dict of fields (platelets, wbc, etc.). The frontend then calculates scores.
    """
    tests_raw = (request.form.get("tests") or "").strip()
    if not tests_raw:
        return jsonify(success=False, message="No tests provided.")

    try:
        if tests_raw.startswith("["):
            tests = json.loads(tests_raw)
        else:
            tests = [t.strip() for t in tests_raw.split(",") if t.strip()]
    except Exception:
        tests = [t.strip() for t in tests_raw.split(",") if t.strip()]

    result_data = {}
    for key in tests:
        file_key = f"file_{key}"
        f = request.files.get(file_key)
        if not f:
            continue
        try:
            reader = PdfReader(f)
            text_chunks = []
            for page in reader.pages:
                try:
                    page_text = page.extract_text() or ""
                except Exception:
                    page_text = ""
                text_chunks.append(page_text)
            full_text = "\n".join(text_chunks)
            parsed = parse_lab_text(key, full_text)

            # If all extracted fields are empty → check whether PDF had readable text.
            # If the PDF is essentially empty, mark as wrong report. If it had text
            # but parser couldn't find expected patterns, return a warning instead
            # (frontend will not treat this as a "wrong report" upload).
            if parsed and all(v == "" for v in parsed.values()):
                if not full_text or len(full_text.strip()) < 80:
                    result_data[key] = {"_error": "missing_required_fields"}
                else:
                    # text present but no fields matched — return parsed plus a warning
                    result_data[key] = {"_warning": "no_fields_extracted", "_text_length": len(full_text)}
            else:
                result_data[key] = parsed


        except Exception as e:
            result_data[key] = {"_error": f"Failed to read PDF: {type(e).__name__}: {e}"}

    return jsonify(success=True, data=result_data)
# ---------------- Results ----------------
@app.route("/api/save-result", methods=["POST"])
def save_result():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    if not email:
        return jsonify(success=False, message="Email is required.")

    record = {
        "timestamp": data.get("timestamp"),
        "client_key": data.get("client_key") or "",
        "patient_name": data.get("patient_name") or "",
        "patient_age": data.get("patient_age") or "",
        "patient_gender": data.get("patient_gender") or "",
        "disease": data.get("disease") or "",
        "risk": data.get("risk") or "",
        "recommendations": data.get("recommendations") or [],
        "report_scores": data.get("report_scores") or {}
    }
    with lock:
        store = get_results_store()
        store.setdefault(email, []).append(record)
        save_results_store(store)
    return jsonify(success=True, message="Saved.")

@app.route("/api/get-results", methods=["POST"])
def get_results():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    if not email:
        return jsonify(success=False, message="Email is required.")
    with lock:
        store = get_results_store()
        rows = store.get(email, [])
    rows_sorted = sorted(rows, key=lambda r: r.get("timestamp") or "", reverse=True)
    return jsonify(success=True, results=rows_sorted)

# --------- SMTP diagnostics (optional but handy) ----------
@app.route("/api/smtp-check", methods=["GET"])
def smtp_check():
    """
    Just connects and logs in. Use this to isolate credential / port issues.
    """
    try:
        # TLS first
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as s:
            if SMTP_DEBUG: s.set_debuglevel(1)
            s.ehlo(); s.starttls(context=context); s.ehlo()
            s.login(SMTP_EMAIL, SMTP_APP_PASSWORD)
        return jsonify(ok=True, mode="TLS", host=SMTP_HOST, port=SMTP_PORT)
    except Exception as e1:
        try:
            with smtplib.SMTP_SSL(SMTP_HOST, 465, timeout=20) as s2:
                if SMTP_DEBUG: s2.set_debuglevel(1)
                s2.login(SMTP_EMAIL, SMTP_APP_PASSWORD)
            return jsonify(ok=True, mode="SSL", host=SMTP_HOST, port=465, tls_error=str(e1))
        except Exception as e2:
            return jsonify(ok=False, error=f"TLS failed: {type(e1).__name__}: {e1} | SSL failed: {type(e2).__name__}: {e2}")

@app.route("/api/smtp-test-send", methods=["POST"])
def smtp_test_send():
    """
    Sends a simple test mail to yourself (SMTP_EMAIL) to verify end-to-end.
    """
    try:
        send_mail(
            SMTP_EMAIL,
            "SMTP Test — MedPredict",
            "This is a test email sent by /api/smtp-test-send to verify SMTP settings."
        )
        return jsonify(ok=True, message=f"Test email sent to {SMTP_EMAIL}")
    except Exception as e:
        return jsonify(ok=False, message=f"Send failed: {type(e).__name__}: {e}")

# ---------------- Run ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    # If testing from same machine/browser, 127.0.0.1 is fine
    app.run(host="127.0.0.1", port=port, debug=True)

