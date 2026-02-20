"""
train_model.py

Trains a small RandomForest classifier on `dataset.json`.
Saves `model.joblib` and `vocab.json`.

This script is deliberately simple and creates binary bag-of-symptom features.
Extend with real labeled data for production use.
"""
import json
from pathlib import Path
from collections import Counter

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump

BASE = Path(__file__).parent
DATASET = BASE / "dataset.json"
MODEL_PATH = BASE / "model.joblib"
VOCAB_PATH = BASE / "vocab.json"

if not DATASET.exists():
    # create a slightly expanded synthetic dataset if none exists
    sample = [
        {"symptoms": ["fever","headache","fatigue"], "disease": "Viral Fever"},
        {"symptoms": ["fever","abdominal pain","constipation","headache"], "disease": "Typhoid"},
        {"symptoms": ["fever","joint_pain","headache"], "disease": "Dengue"},
        {"symptoms": ["fever","sweating","shivering","muscle pain"], "disease": "Malaria"},
        {"symptoms": ["thirst","urination","fatigue"], "disease": "Diabetes"},
        {"symptoms": ["fatigue","swelling_legs","reduced_urine"], "disease": "Kidney"},
        {"symptoms": ["chest pain","palpitations","fatigue"], "disease": "Heart"},
    ]
    DATASET.write_text(json.dumps(sample, indent=2), encoding="utf-8")

data = json.loads(DATASET.read_text(encoding="utf-8"))

# Build vocabulary of symptoms
all_symptoms = Counter()
for row in data:
    for s in row.get('symptoms', []):
        all_symptoms[s] += 1

vocab = sorted(all_symptoms.keys())
print(f"Vocabulary ({len(vocab)}):", vocab)

# Vectorize
X = []
y = []
for row in data:
    sset = set(row.get('symptoms', []))
    vec = [1 if s in sset else 0 for s in vocab]
    X.append(vec)
    y.append(row.get('disease'))

X = np.array(X)
y = np.array(y)

# If dataset is tiny, duplicate some entries with small noise to allow training
if len(X) < 30:
    # simple augmentation: duplicate rows with same label
    reps = 10
    X = np.tile(X, (reps,1))
    y = np.tile(y, reps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print('\nClassification report on synthetic test set:')
print(classification_report(y_test, y_pred))

# Save model and vocab
dump(clf, MODEL_PATH)
VOCAB_PATH.write_text(json.dumps(vocab, indent=2), encoding='utf-8')
print(f"Saved model to {MODEL_PATH} and vocab to {VOCAB_PATH}")
