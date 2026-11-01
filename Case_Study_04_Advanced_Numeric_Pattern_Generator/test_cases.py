"""
Test Suite for Case Study 04: Advanced Numeric Pattern Generator
"""
from problem_27_pattern_generator import (
    validate_dimension,
    generate_hollow_numeric_diamond,
    generate_palindromic_number_pyramid,
)

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 04")
    print("=" * 70)

    # Test Case 1: Input Validation - Valid Odd Dimensions
    val, n, msg = validate_dimension("7")
    assert val is True and n == 7, "Dimension 7 should be valid"
    print("[PASS] Test Case 1: Valid odd dimension validated successfully.")

    # Test Case 2: Input Validation - Even Number Rejection
    val, n, msg = validate_dimension(8)
    assert val is False and "even" in msg, f"Expected even error, got: {msg}"
    print("[PASS] Test Case 2: Even dimension rejected correctly.")

    # Test Case 3: Input Validation - Out of bounds and non-numeric
    val1, _, _ = validate_dimension(1)
    val2, _, _ = validate_dimension(25)
    val3, _, _ = validate_dimension("abc")
    assert val1 is False and val2 is False and val3 is False
    print("[PASS] Test Case 3: Out of bounds and non-numeric rejections verified.")

    # Test Case 4: Hollow diamond line count and vertex symmetry
    lines = generate_hollow_numeric_diamond(5)
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    assert lines[0].strip() == "1", "Top tip should be 1"
    assert lines[4].strip() == "1", "Bottom tip should be 1"
    assert lines[2].startswith("3"), "Middle row starts with 3"
    print("[PASS] Test Case 4: Hollow diamond geometric symmetry verified.")

    # Test Case 5: Palindromic pyramid structure
    p_lines = generate_palindromic_number_pyramid(4)
    assert len(p_lines) == 4
    assert p_lines[3].strip() == "1 2 3 4 3 2 1"
    print("[PASS] Test Case 5: Palindromic number pyramid row content verified.")

    print("=" * 70)
    print("ALL 5 UNIT TESTS PASSED FOR CASE STUDY 04!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
