"""Create one PDF containing the notes and outputs from all case studies."""
import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(ROOT_DIR, "Consolidated_Report.pdf")

CASE_METADATA = [
    {
        "id": "01",
        "prob_num": "1",
        "folder": "Case_Study_01_University_Scholarship_Allocation",
        "title": "University Scholarship Allocation System",
        "concepts": "Tuples, Unpacking, Custom Bubble Sort, Nested Lists, Conditionals",
        "py_file": "problem_01_scholarship_allocation.py"
    },
    {
        "id": "02",
        "prob_num": "2",
        "folder": "Case_Study_02_Progressive_Electricity_Billing",
        "title": "Progressive Electricity Billing & Spike Detection",
        "concepts": "Telescopic Slabs, Loops, Consecutive Month Trend Analysis, Tuples",
        "py_file": "problem_02_electricity_billing.py"
    },
    {
        "id": "03",
        "prob_num": "4",
        "folder": "Case_Study_03_Employee_Payroll_Deductions",
        "title": "Employee Payroll & Progressive Deduction Analysis",
        "concepts": "Financial Slabs, Overtime Multipliers, Deductions, Payslip Table",
        "py_file": "problem_04_employee_payroll.py"
    },
    {
        "id": "04",
        "prob_num": "27",
        "folder": "Case_Study_04_Advanced_Numeric_Pattern_Generator",
        "title": "Advanced Numeric Pattern Generator",
        "concepts": "Nested Loops, Coordinate Spacing, Symmetry, Parity Validation",
        "py_file": "problem_27_pattern_generator.py"
    },
    {
        "id": "05",
        "prob_num": "30",
        "folder": "Case_Study_05_Student_Email_Identifier_Validation",
        "title": "Student Email & Registration ID Validation Engine",
        "concepts": "Pure String Parsing (Non-regex), Slicing, Character Automata",
        "py_file": "problem_30_email_identifier_validation.py"
    },
    {
        "id": "06",
        "prob_num": "42",
        "folder": "Case_Study_06_Student_Marks_Matrix_Analysis",
        "title": "Student Marks Matrix Analysis System",
        "concepts": "2D Nested Lists, Row-Major / Column-Major Traversal, Extremums",
        "py_file": "problem_42_marks_matrix_analysis.py"
    },
    {
        "id": "07",
        "prob_num": "46",
        "folder": "Case_Study_07_Inventory_Matrix_Reconciliation",
        "title": "Multi-Warehouse Inventory Matrix Reconciliation",
        "concepts": "Nested Lists, Variance Matrix, Greedy Rebalancing, Transfer Tuples",
        "py_file": "problem_46_inventory_reconciliation.py"
    },
    {
        "id": "08",
        "prob_num": "48",
        "folder": "Case_Study_08_Tuple_Shift_Conflict_Detection",
        "title": "Tuple-Based Employee Shift Conflict Detection",
        "concepts": "Shift Tuples, Unpacking, 24-hr Time Conversion, Interval Intersections",
        "py_file": "problem_48_shift_conflict_detection.py"
    },
    {
        "id": "09",
        "prob_num": "74",
        "folder": "Case_Study_09_Campus_Festival_Financial_Audit",
        "title": "Campus Festival Registration & Financial Audit",
        "concepts": "Duplicate Key Detection, Lists & Tuples, Budget Variance, Balance Sheet",
        "py_file": "problem_74_festival_audit.py"
    },
    {
        "id": "10",
        "prob_num": "100",
        "folder": "Case_Study_10_Smart_Campus_Simulation",
        "title": "Simple Smart Campus Menu",
        "concepts": "Menu Driven (While Loop), 2D Lab Grid, Summary",
        "py_file": "problem_100_smart_campus_simulation.py"
    },
]

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover page

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#4B5563"))

        # Header
        self.drawString(54, 750, "Dr. RVR NRI Institute of Technology | Python Activity-Based Learning (ABL)")
        self.setStrokeColor(colors.HexColor("#D1D5DB"))
        self.setLineWidth(0.5)
        self.line(54, 744, 558, 744)

        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_str)
        self.drawString(54, 36, "Confidential - Department of Computer Science & Engineering")
        self.line(54, 46, 558, 46)

        self.restoreState()


