import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import matplotlib.pyplot as plt
import io


def generate_graph():
    plt.figure(figsize=(4, 4))
    data = [25, 50, 75, 100]
    labels = ['A', 'B', 'C', 'D']
    plt.bar(labels, data)
    plt.title('Sample Bar Graph')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='PNG')
    buffer.seek(0)
    return buffer

def draw_header(c, width, height):
    
    
    c.setFont("Helvetica-Bold", 12)
    company_name = "ANDREW YULE & COMPANY LIMITED"
    company_text_width = c.stringWidth(company_name, "Helvetica-Bold", 20)
    company_center = (width - company_text_width) / 2
    c.drawString(company_center, height - 50, company_name)
    
    
    small_text = "(A GOVERNMENT OF INDIA ENTERPRISE)"
    small_text_width = c.stringWidth(small_text, "Helvetica", 12)
    small_text_center = (width - small_text_width) / 2
    c.drawString(small_text_center, height - 70, small_text)
    
    
    sub_header = "ENGINEERING DIVISION"
    sub_header_width = c.stringWidth(sub_header, "Helvetica-Bold", 16)
    sub_header_center = (width - sub_header_width) / 2
    c.drawString(sub_header_center, height - 90, sub_header)
    

    c.line(100, height - 100, width - 100, height - 100)

def save_as_pdf(data):
    c = canvas.Canvas("form_output.pdf", pagesize=letter)
    width, height = letter
    
    # First Page
    draw_header(c, width, height)
    c.setFont("Helvetica", 10)
    c.drawString(100, height - 120, f"REPORT NO: {data['REPORT NO']}")
    c.drawRightString(width - 100, height - 120, f"DATED: {data['DATED']}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(100, height - 140, f"REPORT ON PERFORMANCE TEST AS: PER BS:848-L-2007")
    c.setFont("Helvetica", 10)
    y = height - 160
    fields = [
        f"FAN SIZE & TYPE: {data['FAN SIZE & TYPE']}",
        f"c.A.DRc NO.: {data['c.A.DRc NO.']}",
        f"CLINT: {data['CLINT']}",
        f"A/C: {data['A/C']}",
        f"PURCHASE ORDER NO.: {data['PURCHASE ORDER NO.']}",
        f"DATE: {data['DATE']}",
        f"WORK ORDER NO.: {data['WORK ORDER NO.']}",
        f"FAN NUMBER: {data['FAN NUMBER']}",
        f"R.H.r RUNNER NO.: {data['R.H.r RUNNER NO.']}",
        f"DATE OF TEST: {data['DATE OF TEST']}",
        f"SITE OF TEST: {data['SITE OF TEST']}",
        f"WITNESSED BY: {data['WITNESSED BY 1']}",
        f"WITNESSED BY: {data['WITNESSED BY 2']}",
    ]
    for field in fields:
        c.drawString(100, y, field)
        y -= 20

    y -= 20
    contents = [
        "CONTENTS OF REPORT ITEM:",
        "1. TEST REPORT: PAGE 1",
        "2. COMPUTED TEST DATA SHEET: PAGE 2",
        "3. TEST RESULT: PAGE 3",
        "4. SAMPLE CALCULATION: PAGE 4 TO 6",
        "5. FAN PERFORMANCE CURVE: PAGE 7",
        "6. FIELD PT DATA SHEET: PAGE 8",
        "7. MRT TEST DATA SHEET: PAGE 9"
    ]
    for content in contents:
        c.drawString(100, y, content)
        y -= 20

    y -= 20
    variations = [
        "PERCENT VARIATION: ACTUAL DUTY FROM SPECIFIED DUTY:",
        "AT INLET DAMPER CLOSING (IN DEG.): FULL OPEN",
        "(PLEASE REFERENCE PERFORMANCE CURVE OBTAINED FROM TEST READINGS)",
        "PERCENT VARIATION:",
        "(1) FLOW RATE: (+)0.36 %",
        "(2) SHAFT POWER: (-) 1.18 %",
        "(3) STATIC EFFICIENCY: (+)2.18 %",
        "(FAN PERFORMANCE TEST DONE AS PER AGREED CLASS 'B' TOLERANCE LIMIT OF PERFORMANCE",
        "TEST PROCEDURE BS:848-1 1980ie. VOL. FLOW: -5.0%, POWER: +10%, STATIC EFFY: -3.0%)",
        "FOR ANDREW YULE & CO. LIMITED"
    ]
    for variation in variations:
        c.drawString(100, y, variation)
        y -= 20

    c.showPage()

    # Additional Pages with Graph
    c.drawString(100, height - 100, "Form Output - Page 2")
    graph_buffer = generate_graph()
    graph_image = ImageReader(graph_buffer)
    c.drawImage(graph_image, 100, height - 500, width=400, height=400)
    c.showPage()
    
    

    c.save()
    messagebox.showinfo("Success", "Form saved as PDF!")

def submit_form():
    data = {
        "REPORT NO": report_no_var.get(),
        "DATED": dated_var.get(),
        "FAN SIZE & TYPE": fan_size_type_var.get(),
        "c.A.DRc NO.": cadr_no_var.get(),
        "CLINT": clint_var.get(),
        "A/C": ac_var.get(),
        "PURCHASE ORDER NO.": purchase_order_no_var.get(),
        "DATE": date_var.get(),
        "WORK ORDER NO.": work_order_no_var.get(),
        "FAN NUMBER": fan_number_var.get(),
        "R.H.r RUNNER NO.": rhr_runner_no_var.get(),
        "DATE OF TEST": date_of_test_var.get(),
        "SITE OF TEST": site_of_test_var.get(),
        "WITNESSED BY 1": witnessed_by_1_var.get(),
        "WITNESSED BY 2": witnessed_by_2_var.get()
    }
    save_as_pdf(data)

app = tk.Tk()
app.title("Form App")

# Defining Labels and Entries for all required fields
labels = [
    "REPORT NO", "DATED", "FAN SIZE & TYPE", "c.A.DRc NO.",
    "CLINT", "A/C", "PURCHASE ORDER NO.", "DATE",
    "WORK ORDER NO.", "FAN NUMBER", "R.H.r RUNNER NO.",
    "DATE OF TEST", "SITE OF TEST", "WITNESSED BY 1", "WITNESSED BY 2"
]

variables = {}
for idx, label in enumerate(labels):
    tk.Label(app, text=f"{label}:").grid(row=idx, column=0, padx=10, pady=5)
    var = tk.StringVar()
    tk.Entry(app, textvariable=var).grid(row=idx, column=1, padx=10, pady=5)
    variables[label] = var

# Assigning variables to specific keys
report_no_var = variables["REPORT NO"]
dated_var = variables["DATED"]
fan_size_type_var = variables["FAN SIZE & TYPE"]
cadr_no_var = variables["c.A.DRc NO."]
clint_var = variables["CLINT"]
ac_var = variables["A/C"]
purchase_order_no_var = variables["PURCHASE ORDER NO."]
date_var = variables["DATE"]
work_order_no_var = variables["WORK ORDER NO."]
fan_number_var = variables["FAN NUMBER"]
rhr_runner_no_var = variables["R.H.r RUNNER NO."]
date_of_test_var = variables["DATE OF TEST"]
site_of_test_var = variables["SITE OF TEST"]
witnessed_by_1_var = variables["WITNESSED BY 1"]
witnessed_by_2_var = variables["WITNESSED BY 2"]

tk.Button(app, text="Submit", command=submit_form).grid(row=len(labels), columnspan=2, pady=20)

app.mainloop()
