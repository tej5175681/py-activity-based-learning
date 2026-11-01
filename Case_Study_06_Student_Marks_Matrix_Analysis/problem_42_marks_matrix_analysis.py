"""
Case Study 06: Student Marks Matrix Analysis System
===================================================
Syllabus Concepts Used:
- Variables, Data Types (int, float, str, bool)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops (row-wise and column-wise matrix traversals)
- Nested Lists (2D Grid Representation)
- Tuples and Tuple Unpacking
- String Formatting for 2D Tabular Display

Description:
Performs 2-dimensional matrix computation on academic assessment marks:
1. Row-Wise Analytics: Student totals, averages, percentages, letter grades,
   and pass/fail determinations (pass mark = 40 per subject).
2. Column-Wise Analytics: Subject means, highest marks, lowest marks,
   and subject-specific pass percentages.
3. Class performance summary: Finds the students with the highest marks
   and flags curricular subjects with below-benchmark averages (< 65.0%).
"""

def determine_grade(pct, passed_all):
    if not passed_all:
        return "F (Fail)"
    if pct >= 85.0:
        return "O (Outstanding)"
    elif pct >= 75.0:
        return "A+ (Excellent)"
    elif pct >= 65.0:
        return "A (Very Good)"
    elif pct >= 55.0:
        return "B (Good)"
    elif pct >= 40.0:
        return "C (Pass)"
    else:
        return "F (Fail)"


def analyze_marks_matrix(students, subjects, marks_matrix):
    """
    students: List of tuples (roll_no, name)
    subjects: List of strings [sub1, sub2, sub3, sub4, sub5]
    marks_matrix: 2D Nested List of integers [num_students x num_subjects]
    """
    num_students = len(students)
    num_subjects = len(subjects)

    # 1. Row-Wise Analysis (Student-wise)
    student_results = []
    top_performer = None
    highest_total = -1

    for i in range(num_students):
        roll, name = students[i]
        row_marks = marks_matrix[i]

        row_total = 0
        all_passed = True
        for m in row_marks:
            row_total += m
            if m < 40:
                all_passed = False

        avg = row_total / num_subjects if num_subjects > 0 else 0.0
        pct = avg  # Assuming each subject out of 100
        grade = determine_grade(pct, all_passed)
        status = "PASSED" if all_passed else "FAILED"

        record = (roll, name, row_marks, row_total, avg, grade, status)
        student_results.append(record)

        if all_passed and row_total > highest_total:
            highest_total = row_total
            top_performer = (roll, name, row_total, pct)

    # 2. Column-Wise Analysis (Subject-wise)
    subject_stats = []
    low_performing_subjects = []

    for j in range(num_subjects):
        sub_name = subjects[j]
        col_sum = 0
        col_max = -1
        col_min = 1000
        pass_count = 0

        for i in range(num_students):
            score = marks_matrix[i][j]
            col_sum += score
            if score > col_max:
                col_max = score
            if score < col_min:
                col_min = score
            if score >= 40:
                pass_count += 1

        sub_avg = col_sum / num_students if num_students > 0 else 0.0
        sub_pass_pct = (pass_count / num_students) * 100.0 if num_students > 0 else 0.0

        stat_tuple = (sub_name, sub_avg, col_max, col_min, sub_pass_pct)
        subject_stats.append(stat_tuple)

        if sub_avg < 65.0 or sub_pass_pct < 70.0:
            low_performing_subjects.append(stat_tuple)

    return student_results, subject_stats, top_performer, low_performing_subjects


def print_matrix_analysis_report(students, subjects, student_results, subject_stats, top_performer, low_subjects):
    print("=" * 110)
    print("                      DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("                2D MARKS MATRIX ACADEMIC PERFORMANCE AUDIT REPORT")
    print("=" * 110)

    # Header with subjects abbreviated for clean column display
    sub_headers = "".join([f"{s[:10]:>11}" for s in subjects])
    print(f"{'Roll No':<12}{'Student Name':<18}{sub_headers}{'Total':>8}{'Avg %':>8}{'Grade':>16}{'Status':>10}")
    print("-" * 110)

    for item in student_results:
        roll, name, row_marks, tot, avg, grade, status = item
        marks_str = "".join([f"{m:>11}" for m in row_marks])
        print(f"{roll:<12}{name:<18}{marks_str}{tot:>8}{avg:>8.1f}{grade:>16}{status:>10}")

    print("-" * 110)
    print("\n[PART 2: SUBJECT-WISE COLUMN STATISTICS & CURRICULAR BENCHMARKS]")
    print(f"{'Subject Name':<25}{'Subject Mean':<16}{'Highest Mark':<16}{'Lowest Mark':<16}{'Pass Rate %':<16}")
    print("-" * 110)
    for stat in subject_stats:
        sname, savg, smax, smin, spass = stat
        print(f"{sname:<25}{savg:<16.2f}{smax:<16}{smin:<16}{spass:<16.1f}%")

    print("-" * 110)
    print("\n[PART 3: CLASS SUMMARY]")
    if top_performer:
        t_roll, t_name, t_tot, t_pct = top_performer
        print(f"> Top student : {t_name} ({t_roll}) | Total: {t_tot} ({t_pct:.2f}%)")
    else:
        print("> Top student : None")

    if len(low_subjects) > 0:
        print(f"> ATTENTION REQUIRED: {len(low_subjects)} Subject(s) Flagged Below Academic Benchmark (< 65% Mean):")
        for sub in low_subjects:
            sn, sa, _, _, sp = sub
            print(f"    - {sn}: Mean = {sa:.1f}/100, Pass Percentage = {sp:.1f}% [Remedial Sessions Recommended]")
    else:
        print("> All subjects are above the practice limits.")
    print("=" * 110)


if __name__ == "__main__":
    student_list = [
        ("26B91A0501", "Aarav Sharma"),
        ("26B91A0502", "Bhavya Reddy"),
        ("26B91A0503", "Chaitanya V."),
        ("26B91A0504", "Divya Sri"),
        ("26B91A0505", "Eshwar Rao"),
        ("26B91A0506", "Fatima Zahra")
    ]

    subject_list = [
        "Python Prog",
        "Data Struct",
        "Digital Logic",
        "Discrete Math",
        "Eng Physics"
    ]

    # 6 x 5 Marks Matrix (Nested Lists)
    marks_grid = [
        [88, 92, 85, 90, 84],  # Aarav
        [75, 78, 68, 72, 70],  # Bhavya
        [94, 96, 91, 95, 92],  # Chaitanya (Top)
        [82, 85, 80, 84, 81],  # Divya
        [32, 60, 55, 45, 50],  # Eshwar (Fails Python with 32)
        [70, 72, 58, 62, 65]   # Fatima
    ]

    results, stats, top, low = analyze_marks_matrix(student_list, subject_list, marks_grid)
    print_matrix_analysis_report(student_list, subject_list, results, stats, top, low)
