"""
Generate a detailed PDF report including:
- Algorithm application details
- SLOC summary (from sloc_report.json)
- COCOMO basic estimation (semi-detached)
- Team division for 4 members and cost breakdown
"""
import json
import math
import os
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

root = os.path.dirname(__file__)
sloc_path = os.path.join(root, 'sloc_report.json')
if not os.path.exists(sloc_path):
    raise SystemExit('sloc_report.json not found. Run compute_sloc.py first.')

with open(sloc_path, 'r', encoding='utf-8') as f:
    sloc = json.load(f)

py_sloc = sloc['summary']['py_sloc']
js_sloc = sloc['summary']['js_sloc']
total_sloc = sloc['summary']['total_sloc']
KLOC = total_sloc / 1000.0

# COCOMO basic model parameters (semi-detached)
a = 3.0
b = 1.12
c = 2.5
d = 0.35

effort_pm = a * (KLOC ** b)  # person-months
tdev_months = c * (effort_pm ** d)
people_required = max(1, effort_pm / tdev_months)

# Use provided team size (4 members)
team_size = 4
# Cost assumptions (user can change): USD per person-month
cost_per_pm = 4000.0

total_cost = effort_pm * cost_per_pm

# Work division (example for 4 members)
# Roles: Backend/API, ML/Data, Frontend, QA/Docs
role_distribution = [
    ('Backend / API', 0.40),
    ('ML & Data / Algorithms', 0.30),
    ('Frontend / UI', 0.15),
    ('QA & Documentation', 0.15),
]

role_allocations = []
for role, frac in role_distribution:
    pm = effort_pm * frac
    cost = pm * cost_per_pm
    role_allocations.append({'role': role, 'fraction': frac, 'person_months': pm, 'cost': cost})

# Per-person allocation (divide roles across 4 members)
# For simplicity assign one primary role per person with percentages
person_assignments = [
    {'name': 'Member 1', 'role': 'Backend / API', 'share': 0.40},
    {'name': 'Member 2', 'role': 'ML & Data / Algorithms', 'share': 0.30},
    {'name': 'Member 3', 'role': 'Frontend / UI', 'share': 0.15},
    {'name': 'Member 4', 'role': 'QA & Documentation', 'share': 0.15},
]
for p in person_assignments:
    p['person_months'] = effort_pm * p['share']
    p['cost'] = p['person_months'] * cost_per_pm

# Build PDF
pdf_file = os.path.join(root, 'MedPredict_Detailed_Report_COCOMO.pdf')
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('title', parent=styles['Heading1'], fontSize=20, alignment=TA_CENTER)
heading = ParagraphStyle('heading', parent=styles['Heading2'], fontSize=12)
body = ParagraphStyle('body', parent=styles['BodyText'], fontSize=10, alignment=TA_JUSTIFY)

content = []
content.append(Paragraph('MedPredict - Detailed Report (Algorithms & COCOMO Estimation)', title_style))
content.append(Spacer(1, 0.2*inch))
content.append(Paragraph(f'Date: {datetime.now().strftime("%B %d, %Y")}', styles['Normal']))
content.append(Spacer(1, 0.2*inch))

# SLOC Summary
content.append(Paragraph('1. Source Lines of Code (SLOC) Summary', heading))
sloc_text = f"""
- Python SLOC (excluding comments/blank lines): {py_sloc}
- JavaScript SLOC (excluding comments/blank lines): {js_sloc}
- Total SLOC: {total_sloc}
- KLOC (thousands of lines): {KLOC:.3f}
"""
content.append(Paragraph(sloc_text.replace('\n','<br/>'), body))
content.append(Spacer(1, 0.15*inch))

# COCOMO results
content.append(Paragraph('2. COCOMO Basic Estimation (Semi-Detached Mode)', heading))
explain = "We use the Basic COCOMO model (Semi-Detached):\nEffort (Person-Months) = a * (KLOC)^b\nDevelopment Time (Months) = c * (Effort)^d\nParameters used: a=3.0, b=1.12, c=2.5, d=0.35"
content.append(Paragraph(explain.replace('\n','<br/>'), body))
content.append(Spacer(1, 0.1*inch))

