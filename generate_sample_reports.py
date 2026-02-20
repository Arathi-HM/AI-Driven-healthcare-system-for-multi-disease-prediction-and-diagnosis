"""Generate sample PDF test reports for each lab/test.

This script produces three example reports (low, medium, high)
for each test in the TESTS list and writes them to `sample_reports/`.
"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from datetime import datetime
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), 'sample_reports')
os.makedirs(OUT_DIR, exist_ok=True)

TESTS = [
	'widal',
	'dengue_ns1',
	'malaria_test',
	'blood_sugar',
	'kidney_function',
	'ecg',
	'cbc'
]

SEVERITY = ['low', 'medium', 'high']

def make_report(test_name, severity):
	filename = f"{test_name}_{severity}.pdf"
	path = os.path.join(OUT_DIR, filename)
	c = canvas.Canvas(path, pagesize=A4)
	width, height = A4
	margin = 20 * mm
	x = margin
	y = height - margin

	# Header
	c.setFont('Helvetica-Bold', 16)
	c.drawString(x, y, 'MedPredict - Sample Test Report')
	c.setFont('Helvetica', 9)
	c.drawRightString(width - margin, y, datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'))
	y -= 14
	c.line(x, y, width - margin, y)
	y -= 18

	# Patient / test summary
	c.setFont('Helvetica-Bold', 12)
	c.drawString(x, y, f'Test: {test_name.replace("_"," ").title()}')
	y -= 16
	c.setFont('Helvetica', 10)
	c.drawString(x, y, f'Severity Example: {severity.title()}')
	y -= 14
	c.drawString(x, y, 'Patient: John Doe')
	y -= 12
	c.drawString(x, y, 'Age: 35')
	y -= 12
	c.drawString(x, y, 'Gender: Male')
	y -= 18

	# Findings box
	c.setFont('Helvetica-Bold', 11)
	c.drawString(x, y, 'Findings:')
	y -= 14
	c.setFont('Helvetica', 10)
	# Per-test sample numeric values
	sample_fields = {
		'widal': [('O (titer)', None), ('H (titer)', None)],
		'dengue_ns1': [('NS1 (index)', None), ('IgM (index)', None), ('IgG (index)', None)],
		'malaria_test': [('Parasite %', None), ('p.falciparum antigen', None)],
		'blood_sugar': [('Fasting (mg/dL)', None), ('Postprandial (mg/dL)', None), ('HbA1c (%)', None)],
		'kidney_function': [('Creatinine (mg/dL)', None), ('BUN (mg/dL)', None), ('eGFR (mL/min)', None)],
		'ecg': [('Heart Rate (bpm)', None), ('PR (ms)', None), ('QRS (ms)', None), ('QTc (ms)', None)],
		'cbc': [('Hemoglobin (g/dL)', None), ('WBC (×10^3/µL)', None), ('Platelets (×10^3/µL)', None)]
	}

	# numeric generator ranges per severity
	ranges = {
		'widal': {
			'low': [(1,1),(1,1)],
			'medium': [(1,80),(1,80)],
			'high': [(160,1280),(160,1280)]
		},
		'dengue_ns1': {
			'low': [(0,0.5),(0,0.5),(0,0.5)],
			'medium': [(0.6,1.5),(0.6,1.5),(0.6,1.5)],
			'high': [(1.6,5),(1.6,5),(1.6,5)]
		},
		'malaria_test': {
			'low': [(0,0.1),(0,0)],
			'medium': [(0.2,1),(0,1)],
			'high': [(1.1,10),(1,1)]
		},
		'blood_sugar': {
			'low': [(70,99),(90,139),(4.0,5.6)],
			'medium': [(100,125),(140,199),(5.7,6.4)],
			'high': [(126,250),(200,400),(6.5,14)]
		},
		'kidney_function': {
			'low': [(0.6,1.2),(7,20),(90,120)],
			'medium': [(1.3,2.0),(21,40),(45,89)],
			'high': [(2.1,6.0),(41,120),(5,44)]
		},
		'ecg': {
			'low': [(60,90),(120,200),(80,110),(350,430)],
			'medium': [(50,100),(110,220),(90,140),(430,470)],
			'high': [(30,140),(90,300),(120,220),(470,700)]
		},
		'cbc': {
			'low': [(13.5,17.5),(4.0,10.0),(150,450)],
			'medium': [(11.0,13.4),(3.5,11.0),(120,149)],
			'high': [(7.0,10.9),(11.1,30.0),(20,119)]
		}
	}

	import random
	fields = sample_fields.get(test_name, [])
	vals = []
	if test_name in ranges:
		rlist = ranges[test_name][severity]
		for i, fld in enumerate(fields):
			lo, hi = rlist[i]
			if isinstance(lo, int) and isinstance(hi, int):
				v = random.randint(lo, hi)
			else:
				v = round(random.uniform(lo, hi), 2)
			vals.append((fld[0], v))
	else:
		vals = [(f[0], 'N/A') for f in fields]

	# Write the values into the report
	for name, value in vals:
		c.drawString(x + 6*mm, y, f'• {name}: {value}')
		y -= 12

	# derive risk text
	if severity == 'low':
		risk = 'Low'
	elif severity == 'medium':
		risk = 'Moderate'
	else:
		risk = 'High'

	y -= 6
	c.setFont('Helvetica-Bold', 11)
	c.drawString(x, y, 'Interpretation:')
	y -= 14
	c.setFont('Helvetica', 10)
	interp = f'Test {test_name} demonstrates a {risk.lower()} risk pattern in this example ({severity}).'
	c.drawString(x + 6*mm, y, interp)
	y -= 18

	# Recommendations
	c.setFont('Helvetica-Bold', 11)
	c.drawString(x, y, 'Recommendations:')
	y -= 14
	c.setFont('Helvetica', 10)
	if severity == 'low':
		recs = ['Routine monitoring as part of general health checks.']
	elif severity == 'medium':
		recs = ['Repeat test in 1-2 weeks, consult primary physician.']
	else:
		recs = ['Immediate clinical consultation; consider urgent referral.']

	for r in recs:
		c.drawString(x + 6*mm, y, f'• {r}')
		y -= 12

	# Footer
	y = 30 * mm
	c.setFont('Helvetica-Oblique', 8)
	c.drawString(x, y, 'This is a sample generated report for demonstration purposes only. Not a clinical diagnosis.')

	c.showPage()
	c.save()
	print(f'Wrote {path}')

def main():
	for t in TESTS:
		for s in SEVERITY:
			make_report(t, s)

if __name__ == '__main__':
	main()
