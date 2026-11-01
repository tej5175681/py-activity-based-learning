"""
Case Study 08: Tuple-Based Employee Shift Conflict Detection Engine
===================================================================
Syllabus Concepts Used:
- Tuples and Tuple Packing/Unpacking
- Tuple Operations (indexing, concatenation, comparison)
- String Slicing and String Methods (split, strip)
- Variables, Data Types (str, int, bool, list, tuple)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops for Pair-Wise Shift Comparisons
- Formatted Tabular Reports

Description:
Audits institutional duty rotas to detect shift schedule conflicts:
1. Converts 24-hour time strings ("HH:MM") to total minutes from midnight.
2. Identifies direct temporal overlaps (where an employee is scheduled simultaneously).
3. Identifies insufficient rest intervals (< 8 hours / 480 minutes between duties).
4. Identifies cross-departmental double bookings.
"""

def parse_time_to_minutes(time_str):
    """
    Converts 'HH:MM' 24-hour string format into minutes since midnight.
    e.g., '08:30' -> 8 * 60 + 30 = 510 minutes.
    """
    clean_str = time_str.strip()
    parts = clean_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours * 60 + minutes


def format_minutes_to_time(minutes):
    """
    Converts minutes back to 'HH:MM' string format.
    """
    hrs = minutes // 60
    mins = minutes % 60
    return f"{hrs:02d}:{mins:02d}"


def detect_shift_conflicts(shifts, min_rest_hours=8):
    """
    shifts: List of tuples
    (shift_id, emp_id, emp_name, day_of_week, start_time, end_time, department)
    """
    direct_overlaps = []
    rest_violations = []
    min_rest_minutes = min_rest_hours * 60

    num_shifts = len(shifts)

    # Pair-wise comparison using nested loops
    for i in range(num_shifts):
        for j in range(i + 1, num_shifts):
            # Tuple unpacking
            s1_id, e1_id, name1, day1, start1_str, end1_str, dept1 = shifts[i]
            s2_id, e2_id, name2, day2, start2_str, end2_str, dept2 = shifts[j]

            # Check only if it belongs to the same employee and the same day
            if e1_id == e2_id and day1.lower() == day2.lower():
                st1 = parse_time_to_minutes(start1_str)
                et1 = parse_time_to_minutes(end1_str)
                st2 = parse_time_to_minutes(start2_str)
                et2 = parse_time_to_minutes(end2_str)

                # Check 1: Direct Temporal Overlap
                # Overlap exists if max(start1, start2) < min(end1, end2)
                overlap_start = max(st1, st2)
                overlap_end = min(et1, et2)

                if overlap_start < overlap_end:
                    overlap_duration = overlap_end - overlap_start
                    conflict_record = (
                        e1_id, name1, day1,
                        s1_id, start1_str, end1_str, dept1,
                        s2_id, start2_str, end2_str, dept2,
                        overlap_duration
                    )
                    direct_overlaps.append(conflict_record)
                else:
                    # Check 2: Rest Interval Violation (when shifts do not overlap)
                    # Determine chronologically earlier and later shifts
                    if et1 <= st2:
                        gap = st2 - et1
                        earlier_s, later_s = s1_id, s2_id
                    else:
                        gap = st1 - et2
                        earlier_s, later_s = s2_id, s1_id

                    if 0 <= gap < min_rest_minutes:
                        rest_record = (
                            e1_id, name1, day1,
                            earlier_s, later_s, gap, min_rest_minutes
                        )
                        rest_violations.append(rest_record)

    return direct_overlaps, rest_violations


def print_conflict_report(shifts, overlaps, rest_violations):
    print("=" * 105)
    print("                    DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("             TUPLE-BASED EMPLOYEE SHIFT CONFLICT AUDIT REPORT")
    print("=" * 105)

    print("\n[SECTION 1: SCHEDULED ROSTER OVERVIEW]")
    print(f"{'Shift ID':<10}{'Emp ID':<10}{'Employee Name':<18}{'Day':<12}{'Start':<8}{'End':<8}{'Department':<16}")
    print("-" * 105)
    for s in shifts:
        sid, eid, name, day, st, et, dept = s
        print(f"{sid:<10}{eid:<10}{name:<18}{day:<12}{st:<8}{et:<8}{dept:<16}")

    print("-" * 105)
    print("\n[SECTION 2: CRITICAL DIRECT OVERLAP CONFLICTS (SIMULTANEOUS BOOKING)]")
    print(f"{'Emp ID':<10}{'Employee':<18}{'Day':<10}{'Shift 1':<24}{'Shift 2':<24}{'Overlap Duration'}")
    print("-" * 105)
    if len(overlaps) == 0:
        print(">> No direct overlapping assignments detected. All shifts are temporally isolated.")
    else:
        for ov in overlaps:
            eid, name, day, s1, st1, et1, d1, s2, st2, et2, d2, dur = ov
            s1_info = f"{s1} ({st1}-{et1})"
            s2_info = f"{s2} ({st2}-{et2})"
            print(f"{eid:<10}{name:<18}{day:<10}{s1_info:<24}{s2_info:<24}{dur} minutes ({dur/60:.1f} hrs)")

    print("-" * 105)
    print("\n[SECTION 3: INSUFFICIENT REST DURATION WARNINGS (< 8 HOURS REST)]")
    print(f"{'Emp ID':<10}{'Employee':<18}{'Day':<10}{'Prior Shift':<14}{'Next Shift':<14}{'Rest Gap':<16}{'Required Rest'}")
    print("-" * 105)
    if len(rest_violations) == 0:
        print(">> All consecutive shifts comply with the mandatory 8-hour rest policy.")
    else:
        for rv in rest_violations:
            eid, name, day, s_prev, s_next, gap, req = rv
            print(f"{eid:<10}{name:<18}{day:<10}{s_prev:<14}{s_next:<14}{gap} min ({gap/60:.1f} hrs)   {req} min (8.0 hrs)")

    print("=" * 105)


if __name__ == "__main__":
    shift_roster = [
        ("SH-101", "EMP-01", "K. V. Rao",      "Monday", "08:00", "14:00", "CSE Lab-1"),
        ("SH-102", "EMP-01", "K. V. Rao",      "Monday", "12:00", "18:00", "ECE Workshop"), # Overlaps SH-101 (12:00-14:00)!
        ("SH-103", "EMP-02", "P. Anitha",      "Monday", "09:00", "13:00", "Server Room"),
        ("SH-104", "EMP-02", "P. Anitha",      "Monday", "15:00", "21:00", "Network Lab"), # 2h gap (< 8h rest violation)
        ("SH-105", "EMP-03", "M. Rajesh",      "Tuesday", "08:00", "16:00", "Library"),
        ("SH-106", "EMP-01", "K. V. Rao",      "Tuesday", "09:00", "17:00", "CSE Lab-2"),
    ]

    direct, rest = detect_shift_conflicts(shift_roster, min_rest_hours=8)
    print_conflict_report(shift_roster, direct, rest)