coco_text = f"""
Calculated values:
- KLOC = {KLOC:.3f}
- Effort = {effort_pm:.2f} person-months
- Development Time = {tdev_months:.2f} months
- People required (Effort / Time) = {people_required:.2f}
- Team size (given) = {team_size}
- Assumed cost per person-month = ${cost_per_pm:,.2f}
- Estimated total cost = ${total_cost:,.2f}
"""
content.append(Paragraph(coco_text.replace('\n','<br/>'), body))
content.append(Spacer(1, 0.15*inch))

# Role Allocation Table
content.append(Paragraph('3. Role-based Person-Months & Cost Allocation', heading))
table_data = [['Role', 'Share', 'Person-Months', 'Cost (USD)']]
for r in role_allocations:
    table_data.append([r['role'], f"{r['fraction']*100:.0f}%", f"{r['person_months']:.2f}", f"${r['cost']:,.2f}"])

table = Table(table_data, colWidths=[2.5*inch, 1*inch, 1.3*inch, 1.4*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E78')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(2,1),(-1,-1),'CENTER'),
    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
]))
content.append(table)
content.append(Spacer(1, 0.15*inch))

# Per-person assignment
content.append(Paragraph('4. Team Division (4 members)', heading))
pa_text = 'Suggested primary responsibilities and their person-months & cost allocations.'
content.append(Paragraph(pa_text, body))
content.append(Spacer(1, 0.1*inch))
pa_table = [['Member', 'Primary Role', 'Person-Months', 'Cost (USD)']]
for p in person_assignments:
    pa_table.append([p['name'], p['role'], f"{p['person_months']:.2f}", f"${p['cost']:,.2f}"])

pt = Table(pa_table, colWidths=[1.2*inch, 2.2*inch, 1.3*inch, 1.4*inch])
pt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E78')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
]))
content.append(pt)
content.append(Spacer(1, 0.2*inch))

# Algorithms detailed section
content.append(Paragraph('5. Detailed Algorithm Application', heading))
alg_text = """
MedPredict applies the following algorithms and techniques:

- Symptom Matching: k-Nearest Neighbors (k-NN) using Jaccard similarity as the distance measure between symptom sets. Symptoms are treated as unordered categorical features; Jaccard gives an interpretable overlap measure.

- Prediction Process: For a new input, calculate Jaccard(user_symptoms, disease_symptoms) for each disease. Take top-k diseases (k=5 default). Use majority voting among neighbors and compute confidence as (votes for top disease)/k.

- Risk Scoring: Multi-factor additive model combining confidence (0-20), disease severity (10-80), age factor (0-15), comorbidity points (0-15), lab abnormalities (0-20). Sum gives 0-100 risk score.

- PDF Lab Parsing: PyPDF2-based text extraction, regex pattern matching for lab labels/values. Values are compared against clinical ranges to award abnormality points.

- Ensemble & Explainability: Predictions display which symptoms matched and contribution of lab abnormalities and age to the final risk. This preserves traceability for clinician review.
"""
content.append(Paragraph(alg_text.replace('\n','<br/>'), body))
content.append(Spacer(1, 0.2*inch))

# Recommendations & Next steps
content.append(Paragraph('6. Recommendations & Next Steps', heading))
rec_text = """
- Validate model with real annotated clinical cases to improve accuracy.
- Add unit tests and dataset versioning to support repeatable COCOMO re-estimates.
- For production, migrate JSON storage to a proper DB (PostgreSQL) and use Redis for caching.
- Consider migrating to an ISO/medical-device-compliant pipeline if pursuing regulatory approval.
- For cost refinement: select realistic local person-month rates and recompute.
"""
content.append(Paragraph(rec_text.replace('\n','<br/>'), body))
content.append(Spacer(1, 0.2*inch))

# Footer
content.append(PageBreak())
content.append(Paragraph('Appendix: Per-file SLOC (selected)', heading))
file_table = [['File', 'Lang', 'SLOC']]
for f in sloc['files']:
    file_table.append([f['path'], f['lang'], str(f['sloc'])])
ft = Table(file_table, colWidths=[3.5*inch, 0.6*inch, 1*inch])
ft.setStyle(TableStyle([
    ('GRID',(0,0),(-1,-1),0.25,colors.grey),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1F4E78')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
]))
content.append(ft)

# Build
os.makedirs(root, exist_ok=True)
doc.build(content)
print('Generated', pdf_file)
print('Effort (person-months):', f"{effort_pm:.2f}")
print('Development time (months):', f"{tdev_months:.2f}")
print('Estimated total cost (USD):', f"${total_cost:,.2f}")