def build_pdf():
    print("Building Consolidated Technical Report PDF...")
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#374151"),
        alignment=1
    )
    univ_style = ParagraphStyle(
        'UnivStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        textColor=colors.HexColor("#111827"),
        alignment=1
    )
    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1F2937"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'ReportBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=6
    )
    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor("#111827"),
        backColor=colors.HexColor("#F3F4F6"),
        borderColor=colors.HexColor("#E5E7EB"),
        borderWidth=0.5,
        borderPadding=6,
        spaceAfter=8,
        keepWithNext=False
    )

    story = []

    # ==================== COVER PAGE ====================
    story.append(Spacer(1, 20))
    story.append(Paragraph("DR. RVR NRI INSTITUTE OF TECHNOLOGY", univ_style))
    story.append(Paragraph("(An Institution Deemed to be University u/s 3 of UGC Act, 1956)", ParagraphStyle('SubUniv', fontName='Helvetica', fontSize=9, alignment=1, textColor=colors.HexColor("#4B5563"))))
    story.append(Paragraph("Pothavarappadu (V), Agiripalli (M), Eluru Dist., Vijayawada Rural, A.P. - 521212", ParagraphStyle('SubUniv2', fontName='Helvetica', fontSize=8, alignment=1, textColor=colors.HexColor("#6B7280"))))
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1E3A8A"), spaceAfter=25))

    story.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING", ParagraphStyle('Dept', fontName='Helvetica-Bold', fontSize=12, alignment=1, textColor=colors.HexColor("#1E40AF"))))
    story.append(Spacer(1, 15))
    story.append(Paragraph("ACTIVITY-BASED LEARNING (ABL) ASSIGNMENT REPORT", title_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Course: Python Programming (I B.Tech. - Academic Year 2026-2027)", subtitle_style))
    story.append(Spacer(1, 30))

    # Student Details Table
    student_table_data = [
        [Paragraph("<b>Student Name</b>", body_style), Paragraph("[Student Name]", body_style)],
        [Paragraph("<b>Roll Number</b>", body_style), Paragraph("[Roll Number / 26B91AXXXX]", body_style)],
        [Paragraph("<b>Branch & Specialization</b>", body_style), Paragraph("Computer Science and Engineering (CSE)", body_style)],
        [Paragraph("<b>Section</b>", body_style), Paragraph("Section - A", body_style)],
        [Paragraph("<b>Semester / Year</b>", body_style), Paragraph("I B.Tech. - I Semester", body_style)],
        [Paragraph("<b>GitHub Repository</b>", body_style), Paragraph("Python-Activity-Based-Learning", body_style)],
        [Paragraph("<b>Submission Date</b>", body_style), Paragraph("After Dussehra Holidays (October 2026)", body_style)],
    ]
    t_student = Table(student_table_data, colWidths=[180, 280])
    t_student.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F9FAFB")),
        ('BOX', (0, 0), (-1, -1), 1.5, colors.HexColor("#1E3A8A")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(t_student)

    story.append(Spacer(1, 40))

    # Signature Block
    sig_data = [
        [Paragraph("<b>Student Signature</b><br/><br/>_____________________", body_style),
         Paragraph("<b>Course Coordinator</b><br/><br/>_____________________", body_style),
         Paragraph("<b>Dean, School of Computer Studies</b><br/><br/>_____________________", body_style)]
    ]
    t_sig = Table(sig_data, colWidths=[150, 150, 160])
    t_sig.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_sig)

    story.append(PageBreak())

    # ==================== TABLE OF CONTENTS & SYLLABUS MAPPING ====================
    story.append(Paragraph("TABLE OF CONTENTS & CASE STUDY CATALOG", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1E3A8A"), spaceAfter=15))

    toc_rows = [
        [Paragraph("<b>No.</b>", body_style), Paragraph("<b>Prob #</b>", body_style), Paragraph("<b>Case Study Title</b>", body_style), Paragraph("<b>Core Concepts & Syllabus Mapping</b>", body_style)]
    ]
    for m in CASE_METADATA:
        toc_rows.append([
            Paragraph(f"<b>CS-{m['id']}</b>", body_style),
            Paragraph(f"#{m['prob_num']}", body_style),
            Paragraph(f"<b>{m['title']}</b>", body_style),
            Paragraph(m['concepts'], body_style)
        ])

    t_toc = Table(toc_rows, colWidths=[40, 45, 185, 190])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#9CA3AF")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_toc)

    story.append(Spacer(1, 20))
    story.append(Paragraph("SYLLABUS COMPLIANCE CERTIFICATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1E3A8A"), spaceAfter=12))

    compliance_text = (
        "This consolidated report confirms that all 10 developed solutions adhere strictly to the "
        "assigned Python Programming syllabus: <b>computational thinking, algorithms, flowcharts, "
        "pseudocode, variables, data types, operators, conditional statements, loops, strings, pattern generation, "
        "lists, nested lists, tuples, tuple operations, and unpacking</b>. "
        "In strict adherence to academic regulations, <b>no dictionaries ({}), sets, object-oriented classes, "
        "or external libraries (e.g., NumPy, Pandas, Regex)</b> have been utilized in any case study solution."
    )
    story.append(Paragraph(compliance_text, body_style))

    story.append(PageBreak())

    # ==================== CASE STUDY CHAPTERS ====================
    for idx, m in enumerate(CASE_METADATA, 1):
        folder_path = os.path.join(ROOT_DIR, m["folder"])
        doc_path = os.path.join(folder_path, "documentation.md")
        flowchart_img = os.path.join(folder_path, "flowchart.png")
        screenshot_img = os.path.join(folder_path, "output_screenshot.png")
        py_script_path = os.path.join(folder_path, m["py_file"])

        # Chapter Header
        story.append(Paragraph(f"CASE STUDY {m['id']}: {m['title'].upper()}", h1_style))
        story.append(Paragraph(f"Faculty Prescribed Problem #{m['prob_num']} | Concepts: {m['concepts']}", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=12))

        # Read documentation.md sections
        if os.path.exists(doc_path):
            with open(doc_path, "r", encoding="utf-8") as f:
                doc_text = f.read()

            # Parse markdown sections
            sections = doc_text.split("## ")
            for sec in sections[1:]:
                lines = sec.strip().split("\n")
                sec_header = lines[0].strip()
                sec_body = "\n".join(lines[1:]).strip()

                if "Problem Statement" in sec_header:
                    story.append(Paragraph("1. Problem Statement", h2_style))
                    story.append(Paragraph(sec_body, body_style))
                elif "Objectives" in sec_header:
                    story.append(Paragraph("2. Objectives", h2_style))
                    for line in lines[1:]:
                        if line.strip().startswith("-"):
                            story.append(Paragraph(f"• {line.strip()[1:].strip()}", body_style))
                elif "Assumptions" in sec_header:
                    story.append(Paragraph("3. Assumptions", h2_style))
                    for line in lines[1:]:
                        if line.strip():
                            story.append(Paragraph(line.strip(), body_style))
                elif "Algorithm" in sec_header:
                    story.append(Paragraph("4. Step-by-Step Algorithm", h2_style))
                    algo_lines = [l for l in lines[1:] if not l.strip().startswith("```")]
                    story.append(Paragraph("<br/>".join(algo_lines), code_style))
                elif "Pseudocode" in sec_header:
                    story.append(Paragraph("6. Textbook Pseudocode", h2_style))
                    pseudo_lines = [l for l in lines[1:] if not l.strip().startswith("```")]
                    story.append(Paragraph("<br/>".join(pseudo_lines[:30]), code_style))
                elif "Conclusion" in sec_header:
                    story.append(Paragraph("10. Conclusion & Analytical Insights", h2_style))
                    story.append(Paragraph(sec_body, body_style))

        # Embed Flowchart Diagram
        if os.path.exists(flowchart_img):
            story.append(Paragraph("5. Architectural Flowchart Diagram", h2_style))
            try:
                story.append(Image(flowchart_img, width=420, height=260))
            except Exception as e:
                story.append(Paragraph(f"[Flowchart preview available at {flowchart_img}]", body_style))
            story.append(Spacer(1, 10))

        # Embed Python Source Code Excerpt
        if os.path.exists(py_script_path):
            story.append(Paragraph(f"7. Python Source Code Implementation ({m['py_file']})", h2_style))
            with open(py_script_path, "r", encoding="utf-8") as pf:
                code_text = pf.read()
            # Truncate to first 40 lines in PDF with note to see .py file
            code_lines = code_text.split("\n")
            truncated_code = "\n".join(code_lines[:45])
            if len(code_lines) > 45:
                truncated_code += f"\n... [Complete {len(code_lines)} lines available in {m['py_file']}]"
            # escape html tags
            clean_code = truncated_code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>").replace(" ", "&nbsp;")
            story.append(Paragraph(clean_code, code_style))

        # Embed Terminal Execution Screenshot
        if os.path.exists(screenshot_img):
            story.append(Paragraph("8 & 9. Test Verification & Terminal Execution Output", h2_style))
            try:
                story.append(Image(screenshot_img, width=440, height=230))
            except Exception as e:
                story.append(Paragraph(f"[Output screenshot preview available at {screenshot_img}]", body_style))

        story.append(PageBreak())

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Consolidated PDF successfully generated at: {PDF_PATH}")

if __name__ == "__main__":
    build_pdf()
