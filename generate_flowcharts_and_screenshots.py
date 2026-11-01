"""Make simple flowchart and output images for the case studies."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CASE_STUDIES = [
    ("Case_Study_01_University_Scholarship_Allocation", "Case Study 01: Scholarship Allocation"),
    ("Case_Study_02_Progressive_Electricity_Billing", "Case Study 02: Electricity Billing"),
    ("Case_Study_03_Employee_Payroll_Deductions", "Case Study 03: Employee Payroll"),
    ("Case_Study_04_Advanced_Numeric_Pattern_Generator", "Case Study 04: Numeric Pattern Generator"),
    ("Case_Study_05_Student_Email_Identifier_Validation", "Case Study 05: Email & ID Validation"),
    ("Case_Study_06_Student_Marks_Matrix_Analysis", "Case Study 06: Marks Matrix Analysis"),
    ("Case_Study_07_Inventory_Matrix_Reconciliation", "Case Study 07: Inventory Matrix Reconciliation"),
    ("Case_Study_08_Tuple_Shift_Conflict_Detection", "Case Study 08: Shift Conflict Detection"),
    ("Case_Study_09_Campus_Festival_Financial_Audit", "Case Study 09: Campus Festival Financial Audit"),
    ("Case_Study_10_Smart_Campus_Simulation", "Case Study 10: Smart Campus Simulation"),
]

FLOWCHART_STEPS = {
    "Case_Study_01_University_Scholarship_Allocation": [
        ("Start", "OVAL"),
        ("Input Applicants Tuples: (ID, Name, Marks, Att, Inc, Age) & Quota", "RECT"),
        ("Iterate Applicants: Check Subject >= 50, Agg >= 75%, Att >= 75%, Inc <= 2.5L", "DIAMOND"),
        ("Separate into eligible_list and disqualified_list (with reasons)", "RECT"),
        ("Sort eligible_list: Bubble Sort (Agg desc -> Att desc -> Inc asc -> Age asc)", "RECT"),
        ("Slice by Quota: Top K -> selected_list, Remainder -> waitlist", "RECT"),
        ("Render Formatted Scholarship & Audit Reports", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_02_Progressive_Electricity_Billing": [
        ("Start", "OVAL"),
        ("Input Monthly Consumption Units & Prompt Pay Flags", "RECT"),
        ("Loop Slabs: 0-100 @ 1.5, 101-200 @ 3.0, 201-400 @ 4.5, >400 @ 6.0", "RECT"),
        ("Compute Energy Charge + Fixed Charge (100.0)", "RECT"),
        ("Is Energy Charge > 1500? Add 10% Surcharge", "DIAMOND"),
        ("Is Paid on Time? Apply 5% Early Rebate", "DIAMOND"),
        ("Multi-Month Check: Is Change in Units >= 25%?", "DIAMOND"),
        ("Flag Consumption Spikes and Print Multi-Month Statements", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_03_Employee_Payroll_Deductions": [
        ("Start", "OVAL"),
        ("Input Employee Tuples: (ID, Name, Basic, OT Hours, Rating)", "RECT"),
        ("Calculate Allowances: DA (15%), HRA (20%), Special Allw (10%)", "RECT"),
        ("Calculate Overtime: OT Hours * (Basic / 160) * 1.5x Multiplier", "RECT"),
        ("Determine Performance Incentive (Tier 5: 12k, 4: 8k, 3: 4k, <=2: 0)", "RECT"),
        ("Compute Gross Salary = Basic + Allowances + OT + Incentives", "RECT"),
        ("Calculate Progressive Tax across brackets (0%, 5%, 10%, 20%)", "RECT"),
        ("Statutory Deductions: PF (12%), Prof Tax (200), Health Ins (1000)", "RECT"),
        ("Compute Net Salary = Gross - Total Deductions & Print Payslip", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_04_Advanced_Numeric_Pattern_Generator": [
        ("Start", "OVAL"),
        ("Input Pattern Dimension N", "RECT"),
        ("Validate: Is Integer, 3 <= N <= 19, and Odd Parity?", "DIAMOND"),
        ("Calculate Mid Row = N // 2", "RECT"),
        ("Render Hollow Diamond: Row dist = abs(mid - i), Outer/Inner spaces", "RECT"),
        ("Render Centered Palindromic Pyramid: 1 -> Level -> 1", "RECT"),
        ("Display Formatted Aligned Numeric Patterns", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_05_Student_Email_Identifier_Validation": [
        ("Start", "OVAL"),
        ("Input Student Email & Registration ID Strings", "RECT"),
        ("Email Check: Exactly one '@', Domain == 'student.rvrnriit.edu.in'", "DIAMOND"),
        ("Local Check: Exactly one '.', 10-char Alnum Roll, Alpha Name", "DIAMOND"),
        ("Reg ID Check: Split by '-', Tokens == 4, Year in 20-30, Valid Branch/Sec", "DIAMOND"),
        ("Aggregate Errors: APPROVED if both valid, else REJECTED", "RECT"),
        ("Print Credential Verification Table & Itemized Defect Log", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_06_Student_Marks_Matrix_Analysis": [
        ("Start", "OVAL"),
        ("Input Students, Subjects, and 2D Marks Matrix (M x N)", "RECT"),
        ("Row-wise Traversal: Student Totals, Averages, Grades, Pass/Fail", "RECT"),
        ("Track Overall Class Top Performer", "RECT"),
        ("Column-wise Traversal: Subject Means, Max, Min, and Pass %", "RECT"),
        ("Is Subject Mean < 65% or Pass Rate < 70%?", "DIAMOND"),
        ("Flag Low-Performing Subjects for Remedial Review", "RECT"),
        ("Print Formatted 2D Matrix Grid and Curriculum Findings", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_07_Inventory_Matrix_Reconciliation": [
        ("Start", "OVAL"),
        ("Input Actual Stock Matrix and Target Threshold Matrix", "RECT"),
        ("Compute Variance Matrix: Diff[i][j] = Actual[i][j] - Target[i][j]", "RECT"),
        ("For each product: Segregate Surplus (+ve) and Deficit (-ve) Nodes", "RECT"),
        ("Greedy Rebalance: Transfer = min(Surplus, Deficit) from Source to Dest", "RECT"),
        ("Are Deficits still remaining after internal transfers?", "DIAMOND"),
        ("Log Unmet Shortages for External Procurement", "RECT"),
        ("Print Inventory Matrices, Transfer Orders, and Procurement Alerts", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_08_Tuple_Shift_Conflict_Detection": [
        ("Start", "OVAL"),
        ("Input Roster of Shift Tuples: (ID, EmpID, Day, Start, End, Dept)", "RECT"),
        ("Pair-wise Iteration: Compare Shifts (i, j) for Same Emp & Day", "RECT"),
        ("Convert 'HH:MM' 24-hr Time Strings to Minutes from Midnight", "RECT"),
        ("Check Collision: max(start1, start2) < min(end1, end2)?", "DIAMOND"),
        ("Record Direct Temporal Overlap and Duration", "RECT"),
        ("Check Rest Gap: Is gap between consecutive shifts < 480 mins (8 hrs)?", "DIAMOND"),
        ("Record Mandatory Rest Period Warning", "RECT"),
        ("Print Roster Table, Collision Reports, and Rest Audit Log", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_09_Campus_Festival_Financial_Audit": [
        ("Start", "OVAL"),
        ("Input Registrations, Corporate Sponsorships, and Expense Ledgers", "RECT"),
        ("Registration Audit: Check (StudentID, EventCode) Uniqueness", "DIAMOND"),
        ("Flag Duplicates, Void & Refund; Sum Realized Registration Fees", "RECT"),
        ("Sponsorship Audit: Sum Received Funds, Flag Pledge Shortfalls", "RECT"),
        ("Expense Ledger: Compute Budget - Actual Variance per Item", "RECT"),
        ("Reconciliation: Net Balance = (Reg Fees + Sponsorships) - Expenses", "RECT"),
        ("Print Financial Balance Sheet & Audit Verdict (Surplus / Deficit)", "RECT"),
        ("End", "OVAL"),
    ],
    "Case_Study_10_Smart_Campus_Simulation": [
        ("Start", "OVAL"),
        ("Initialize Registry, Attendance, Marks, Events, and Lab Seat Grid", "RECT"),
        ("Display Main Menu (1: Registry, 2: Att, 3: Marks, 4: Events, 5: Lab, 6: Exec)", "RECT"),
        ("Option 1-3: Display Roster, Flag Attendance < 75%, Compute Marks", "RECT"),
        ("Option 4: Register Event with Duplicate Check & Capacity Check", "DIAMOND"),
        ("Option 5: 2D Computing Lab Workspace Allocation & Seat Conflict Guard", "DIAMOND"),
        ("Option 6: Show Campus Summary", "RECT"),
        ("Option 7: Exit Application", "OVAL"),
    ]
}

def create_flowchart_image(steps, title, output_path):
    width = 900
    step_height = 80
    gap = 40
    padding_top = 100
    total_height = padding_top + len(steps) * (step_height + gap) + 40

    img = Image.new("RGB", (width, total_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 22)
        font_box = ImageFont.truetype("arial.ttf", 14)
        font_sub = ImageFont.truetype("arial.ttf", 13)
    except IOError:
        font_title = ImageFont.load_default()
        font_box = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Draw Title Header
    draw.rectangle([(0, 0), (width, 70)], fill=(30, 58, 138))  # Dark Blue
    draw.text((width // 2, 35), title.upper(), fill=(255, 255, 255), anchor="mm", font=font_title)

    center_x = width // 2
    cur_y = padding_top

    for idx, (text, shape) in enumerate(steps):
        box_w = 680
        box_h = step_height
        x0 = center_x - box_w // 2
        y0 = cur_y
        x1 = center_x + box_w // 2
        y1 = cur_y + box_h

        # Draw shape
        if shape == "OVAL":
            draw.rounded_rectangle([(x0 + 140, y0 + 10), (x1 - 140, y1 - 10)], radius=30, fill=(219, 234, 254), outline=(30, 64, 175), width=2)
            draw.text((center_x, (y0 + y1) // 2), text, fill=(30, 64, 175), anchor="mm", font=font_box)
        elif shape == "DIAMOND":
            mid_y = (y0 + y1) // 2
            diamond_pts = [(center_x, y0), (x1 - 20, mid_y), (center_x, y1), (x0 + 20, mid_y)]
            draw.polygon(diamond_pts, fill=(254, 243, 199), outline=(180, 83, 9), width=2)
            draw.text((center_x, mid_y), text, fill=(180, 83, 9), anchor="mm", font=font_sub)
        else:  # RECT
            draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=10, fill=(243, 244, 246), outline=(75, 85, 99), width=2)
            draw.text((center_x, (y0 + y1) // 2), text, fill=(17, 24, 39), anchor="mm", font=font_sub)

        # Draw downward connecting arrow to next node
        if idx < len(steps) - 1:
            arrow_start = (center_x, y1)
            arrow_end = (center_x, y1 + gap)
            draw.line([arrow_start, arrow_end], fill=(107, 114, 128), width=3)
            # Arrow head
            draw.polygon([
                (center_x, arrow_end[1]),
                (center_x - 6, arrow_end[1] - 8),
                (center_x + 6, arrow_end[1] - 8)
            ], fill=(107, 114, 128))

        cur_y += box_h + gap

    img.save(output_path, "PNG", quality=95)


def create_terminal_screenshot(output_text, title, output_path):
    width = 1000
    line_height = 20
    lines = output_text.strip().split("\n")
    # Cap displayed lines to 45 lines if too long to maintain readable resolution
    if len(lines) > 45:
        lines = lines[:45] + ["... [Output truncated for preview - full log available in output.txt] ..."]

    total_height = 80 + len(lines) * line_height + 40

    img = Image.new("RGB", (width, total_height), color=(30, 30, 30))  # Dark IDE background
    draw = ImageDraw.Draw(img)

    try:
        font_term = ImageFont.truetype("consola.ttf", 13)
        font_bar = ImageFont.truetype("arialbd.ttf", 13)
    except IOError:
        font_term = ImageFont.load_default()
        font_bar = ImageFont.load_default()

    # Terminal Window Header Bar
    draw.rectangle([(0, 0), (width, 42)], fill=(45, 45, 45))
    # macOS/Linux terminal buttons (Red, Yellow, Green)
    draw.ellipse([(18, 14), (30, 26)], fill=(239, 68, 68))
    draw.ellipse([(38, 14), (50, 26)], fill=(245, 158, 11))
    draw.ellipse([(58, 14), (70, 26)], fill=(16, 185, 129))

    # Window title centered
    draw.text((width // 2, 20), f"bash - Python 3.14 - {title}", fill=(209, 213, 219), anchor="mm", font=font_bar)

    # Terminal prompt line
    y = 60
    draw.text((25, y), "$ python solution_runner.py", fill=(74, 222, 128), font=font_term)
    y += line_height + 5

    # Render terminal text
    for line in lines:
        color = (229, 231, 235)  # Light gray
        if "ALERT" in line or "FAILED" in line or "SHORTAGE" in line or "REJECTED" in line or "OVER-BUDGET" in line:
            color = (248, 113, 113)  # Soft red
        elif "PASSED" in line or "APPROVED" in line or "SUCCESS" in line or "SURPLUS" in line or "PASS" in line:
            color = (134, 239, 172)  # Soft green
        elif "SECTION" in line or "PART" in line or "MODULE" in line or "DR. RVR" in line or "=====" in line:
            color = (147, 197, 253)  # Soft blue

        draw.text((25, y), line, fill=color, font=font_term)
        y += line_height

    img.save(output_path, "PNG", quality=95)


def main():
    print("Generating flowchart and terminal screenshot images for all 10 case studies...")
    for folder, title in CASE_STUDIES:
        folder_path = os.path.join(ROOT_DIR, folder)
        flowchart_path = os.path.join(folder_path, "flowchart.png")
        screenshot_path = os.path.join(folder_path, "output_screenshot.png")
        output_txt_path = os.path.join(folder_path, "output.txt")

        # 1. Flowchart
        if folder in FLOWCHART_STEPS:
            create_flowchart_image(FLOWCHART_STEPS[folder], title, flowchart_path)

        # 2. Screenshot from output.txt
        if os.path.exists(output_txt_path):
            try:
                with open(output_txt_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, Exception):
                with open(output_txt_path, "r", encoding="utf-16", errors="replace") as f:
                    content = f.read()
            create_terminal_screenshot(content, title, screenshot_path)

        print(f"  [DONE] Generated images for {folder}")

    print("All flowcharts and screenshots generated successfully!")

if __name__ == "__main__":
    main()
