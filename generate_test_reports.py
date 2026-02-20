#!/usr/bin/env python3
"""
Generate realistic sample medical test reports as PDFs for testing the app.
Each PDF contains realistic lab values and formatted output.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime, timedelta
import random
import os

# Output folder
OUTPUT_FOLDER = "."

def create_cbc_report():
    """Complete Blood Count (CBC) report"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_cbc_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Header
    elements.append(Paragraph("COMPLETE BLOOD COUNT (CBC)", styles['Heading1']))
    elements.append(Paragraph("Pathology Laboratory Report", styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Patient info
    patient_data = [
        ["Patient Name:", "John Doe"],
        ["Age:", "35 years"],
        ["Gender:", "Male"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Sample Type:", "Whole Blood (EDTA)"]
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    # Lab values
    elements.append(Paragraph("Laboratory Results:", styles['Heading2']))
    
    lab_data = [
        ["Test Parameter", "Result", "Unit", "Reference Range", "Status"],
        ["Hemoglobin (Hb)", "14.5", "g/dL", "13.5-17.5", "Normal"],
        ["Hematocrit (Hct)", "43.2", "%", "38-50", "Normal"],
        ["WBC Count", "7200", "/µL", "4500-11000", "Normal"],
        ["Red Blood Cells", "4.8", "Million/µL", "4.5-5.5", "Normal"],
        ["Platelets", "245000", "/µL", "150000-400000", "Normal"],
        ["Mean Corpuscular Volume", "88", "fL", "80-100", "Normal"],
        ["Mean Corpuscular Hemoglobin", "28", "pg", "26-32", "Normal"],
    ]
    
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1*inch, 1.5*inch, 1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("No abnormalities detected. All values within normal range.", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Pathologist: Dr. Sharma | Signature: _______", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_blood_sugar_report():
    """Blood Sugar / Glucose report"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_blood_sugar_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("BLOOD GLUCOSE TEST REPORT", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "Jane Smith"],
        ["Age:", "42 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Sample Type:", "Serum"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Test Results:", styles['Heading2']))
    
    lab_data = [
        ["Test Parameter", "Result", "Unit", "Reference Range", "Interpretation"],
        ["Fasting Blood Sugar (FBS)", "98", "mg/dL", "70-100", "Normal"],
        ["Post Prandial (PP) - 2 hrs", "135", "mg/dL", "<140", "Normal"],
        ["Random Blood Sugar", "110", "mg/dL", "<140 (random)", "Normal"],
        ["HbA1c (Glycated Hemoglobin)", "5.8", "%", "<5.7", "Normal"],
    ]
    
    t = Table(lab_data, colWidths=[2*inch, 1*inch, 1*inch, 1.5*inch, 1.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Interpretation: Patient shows normal glucose metabolism. No signs of diabetes or impaired glucose tolerance.", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    elements.append(Paragraph("Lab Director: Dr. Patel | Approved: _______", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_kidney_function_report():
    """Kidney Function Test report"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_kidney_function_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("KIDNEY FUNCTION TEST (KFT)", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "Robert Johnson"],
        ["Age:", "55 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Sample Type:", "Serum"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Test Results:", styles['Heading2']))
    
    lab_data = [
        ["Parameter", "Result", "Unit", "Normal Range", "Status"],
        ["Creatinine", "0.9", "mg/dL", "0.7-1.3", "Normal"],
        ["BUN (Blood Urea Nitrogen)", "16", "mg/dL", "7-20", "Normal"],
        ["eGFR (Estimated GFR)", "92", "mL/min/1.73m²", ">60", "Normal"],
        ["Sodium (Na)", "138", "mEq/L", "135-145", "Normal"],
        ["Potassium (K)", "4.1", "mEq/L", "3.5-5.0", "Normal"],
        ["Chloride (Cl)", "102", "mEq/L", "96-106", "Normal"],
        ["Phosphorus", "3.5", "mg/dL", "2.5-4.5", "Normal"],
        ["Calcium", "9.2", "mg/dL", "8.5-10.2", "Normal"],
    ]
    
    t = Table(lab_data, colWidths=[1.8*inch, 1*inch, 1*inch, 1.3*inch, 1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Interpretation: Kidney function is normal. No renal impairment detected.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_dengue_ns1_report():
    """Dengue NS1 Antigen Test report"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_dengue_ns1_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("DENGUE NS1 ANTIGEN TEST", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "Maria Garcia"],
        ["Age:", "28 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Referred By:", "Dr. Kumar"],
        ["Clinical Symptoms:", "Fever, Headache, Body Ache"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Test Result:", styles['Heading2']))
    
    result_data = [
        ["Test", "Result", "Interpretation"],
        ["Dengue NS1 Antigen", "POSITIVE", "Acute dengue infection detected"],
        ["Dengue IgM Antibody", "NEGATIVE", "Early phase - IgM not yet developed"],
        ["Dengue IgG Antibody", "NEGATIVE", "Primary infection (not secondary)"],
    ]
    
    t = Table(result_data, colWidths=[2*inch, 1.5*inch, 2.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("<b>Clinical Recommendation:</b> Patient has acute dengue infection. Recommend supportive care, hydration, rest, and close monitoring. Platelet count and hematocrit should be monitored daily.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_malaria_test_report():
    """Malaria Test report (Blood Smear & RDT)"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_malaria_test_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("MALARIA TEST REPORT", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "Raj Kumar"],
        ["Age:", "38 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Clinical Symptoms:", "Intermittent Fever, Chills, Sweating"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Test Results:", styles['Heading2']))
    
    result_data = [
        ["Test Method", "Result", "Species Detected", "Parasitemia"],
        ["Blood Smear Microscopy", "POSITIVE", "Plasmodium falciparum", "2.5% RBCs"],
        ["Rapid Diagnostic Test (RDT)", "POSITIVE", "P. falciparum specific", "Confirmed"],
    ]
    
    t = Table(result_data, colWidths=[2*inch, 1.3*inch, 1.5*inch, 1.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("<b>Clinical Recommendation:</b> Confirmed case of Plasmodium falciparum malaria. Start artemisinin-based combination therapy (ACT) immediately. Follow-up blood smear at Day 2 and Day 28.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_widal_test_report():
    """Widal Test report (Typhoid)"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_widal_test_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("WIDAL TEST REPORT (TYPHOID SEROLOGY)", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "Priya Singh"],
        ["Age:", "32 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Clinical Symptoms:", "Prolonged Fever, Headache, Abdominal Pain"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("Test Results:", styles['Heading2']))
    
    result_data = [
        ["Antigen", "Titer", "Result", "Interpretation"],
        ["O Antigen (TO Ag)", "1:160", "POSITIVE", "Suggestive of acute typhoid"],
        ["H Antigen (TH Ag)", "1:320", "POSITIVE", "Suggestive of acute typhoid"],
        ["AH Antigen (TAH Ag)", "Negative", "NEGATIVE", "No paratyphoid"],
        ["BH Antigen (TBH Ag)", "Negative", "NEGATIVE", "No paratyphoid B"],
    ]
    
    t = Table(result_data, colWidths=[1.5*inch, 1*inch, 1.2*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("<b>Clinical Recommendation:</b> Widal test shows positive titers suggestive of active typhoid fever. Recommend blood culture confirmation and start fluoroquinolone or cephalosporin therapy.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

def create_ecg_report():
    """ECG (Electrocardiogram) report"""
    filename = os.path.join(OUTPUT_FOLDER, "sample_ecg_report.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("ELECTROCARDIOGRAM (ECG) REPORT", styles['Heading1']))
    elements.append(Spacer(1, 0.2*inch))
    
    patient_data = [
        ["Patient Name:", "David Brown"],
        ["Age:", "65 years"],
        ["Test Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Test Time:", datetime.now().strftime("%H:%M:%S")],
        ["Clinical Symptoms:", "Chest Pain, Palpitations, Shortness of Breath"],
    ]
    pt = Table(patient_data, colWidths=[2*inch, 3*inch])
    pt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(pt)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("ECG Findings:", styles['Heading2']))
    
    finding_data = [
        ["Parameter", "Value", "Normal Range", "Status"],
        ["Heart Rate", "78 bpm", "60-100 bpm", "Normal"],
        ["PR Interval", "160 ms", "120-200 ms", "Normal"],
        ["QRS Duration", "90 ms", "<120 ms", "Normal"],
        ["QT Interval (Corrected)", "420 ms", "<450 ms", "Normal"],
        ["Axis", "Normal (+45°)", "-30° to +90°", "Normal"],
    ]
    
    t = Table(finding_data, colWidths=[1.8*inch, 1.2*inch, 1.5*inch, 1*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 0.3*inch))
    
    elements.append(Paragraph("ECG Interpretation:", styles['Heading2']))
    elements.append(Paragraph("Normal sinus rhythm with no acute ST-segment changes. No signs of acute myocardial infarction. No significant arrhythmias detected.", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    elements.append(Paragraph("<b>Cardiologist Recommendation:</b> ECG is normal. Patient appears to be low risk. Recommend stress test if chest pain persists.", styles['Normal']))
    
    doc.build(elements)
    print(f"✓ Created: {filename}")

if __name__ == "__main__":
    print("Generating sample medical test reports as PDFs...\n")
    
    try:
        create_cbc_report()
        create_blood_sugar_report()
        create_kidney_function_report()
        create_dengue_ns1_report()
        create_malaria_test_report()
        create_widal_test_report()
        create_ecg_report()
        
        print("\n✅ All sample reports generated successfully!")
        print(f"📁 Reports saved in: {os.path.abspath(OUTPUT_FOLDER)}")
        
    except Exception as e:
        print(f"❌ Error generating reports: {e}")
