"""
Case Study 01: University Scholarship Allocation System
=====================================================
Syllabus Concepts Used:
- Variables and Data Types (int, float, str, bool)
- Arithmetic, Relational, and Logical Operators
- Conditional Statements (if, elif, else)
- Loops (for, while, nested loops)
- Lists and Nested Lists
- Tuples, Tuple Operations, and Tuple Unpacking
- String Formatting

Description:
Evaluates scholarship applicants using multi-criteria validation:
1. Subject-wise pass constraint (each subject >= 50 marks)
2. Minimum overall aggregate marks (>= 75.0%)
3. Minimum attendance percentage (>= 75.0%)
4. Annual family income ceiling (<= INR 2,50,000)

Ranks eligible candidates using deterministic tie-breaking rules:
Priority 1: Higher Aggregate Marks
Priority 2: Higher Attendance Percentage
Priority 3: Lower Family Income
Priority 4: Younger Age
"""

def evaluate_and_rank_scholarships(applicants, total_quota):
    """
    Evaluates applicants and allocates a limited number of scholarships.
    Applicants format:
    List of tuples: (student_id, name, [m1, m2, m3, m4], attendance_pct, family_income, age)
    """
    eligible_list = []
    disqualified_list = []

    # Step 1: Filter applicants based on eligibility criteria
    for applicant in applicants:
        # Tuple unpacking
        student_id, name, marks, attendance, income, age = applicant

        # Validate subject-wise minimum marks
        all_subjects_passed = True
        marks_sum = 0
        subject_count = len(marks)
        
        for mark in marks:
            marks_sum += mark
            if mark < 50:
                all_subjects_passed = False

        aggregate_pct = marks_sum / subject_count if subject_count > 0 else 0.0

        # Disqualification reason check
        reasons = []
        if not all_subjects_passed:
            reasons.append("Failed subject-wise minimum criterion (< 50 marks)")
        if aggregate_pct < 75.0:
            reasons.append("Aggregate marks below 75.0% threshold")
        if attendance < 75.0:
            reasons.append("Attendance below 75.0% threshold")
        if income > 250000:
            reasons.append("Annual family income exceeds INR 2,50,000 ceiling")

        if len(reasons) == 0:
            # Store eligible candidate tuple: (student_id, name, aggregate_pct, attendance, income, age)
            eligible_list.append((student_id, name, aggregate_pct, attendance, income, age))
        else:
            disqualified_list.append((student_id, name, aggregate_pct, attendance, income, age, reasons))

    # Step 2: Custom Sorting Algorithm (Bubble Sort using syllabus concepts)
    # Multi-level tie-breaking:
    # Key 1: aggregate (descending)
    # Key 2: attendance (descending)
    # Key 3: income (ascending)
    # Key 4: age (ascending)
    n = len(eligible_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            cand1 = eligible_list[j]
            cand2 = eligible_list[j + 1]

            # Unpack tuples
            id1, name1, agg1, att1, inc1, age1 = cand1
            id2, name2, agg2, att2, inc2, age2 = cand2

            swap = False
            if agg1 < agg2:
                swap = True
            elif agg1 == agg2:
                if att1 < att2:
                    swap = True
                elif att1 == att2:
                    if inc1 > inc2:
                        swap = True
                    elif inc1 == inc2:
                        if age1 > age2:
                            swap = True

            if swap:
                eligible_list[j], eligible_list[j + 1] = eligible_list[j + 1], eligible_list[j]

    # Step 3: Allocation based on quota
    selected_list = []
    waitlisted_list = []
    for idx in range(len(eligible_list)):
        cand = eligible_list[idx]
        rank = idx + 1
        record = (rank,) + cand  # Tuple concatenation
        if idx < total_quota:
            selected_list.append(record)
        else:
            waitlisted_list.append(record)

    return selected_list, waitlisted_list, disqualified_list


def print_scholarship_report(selected, waitlist, disqualified, quota):
    print("=" * 86)
    print("               DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("       UNIVERSITY SCHOLARSHIP ALLOCATION & MERIT RANKING REPORT")
    print("=" * 86)
    print(f"Total Available Scholarships (Quota): {quota}")
    print(f"Total Qualified Candidates: {len(selected) + len(waitlist)}")
    print(f"Total Disqualified Applicants: {len(disqualified)}")
    print("-" * 86)

    print("\n[SECTION 1: SELECTED SCHOLARSHIP RECIPIENTS]")
    print(f"{'Rank':<5}{'ID':<12}{'Name':<18}{'Aggregate %':<14}{'Att %':<10}{'Income (INR)':<14}{'Age':<5}")
    print("-" * 86)
    if len(selected) == 0:
        print("No candidates met the scholarship selection criteria.")
    else:
        for item in selected:
            rank, sid, name, agg, att, inc, age = item
            print(f"{rank:<5}{sid:<12}{name:<18}{agg:<14.2f}{att:<10.1f}{inc:<14,}{age:<5}")

    print("\n[SECTION 2: WAITLISTED CANDIDATES (BEYOND QUOTA)]")
    print(f"{'Rank':<5}{'ID':<12}{'Name':<18}{'Aggregate %':<14}{'Att %':<10}{'Income (INR)':<14}{'Age':<5}")
    print("-" * 86)
    if len(waitlist) == 0:
        print("No waitlisted candidates.")
    else:
        for item in waitlist:
            rank, sid, name, agg, att, inc, age = item
            print(f"{rank:<5}{sid:<12}{name:<18}{agg:<14.2f}{att:<10.1f}{inc:<14,}{age:<5}")

    print("\n[SECTION 3: DISQUALIFIED APPLICANTS & AUDIT TRAIL]")
    print(f"{'ID':<12}{'Name':<18}{'Agg %':<10}{'Att %':<8}{'Income':<12}{'Primary Disqualification Reason'}")
    print("-" * 86)
    for item in disqualified:
        sid, name, agg, att, inc, age, reasons = item
        primary_reason = reasons[0]
        if len(reasons) > 1:
            primary_reason += f" (+{len(reasons)-1} more)"
        print(f"{sid:<12}{name:<18}{agg:<10.2f}{att:<8.1f}{inc:<12,}{primary_reason}")
    print("=" * 86)


if __name__ == "__main__":
    # Sample Applicant Records:
    # (student_id, name, [marks], attendance, family_income, age)
    applicants_data = [
        ("26B91A0501", "Aarav Sharma",    [85, 90, 88, 92], 91.0, 180000, 19),
        ("26B91A0502", "Bhavya Reddy",    [78, 82, 80, 85], 88.5, 210000, 18),
        ("26B91A0503", "Chaitanya V.",    [92, 95, 91, 94], 94.0, 150000, 19),
        ("26B91A0504", "Divya Sri",       [85, 90, 88, 92], 91.0, 180000, 18), # Tie with Aarav, but younger!
        ("26B91A0505", "Eshwar Rao",      [45, 88, 85, 90], 82.0, 140000, 19), # Subject fail (<50)
        ("26B91A0506", "Fatima Zahra",    [72, 70, 74, 71], 79.0, 190000, 19), # Low agg (<75)
        ("26B91A0507", "Ganesh Kumar",    [88, 86, 90, 84], 72.0, 160000, 20), # Low attendance (<75)
        ("26B91A0508", "Harini Murthy",   [90, 92, 89, 93], 89.0, 320000, 19), # High income (>250k)
        ("26B91A0509", "Ishaan Verma",    [80, 82, 79, 83], 86.0, 220000, 19),
        ("26B91A0510", "Janani Iyer",     [85, 90, 88, 92], 93.0, 190000, 19)  # Agg tie, higher att
    ]

    quota = 3
    selected, waitlist, disqualified = evaluate_and_rank_scholarships(applicants_data, quota)
    print_scholarship_report(selected, waitlist, disqualified, quota)
