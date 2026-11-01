"""
Test Suite for Case Study 10: Smart Campus Management Simulation
"""
from problem_100_smart_campus_simulation import (
    initialize_campus_data,
    audit_attendance,
    register_for_event,
    allocate_lab_seat
)

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 10")
    print("=" * 70)

    students, attendance, subjects, marks, events, lab_seats = initialize_campus_data()

    # Test Case 1: Attendance Shortage Audit Threshold (< 75%)
    # In initial data: Divya (68%) and Eshwar (72%) are below 75%
    shortage_list = audit_attendance(students, attendance, threshold=75.0)
    assert len(shortage_list) == 2, f"Expected 2 shortages, got {len(shortage_list)}"
    assert shortage_list[0][0] == "26B91A0504"
    assert shortage_list[1][0] == "26B91A0505"
    print("[PASS] Test Case 1: Attendance shortage detection (<75%) verified.")

    # Test Case 2: Event Registration Capacity and Duplicate Guard
    # EV-ROBO initial has 1 student ("26B91A0503"), capacity = 2.
    # Registering new student "26B91A0504" should succeed.
    ok1, msg1 = register_for_event(events, "EV-ROBO", "26B91A0504")
    assert ok1 is True, f"Registration failed: {msg1}"

    # Attempting duplicate registration of "26B91A0504" should fail.
    ok2, msg2 = register_for_event(events, "EV-ROBO", "26B91A0504")
    assert ok2 is False and "Duplicate" in msg2, f"Expected duplicate error, got: {msg2}"

    # Attempting overflow registration should fail (capacity 2 full)
    ok3, msg3 = register_for_event(events, "EV-ROBO", "26B91A0505")
    assert ok3 is False and "Capacity Exceeded" in msg3, f"Expected capacity error, got: {msg3}"
    print("[PASS] Test Case 2: Event capacity and duplicate registration guards verified.")

    # Test Case 3: Lab Seat Allocation Valid and Collision Check
    # (Row 1, Col 0) is empty (".") initially
    ok_seat1, msg_s1 = allocate_lab_seat(lab_seats, 1, 0, "26B91A0505")
    assert ok_seat1 is True
    assert lab_seats[1][0] == "26B91A0505"

    # Attempting to assign already seated student to another seat (Row 2, Col 0) should fail
    ok_seat2, msg_s2 = allocate_lab_seat(lab_seats, 2, 0, "26B91A0505")
    assert ok_seat2 is False and "already seated" in msg_s2

    # Attempting to overwrite an occupied seat should fail
    ok_seat3, msg_s3 = allocate_lab_seat(lab_seats, 1, 0, "26B91A0501")
    assert ok_seat3 is False and "already assigned" in msg_s3
    print("[PASS] Test Case 3: Lab seat allocation and conflict prevention verified.")

    # Test Case 4: Out of bounds seat coordinates
    ok_oob, _ = allocate_lab_seat(lab_seats, 10, 10, "TEST")
    assert ok_oob is False
    print("[PASS] Test Case 4: Coordinate boundary checks verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 10!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
