"""
Test Suite for Case Study 08: Tuple-Based Shift Conflict Detection
"""
from problem_48_shift_conflict_detection import parse_time_to_minutes, detect_shift_conflicts

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 08")
    print("=" * 70)

    # Test Case 1: Time Parsing Accuracy
    t1 = parse_time_to_minutes("00:00")
    t2 = parse_time_to_minutes("08:30")
    t3 = parse_time_to_minutes("23:59")
    assert t1 == 0 and t2 == 510 and t3 == 1439
    print("[PASS] Test Case 1: 24-hour time to minutes conversion verified.")

    # Test Case 2: Exact Direct Overlap Detection
    # Same employee, same day: 09:00 - 13:00 vs 12:00 - 16:00 (Overlap: 12:00 - 13:00 = 60 mins)
    shifts1 = [
        ("S1", "E1", "John", "Monday", "09:00", "13:00", "Dept1"),
        ("S2", "E1", "John", "Monday", "12:00", "16:00", "Dept2"),
    ]
    overlaps, rests = detect_shift_conflicts(shifts1, 8)
    assert len(overlaps) == 1
    assert overlaps[0][11] == 60, f"Expected 60 minutes overlap, got {overlaps[0][11]}"
    print("[PASS] Test Case 2: Direct shift overlap and duration verified.")

    # Test Case 3: Rest Interval Shortage (< 8 hours)
    # Shift 1 ends at 12:00 (720 min), Shift 2 starts at 15:00 (900 min).
    # Gap = 180 min (3 hours) < 480 min.
    shifts2 = [
        ("S1", "E1", "John", "Monday", "08:00", "12:00", "Dept1"),
        ("S2", "E1", "John", "Monday", "15:00", "19:00", "Dept1"),
    ]
    overlaps, rests = detect_shift_conflicts(shifts2, 8)
    assert len(overlaps) == 0
    assert len(rests) == 1
    assert rests[0][5] == 180, f"Expected 180 min gap, got {rests[0][5]}"
    print("[PASS] Test Case 3: Insufficient rest period detection verified.")

    # Test Case 4: Different Days and Different Employees (No Conflict)
    shifts3 = [
        ("S1", "E1", "John", "Monday", "08:00", "14:00", "Dept1"),
        ("S2", "E2", "Jane", "Monday", "08:00", "14:00", "Dept1"), # Different employee
        ("S3", "E1", "John", "Tuesday", "08:00", "14:00", "Dept1"), # Different day
    ]
    overlaps, rests = detect_shift_conflicts(shifts3, 8)
    assert len(overlaps) == 0 and len(rests) == 0
    print("[PASS] Test Case 4: Shift isolation across employees and calendar days verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 08!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
