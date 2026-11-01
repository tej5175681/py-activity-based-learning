"""Run all programs and their simple test files."""
import subprocess
import sys
import os

CASE_STUDIES = [
    ("Case Study 01: University Scholarship Allocation", "Case_Study_01_University_Scholarship_Allocation", "problem_01_scholarship_allocation.py", "test_cases.py"),
    ("Case Study 02: Progressive Electricity Billing", "Case_Study_02_Progressive_Electricity_Billing", "problem_02_electricity_billing.py", "test_cases.py"),
    ("Case Study 03: Employee Payroll & Deductions", "Case_Study_03_Employee_Payroll_Deductions", "problem_04_employee_payroll.py", "test_cases.py"),
    ("Case Study 04: Advanced Numeric Pattern Generator", "Case_Study_04_Advanced_Numeric_Pattern_Generator", "problem_27_pattern_generator.py", "test_cases.py"),
    ("Case Study 05: Student Email & ID Validation", "Case_Study_05_Student_Email_Identifier_Validation", "problem_30_email_identifier_validation.py", "test_cases.py"),
    ("Case Study 06: Student Marks Matrix Analysis", "Case_Study_06_Student_Marks_Matrix_Analysis", "problem_42_marks_matrix_analysis.py", "test_cases.py"),
    ("Case Study 07: Inventory Matrix Reconciliation", "Case_Study_07_Inventory_Matrix_Reconciliation", "problem_46_inventory_reconciliation.py", "test_cases.py"),
    ("Case Study 08: Tuple Shift Conflict Detection", "Case_Study_08_Tuple_Shift_Conflict_Detection", "problem_48_shift_conflict_detection.py", "test_cases.py"),
    ("Case Study 09: Campus Festival Financial Audit", "Case_Study_09_Campus_Festival_Financial_Audit", "problem_74_festival_audit.py", "test_cases.py"),
    ("Case Study 10: Smart Campus Management Simulation", "Case_Study_10_Smart_Campus_Simulation", "problem_100_smart_campus_simulation.py", "test_cases.py"),
]

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 70)
    print("PYTHON ACTIVITY BASED LEARNING - RUNNING ALL PROGRAMS")
    print("=" * 70)

    passed_count = 0
    total_count = len(CASE_STUDIES)

    for idx, (title, folder, script, test_file) in enumerate(CASE_STUDIES, 1):
        print(f"\n[{idx}/{total_count}] {title}")
        case_dir = os.path.join(root_dir, folder)

        # Run the main program first.
        res_script = subprocess.run(
            [sys.executable, script],
            cwd=case_dir,
            capture_output=True,
            text=True
        )
        if res_script.returncode != 0:
            print(f"  Main program failed (return code {res_script.returncode})")
            print(res_script.stderr)
            continue

        # Then run the tests in the same folder.
        res_test = subprocess.run(
            [sys.executable, test_file],
            cwd=case_dir,
            capture_output=True,
            text=True
        )
        if res_test.returncode != 0:
            print(f"  Tests failed (return code {res_test.returncode})")
            print(res_test.stderr)
            continue

        print("  Main program and tests passed.")
        passed_count += 1

    print("\n" + "=" * 70)
    print(f"Result: {passed_count}/{total_count} case studies passed")
    print("=" * 70)

if __name__ == "__main__":
    main()
