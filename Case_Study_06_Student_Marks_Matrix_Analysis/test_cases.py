"""
Test Suite for Case Study 06: Student Marks Matrix Analysis
"""
from problem_42_marks_matrix_analysis import analyze_marks_matrix

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 06")
    print("=" * 70)

    studs = [("S1", "Alice"), ("S2", "Bob")]
    subs = ["Math", "Physics"]

    # Test Case 1: Standard 2x2 Matrix Aggregation
    # Alice: [90, 80] -> Total = 170, Avg = 85.0, Grade O
    # Bob:   [50, 40] -> Total = 90, Avg = 45.0, Grade C
    # Math stats: Avg = (90 + 50)/2 = 70.0, Max = 90, Min = 50, Pass = 100%
    # Physics stats: Avg = (80 + 40)/2 = 60.0, Max = 80, Min = 40, Pass = 100%
    grid1 = [[90, 80], [50, 40]]
    results, stats, top, low = analyze_marks_matrix(studs, subs, grid1)

    assert results[0][3] == 170 and results[0][4] == 85.0
    assert results[1][3] == 90 and results[1][4] == 45.0
    assert top[1] == "Alice" and top[2] == 170
    assert stats[0][1] == 70.0 and stats[1][1] == 60.0
    print("[PASS] Test Case 1: Row-wise total/average and column-wise stats verified.")

    # Test Case 2: Subject Failure and Grade Override
    # Score < 40 in one subject must result in status "FAILED" and Grade "F" even if avg is high
    grid2 = [[100, 35], [70, 70]]
    results, stats, top, low = analyze_marks_matrix(studs, subs, grid2)
    assert results[0][6] == "FAILED"
    assert "Fail" in results[0][5]
    print("[PASS] Test Case 2: Individual subject failure overriding aggregate grade verified.")

    # Test Case 3: Detection of Low-Performing Subjects
    # In grid1, Physics has average 60.0 < 65.0 threshold -> must be flagged
    assert len(low) == 1 and low[0][0] == "Physics"
    print("[PASS] Test Case 3: Low-performing subject detection verified.")

    # Test Case 4: Subject Pass Rate Metric
    # In grid2, Math has 2 passes (100%), Physics has 1 pass out of 2 (50%)
    assert stats[1][4] == 50.0
    print("[PASS] Test Case 4: Subject pass percentage metric verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 06!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
