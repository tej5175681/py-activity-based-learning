"""
Test Suite for Case Study 05: Student Email and Registration Identifier Validation
"""
from problem_30_email_identifier_validation import (
    validate_student_email,
    validate_registration_identifier,
    audit_student_credentials
)

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 05")
    print("=" * 70)

    # Test Case 1: Perfectly Formatted Email and Registration ID
    email_ok = "26B91A0501.manikanta@student.rvrnriit.edu.in"
    val, info, errs = validate_student_email(email_ok)
    assert val is True, f"Expected True, got {val} with errors: {errs}"
    assert info == ("26B91A0501", "Manikanta", "student.rvrnriit.edu.in")

    reg_ok = "26-CSE-A-0501"
    val_r, info_r, errs_r = validate_registration_identifier(reg_ok)
    assert val_r is True and info_r == ("26", "CSE", "A", "0501")
    print("[PASS] Test Case 1: Valid email and registration ID verified.")

    # Test Case 2: Email Malformed Separator (Double Dots in Local Part)
    email_double_dot = "26B91A0501..kumar@student.rvrnriit.edu.in"
    val, info, errs = validate_student_email(email_double_dot)
    assert val is False
    assert any("Malformed separators" in e for e in errs)
    print("[PASS] Test Case 2: Consecutive dot malformed separator caught.")

    # Test Case 3: Registration ID Invalid Branch & Non-digit sequence
    reg_bad = "26-AERONAUTICS-A-99X"
    val_r, _, errs_r = validate_registration_identifier(reg_bad)
    assert val_r is False
    assert any("Invalid branch" in e for e in errs_r)
    assert any("Invalid roll sequence" in e for e in errs_r)
    print("[PASS] Test Case 3: Invalid branch and non-numeric roll sequence caught.")

    # Test Case 4: Non-institutional Domain Rejection
    email_gmail = "26B91A0501.kumar@gmail.com"
    val, _, errs = validate_student_email(email_gmail)
    assert val is False
    assert any("Invalid domain" in e for e in errs)
    print("[PASS] Test Case 4: Non-institutional public domain rejected.")

    # Test Case 5: Missing Separators
    email_no_at = "26B91A0501.kumar.student.rvrnriit.edu.in"
    val, _, errs = validate_student_email(email_no_at)
    assert val is False
    assert any("Missing '@'" in e for e in errs)
    print("[PASS] Test Case 5: Missing @ symbol detected.")

    print("=" * 70)
    print("ALL 5 UNIT TESTS PASSED FOR CASE STUDY 05!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
