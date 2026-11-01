"""
Test Suite for Case Study 01: University Scholarship Allocation
"""
import sys
from problem_01_scholarship_allocation import evaluate_and_rank_scholarships

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 01")
    print("=" * 70)

    # Test Case 1: Standard Eligibility and Tie Resolution
    # Divya Sri (18) and Aarav (19) have identical agg (88.75), att (91.0), income (180000).
    # Divya must rank ahead of Aarav due to younger age rule.
    data_1 = [
        ("S1", "Aarav", [85, 90, 88, 92], 91.0, 180000, 19),
        ("S2", "Divya", [85, 90, 88, 92], 91.0, 180000, 18),
    ]
    sel, wait, disq = evaluate_and_rank_scholarships(data_1, 2)
    assert len(sel) == 2, f"Expected 2 selected, got {len(sel)}"
    assert sel[0][1] == "S2", f"Expected younger candidate Divya to be Rank 1, got {sel[0][1]}"
    assert sel[1][1] == "S1", f"Expected Aarav to be Rank 2, got {sel[1][1]}"
    print("[PASS] Test Case 1: Tie-breaking by Age verified successfully.")

    # Test Case 2: Boundary condition - exact threshold marks (50.0 sub, 75.0% agg, 75.0% att, 250000 income)
    data_2 = [
        ("S_BOUNDARY", "Kavya", [75, 75, 75, 75], 75.0, 250000, 20),
    ]
    sel, wait, disq = evaluate_and_rank_scholarships(data_2, 1)
    assert len(sel) == 1, "Expected boundary candidate to be eligible"
    assert len(disq) == 0, "Expected 0 disqualified"
    print("[PASS] Test Case 2: Exact boundary thresholds verified successfully.")

    # Test Case 3: Multiple Disqualification Criteria simultaneously
    data_3 = [
        ("S_FAIL_ALL", "Raju", [40, 45, 48, 49], 60.0, 400000, 22),
    ]
    sel, wait, disq = evaluate_and_rank_scholarships(data_3, 1)
    assert len(sel) == 0, "Expected 0 selected"
    assert len(disq) == 1, "Expected 1 disqualified"
    assert len(disq[0][6]) == 4, f"Expected 4 disqualification reasons, got {len(disq[0][6])}"
    print("[PASS] Test Case 3: Multiple disqualifications detected successfully.")

    # Test Case 4: Quota overflow waitlist test
    data_4 = [
        ("S1", "Cand 1", [90, 90, 90, 90], 90.0, 100000, 19),
        ("S2", "Cand 2", [85, 85, 85, 85], 85.0, 100000, 19),
        ("S3", "Cand 3", [80, 80, 80, 80], 80.0, 100000, 19),
    ]
    sel, wait, disq = evaluate_and_rank_scholarships(data_4, 1)
    assert len(sel) == 1 and sel[0][1] == "S1", "Expected only Cand 1 to be selected"
    assert len(wait) == 2, f"Expected 2 waitlisted, got {len(wait)}"
    print("[PASS] Test Case 4: Quota capping and waitlist partitioning verified successfully.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 01!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
