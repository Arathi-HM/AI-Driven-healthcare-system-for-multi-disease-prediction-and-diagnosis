#!/usr/bin/env python3
"""
Generate comprehensive risk-level medical test reports (Low, Medium, High risk) for all test types.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime
import os

OUTPUT_FOLDER = "."

def add_header_footer(story, doc, title):
    """Add header and footer to document"""
    story.insert(0, Paragraph(title, getSampleStyleSheet()['Heading1']))
    story.insert(1, Paragraph("Risk Assessment Report", getSampleStyleSheet()['Normal']))
    story.insert(2, Spacer(1, 0.2*inch))

# ===== CBC REPORTS =====
def create_cbc_low_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_cbc_LOW_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("CBC - LOW RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Alice Johnson | Age: 28 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Risk"],
        ["Hemoglobin (Hb)", "13.8", "13.5-17.5 g/dL", "✓ Normal"],
        ["WBC Count", "7000", "4500-11000 /µL", "✓ Normal"],
        ["Platelets", "280000", "150k-400k /µL", "✓ Normal"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Assessment:</b> All parameters within normal range. No blood disorders detected.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_cbc_medium_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_cbc_MEDIUM_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("CBC - MEDIUM RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Bob Smith | Age: 45 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add plain text values for extraction
    elements.append(Paragraph("<b>Lab Values (Plain Text - for easy parsing):</b>", styles['Normal']))
    elements.append(Paragraph("Hemoglobin: 11.2 g/dL", styles['Normal']))
    elements.append(Paragraph("WBC: 12500 /µL", styles['Normal']))
    elements.append(Paragraph("Platelets: 200000 /µL", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Status"],
        ["Hemoglobin (Hb)", "11.2", "13.5-17.5 g/dL", "⚠ Low - Mild Anemia"],
        ["WBC Count", "12500", "4500-11000 /µL", "⚠ Elevated - Possible Infection"],
        ["Platelets", "200000", "150k-400k /µL", "✓ Normal"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (0, -1), colors.lightyellow),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Assessment:</b> Mild anemia and elevated WBC detected. Recommend iron supplement and infection workup.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_cbc_high_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_cbc_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("CBC - HIGH RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Carlos Martinez | Age: 62 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add plain text values for extraction
    elements.append(Paragraph("<b>Critical Lab Values (Plain Text - for easy parsing):</b>", styles['Normal']))
    elements.append(Paragraph("Hemoglobin: 8.5 g/dL", styles['Normal']))
    elements.append(Paragraph("WBC: 18000 /µL", styles['Normal']))
    elements.append(Paragraph("Platelets: 85000 /µL", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Also add in table format for professional look
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Status"],
        ["Hemoglobin (Hb)", "8.5", "13.5-17.5 g/dL", "🔴 CRITICAL - Severe Anemia"],
        ["WBC Count", "18000", "4500-11000 /µL", "🔴 CRITICAL - Severe Leukocytosis"],
        ["Platelets", "85000", "150k-400k /µL", "🔴 CRITICAL - Thrombocytopenia"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (0, -1), colors.lightcoral),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>URGENT:</b> Severe hematologic abnormalities. Possible leukemia or severe infection. Immediate specialist referral required. Blood transfusion may be needed.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

# ===== BLOOD SUGAR REPORTS =====
def create_blood_sugar_low_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_blood_sugar_LOW_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("BLOOD GLUCOSE - LOW RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Sarah Williams | Age: 35 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Test", "Result", "Normal Range", "Status"],
        ["Fasting Blood Sugar", "92", "70-100 mg/dL", "✓ Normal"],
        ["Post Prandial (2hrs)", "118", "<140 mg/dL", "✓ Normal"],
        ["HbA1c", "5.4", "<5.7%", "✓ Normal"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Status:</b> Excellent glucose control. No diabetes risk.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_blood_sugar_medium_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_blood_sugar_MEDIUM_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("BLOOD GLUCOSE - MEDIUM RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Diana Prince | Age: 50 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Test", "Result", "Normal Range", "Status"],
        ["Fasting Blood Sugar", "110", "70-100 mg/dL", "⚠ Impaired Fasting Glucose"],
        ["Post Prandial (2hrs)", "165", "<140 mg/dL", "⚠ Impaired Glucose Tolerance"],
        ["HbA1c", "6.1", "<5.7%", "⚠ Prediabetes"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Status:</b> Prediabetic state. Lifestyle changes and diet control recommended.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_blood_sugar_high_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_blood_sugar_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("BLOOD GLUCOSE - HIGH RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Edward Norton | Age: 58 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Test", "Result", "Normal Range", "Status"],
        ["Fasting Blood Sugar", "182", "70-100 mg/dL", "🔴 CRITICAL - Diabetes"],
        ["Post Prandial (2hrs)", "285", "<140 mg/dL", "🔴 CRITICAL - Uncontrolled"],
        ["HbA1c", "9.2", "<5.7%", "🔴 CRITICAL - Poorly Controlled"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>URGENT:</b> Type 2 diabetes with poor glycemic control. Immediate endocrinologist consultation. Insulin therapy may be needed.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

# ===== KIDNEY FUNCTION REPORTS =====
def create_kidney_low_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_kidney_function_LOW_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("KIDNEY FUNCTION - LOW RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Frank Castle | Age: 40 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Status"],
        ["Creatinine", "0.8", "0.7-1.3 mg/dL", "✓ Normal"],
        ["eGFR", "102", ">60 mL/min", "✓ Normal"],
        ["BUN", "15", "7-20 mg/dL", "✓ Normal"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Status:</b> Normal kidney function. No intervention needed.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_kidney_medium_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_kidney_function_MEDIUM_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("KIDNEY FUNCTION - MEDIUM RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Grace Hopper | Age: 55 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Status"],
        ["Creatinine", "1.5", "0.7-1.3 mg/dL", "⚠ Stage 2 CKD"],
        ["eGFR", "48", ">60 mL/min", "⚠ Mild-Moderate Reduction"],
        ["BUN", "28", "7-20 mg/dL", "⚠ Elevated"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Status:</b> Stage 2 Chronic Kidney Disease. Monitor closely, control BP & diabetes.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_kidney_high_risk():
    filename = os.path.join(OUTPUT_FOLDER, "sample_kidney_function_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("KIDNEY FUNCTION - HIGH RISK", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Henry Mills | Age: 72 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Parameter", "Result", "Normal Range", "Status"],
        ["Creatinine", "4.2", "0.7-1.3 mg/dL", "🔴 Stage 5 CKD - ESRD"],
        ["eGFR", "8", ">60 mL/min", "🔴 Severe Reduction - <10%"],
        ["BUN", "95", "7-20 mg/dL", "🔴 Severely Elevated"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>URGENT:</b> End-Stage Renal Disease (Stage 5). Dialysis initiation or transplant needed immediately. Nephrologist consultation critical.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

# ===== DENGUE & MALARIA REPORTS =====
def create_dengue_positive():
    filename = os.path.join(OUTPUT_FOLDER, "sample_dengue_ns1_POSITIVE_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("DENGUE NS1 - POSITIVE (HIGH RISK)", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Iris West | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Test", "Result", "Status"],
        ["Dengue NS1 Antigen", "POSITIVE", "🔴 ACUTE INFECTION"],
        ["IgM Antibody", "NEGATIVE", "Early phase"],
        ["Platelets", "65000", "🔴 Thrombocytopenia - High DHF Risk"],
    ]
    t = Table(lab_data, colWidths=[2.5*inch, 1.5*inch, 2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>CRITICAL:</b> Acute dengue with hemorrhagic fever risk. Immediate hospitalization. Daily platelet & hematocrit monitoring. IV fluids & supportive care.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_malaria_positive():
    filename = os.path.join(OUTPUT_FOLDER, "sample_malaria_test_POSITIVE_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("MALARIA TEST - POSITIVE (HIGH RISK)", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Jack Ryan | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Test", "Result", "Status"],
        ["Blood Smear", "POSITIVE", "🔴 Plasmodium falciparum detected"],
        ["Parasitemia", "3.2%", "🔴 SEVERE - >1% is severe malaria"],
        ["RDT", "POSITIVE", "Confirmed positive"],
    ]
    t = Table(lab_data, colWidths=[2.5*inch, 1.5*inch, 2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>URGENT:</b> Severe Plasmodium falciparum malaria. Start artemisinin-based therapy IMMEDIATELY. Hospitalization required. Monitor for cerebral malaria complications.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

# ===== ECG REPORTS =====
def create_ecg_normal():
    filename = os.path.join(OUTPUT_FOLDER, "sample_ecg_NORMAL_LOW_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("ECG - NORMAL (LOW RISK)", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Jessica Jones | Age: 42 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Finding", "Value", "Status"],
        ["Rhythm", "Normal sinus", "✓ Normal"],
        ["Heart Rate", "72 bpm", "✓ Normal"],
        ["ST Segment", "No elevation", "✓ Normal"],
        ["T Waves", "Normal", "✓ Normal"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1.5*inch, 2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>Status:</b> Normal ECG. Low cardiac risk. No acute issues.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_ecg_abnormal():
    filename = os.path.join(OUTPUT_FOLDER, "sample_ecg_ABNORMAL_HIGH_RISK.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("ECG - ABNORMAL (HIGH RISK)", styles['Heading1']))
    elements.append(Spacer(1, 0.15*inch))
    
    elements.append(Paragraph("Patient: Kevin Hart | Age: 68 | Date: " + datetime.now().strftime("%d/%m/%Y"), styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    lab_data = [
        ["Finding", "Value", "Status"],
        ["Rhythm", "Atrial fibrillation", "🔴 ABNORMAL - Arrhythmia"],
        ["Heart Rate", "105 bpm", "⚠ Tachycardia"],
        ["ST Segment", "2mm elevation", "🔴 CRITICAL - MI Pattern"],
        ["T Waves", "Inverted", "🔴 Ischemia"],
    ]
    t = Table(lab_data, colWidths=[2*inch, 1.5*inch, 2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("<b>🚨 CRITICAL:</b> ECG shows acute MI pattern. ACTIVATE EMS IMMEDIATELY. Troponin testing & cardiology consultation urgent.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

if __name__ == "__main__":
    print("Generating comprehensive risk-level medical test reports...\n")
    
    try:
        # CBC Reports
        create_cbc_low_risk()
        create_cbc_medium_risk()
        create_cbc_high_risk()
        
        # Blood Sugar Reports
        create_blood_sugar_low_risk()
        create_blood_sugar_medium_risk()
        create_blood_sugar_high_risk()
        
        # Kidney Function Reports
        create_kidney_low_risk()
        create_kidney_medium_risk()
        create_kidney_high_risk()
        
        # Dengue & Malaria
        create_dengue_positive()
        create_malaria_positive()
        
        # ECG Reports
        create_ecg_normal()
        create_ecg_abnormal()
        
        print("\n✅ All risk-level reports generated successfully!")
        print(f"📁 Reports saved in: {os.path.abspath(OUTPUT_FOLDER)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
