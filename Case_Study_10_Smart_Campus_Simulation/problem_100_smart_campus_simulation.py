"""
Case Study 10: Simple Smart Campus Menu
===============================================================
Syllabus Concepts Used:
- Variables, Data Types (int, float, str, bool)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops and While Loops (Menu-Driven Architecture)
- Strings (formatting, centering, banners, alignment)
- Pattern Generation (Grid visualization and terminal banners)
- Lists and Nested Lists (2D Lab Seat Grids, Marks Matrix, Attendance Logs)
- Tuples, Tuple Concatenation, and Tuple Unpacking

Description:
A small terminal program showing a few campus activities:
1. Student Academic Registry
2. Attendance Monitoring & Condonation/Shortage Alert Engine (< 75% threshold)
3. Internal Marks Evaluation & Grade Determination
4. Campus Event Registration & Duplicate Shield
5. Computer Lab Seating Grid & Resource Allocation Matrix (2D Nested List)
6. Campus Summary
"""

def initialize_campus_data():
    """
    Initializes simulated campus datasets.
    """
    # Student Registry: List of tuples (roll_no, name, branch, section)
    students = [
        ("26B91A0501", "Aarav Sharma",    "CSE", "A"),
        ("26B91A0502", "Bhavya Reddy",    "CSE", "A"),
        ("26B91A0503", "Chaitanya V.",    "CSE", "B"),
        ("26B91A0504", "Divya Sri",       "ECE", "A"),
        ("26B91A0505", "Eshwar Rao",      "ECE", "B"),
    ]

    # Attendance: List of tuples (roll_no, total_classes, attended_classes)
    attendance = [
        ("26B91A0501", 100, 92),
        ("26B91A0502", 100, 84),
        ("26B91A0503", 100, 95),
        ("26B91A0504", 100, 68),  # Shortage (<75%)
        ("26B91A0505", 100, 72),  # Shortage (<75%)
    ]

    # Marks Matrix: Nested List [5 students x 3 subjects: Python, DS, Math]
    subjects = ["Python", "DataStruct", "Math"]
    marks = [
        [88, 92, 85],
        [75, 80, 72],
        [94, 96, 91],
        [82, 85, 79],
        [35, 58, 52],  # Python Fail (<40)
    ]

    # Events: List of tuples (event_code, event_name, max_capacity, registered_list)
    events = [
        ("EV-HACK", "Annual Hackathon", 3, ["26B91A0501", "26B91A0502"]),
        ("EV-ROBO", "Robotics Contest", 2, ["26B91A0503"]),
    ]

    # Lab Seating Grid: 3 rows x 4 columns (Nested List of strings)
    # "." represents vacant, Roll Number represents occupied
    lab_seats = [
        ["26B91A0501", ".", ".", "26B91A0502"],
        [".", "26B91A0503", ".", "."],
        [".", ".", "26B91A0504", "."]
    ]

    return students, attendance, subjects, marks, events, lab_seats


def display_registry(students):
    print("\n" + "=" * 70)
    print("           MODULE 1: STUDENT ACADEMIC REGISTRY")
    print("=" * 70)
    print(f"{'Roll Number':<16}{'Student Name':<24}{'Branch':<12}{'Section':<10}")
    print("-" * 70)
    for s in students:
        roll, name, branch, sec = s
        print(f"{roll:<16}{name:<24}{branch:<12}{sec:<10}")
    print("=" * 70)


def audit_attendance(students, attendance, threshold=75.0):
    print("\n" + "=" * 75)
    print("        MODULE 2: ATTENDANCE MONITORING & SHORTAGE WARNINGS")
    print("=" * 75)
    print(f"{'Roll Number':<16}{'Name':<20}{'Attended':<12}{'Total':<10}{'Att %':<10}{'Status'}")
    print("-" * 75)
    shortage_count = 0
    shortage_list = []

    for i in range(len(students)):
        roll, name, _, _ = students[i]
        _, tot, att = attendance[i]
        pct = (att / tot) * 100.0 if tot > 0 else 0.0

        if pct < threshold:
            status = "SHORTAGE ALERT [!]"
            shortage_count += 1
            shortage_list.append((roll, name, pct))
        else:
            status = "ELIGIBLE (Pass)"

        print(f"{roll:<16}{name:<20}{att:<12}{tot:<10}{pct:<10.1f}{status}")

    print("-" * 75)
    print(f"Attendance Audit: {shortage_count} student(s) below mandatory {threshold:.1f}% threshold.")
    print("=" * 75)
    return shortage_list


def evaluate_marks(students, subjects, marks):
    print("\n" + "=" * 80)
    print("        MODULE 3: ACADEMIC MARKS & PERFORMANCE EVALUATION")
    print("=" * 80)
    header = f"{'Roll':<14}{'Name':<18}"
    for sub in subjects:
        header += f"{sub:>10}"
    header += f"{'Total':>8}{'Avg %':>8}{'Status':>10}"
    print(header)
    print("-" * 80)

    for i in range(len(students)):
        roll, name, _, _ = students[i]
        scores = marks[i]
        tot = sum(scores)
        avg = tot / len(subjects) if len(subjects) > 0 else 0.0
        passed = all(m >= 40 for m in scores)
        status = "PASSED" if passed else "FAILED"

        row = f"{roll:<14}{name:<18}"
        for s in scores:
            row += f"{s:>10}"
        row += f"{tot:>8}{avg:>8.1f}{status:>10}"
        print(row)
    print("=" * 80)


def register_for_event(events, event_code, student_roll):
    """
    Registers a student for a campus event.
    Enforces duplicate checking and capacity limits.
    """
    for i in range(len(events)):
        code, name, cap, reg_list = events[i]
        if code.upper() == event_code.upper():
            if student_roll in reg_list:
                return False, f"Duplicate Error: Student {student_roll} is already registered for {name}."
            if len(reg_list) >= cap:
                return False, f"Capacity Exceeded: {name} is at full capacity ({cap}/{cap})."
            
            # Register student
            reg_list.append(student_roll)
            return True, f"Registration Successful: {student_roll} enrolled in {name}."

    return False, f"Event Not Found: Code {event_code} does not exist."


def display_events(events):
    print("\n" + "=" * 75)
    print("           MODULE 4: CAMPUS EVENT ROSTERS & CAPACITY")
    print("=" * 75)
    print(f"{'Code':<12}{'Event Name':<22}{'Capacity':<12}{'Enrolled':<12}{'Available'}")
    print("-" * 75)
    for code, name, cap, reg_list in events:
        avail = cap - len(reg_list)
        print(f"{code:<12}{name:<22}{cap:<12}{len(reg_list):<12}{avail:<12}")
        if len(reg_list) > 0:
            print(f"   -> Participants: {', '.join(reg_list)}")
    print("=" * 75)


def display_lab_grid(lab_seats):
    print("\n" + "=" * 65)
    print("      MODULE 5: COMPUTER LAB SEAT ALLOCATION")
    print("=" * 65)
    rows = len(lab_seats)
    cols = len(lab_seats[0]) if rows > 0 else 0

    vacant = 0
    occupied = 0

    col_hdr = "       " + "".join([f"Col {c:<8}" for c in range(cols)])
    print(col_hdr)
    print("      " + "-" * (cols * 12))

    for r in range(rows):
        row_str = f"Row {r}: "
        for c in range(cols):
            val = lab_seats[r][c]
            if val == ".":
                vacant += 1
                row_str += f"{'[EMPTY]':<12}"
            else:
                occupied += 1
                row_str += f"{val:<12}"
        print(row_str)

    print("-" * 65)
    print(f"Seat Statistics: Total = {rows*cols} | Occupied = {occupied} | Vacant = {vacant}")
    print("=" * 65)


def allocate_lab_seat(lab_seats, row, col, student_roll):
    rows = len(lab_seats)
    cols = len(lab_seats[0])

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False, f"Invalid Coordinates: ({row}, {col}) is out of bounds."

    if lab_seats[row][col] != ".":
        return False, f"Seat Occupied: ({row}, {col}) is already assigned to {lab_seats[row][col]}."

    # Check duplicate student in lab
    for r in range(rows):
        for c in range(cols):
            if lab_seats[r][c] == student_roll:
                return False, f"Duplicate Error: Student {student_roll} is already seated at ({r}, {c})."

    lab_seats[row][col] = student_roll
    return True, f"Seat Allocated: Student {student_roll} placed at Row {row}, Col {col}."


def generate_executive_audit_report(students, attendance, subjects, marks, events, lab_seats):
    print("\n" + "#" * 85)
    print("   SMART CAMPUS SUMMARY")
    print("#" * 85)

    tot_students = len(students)
    shortages = sum(1 for _, t, a in attendance if (a/t)*100 < 75.0)
    failed = sum(1 for m_row in marks if any(s < 40 for s in m_row))
    tot_events = len(events)
    tot_seats = len(lab_seats) * len(lab_seats[0])
    vac_seats = sum(row.count(".") for row in lab_seats)

    print(f"| Metric 1: Total Enrolled Students       : {tot_students:<20} |")
    print(f"| Metric 2: Attendance Shortage Alerts    : {shortages:<20} |")
    print(f"| Metric 3: Academic Remedial Students    : {failed:<20} |")
    print(f"| Metric 4: Active Campus Events          : {tot_events:<20} |")
    print(f"| Metric 5: Computer Lab Seat Vacancies   : {vac_seats}/{tot_seats:<18} |")
    print("#" * 85 + "\n")


def run_campus_simulation(interactive=False):
    students, attendance, subjects, marks, events, lab_seats = initialize_campus_data()

    if not interactive:
        # Show a fixed example when the program is run normally.
        display_registry(students)
        audit_attendance(students, attendance)
        evaluate_marks(students, subjects, marks)
        display_events(events)

        # Event registration demonstration
        print("\n[ACTION: Registering 26B91A0504 for EV-ROBO]")
        ok, msg = register_for_event(events, "EV-ROBO", "26B91A0504")
        print(f"Status: {msg}")

        print("\n[ACTION: Attempting Duplicate Registration for EV-ROBO]")
        ok, msg = register_for_event(events, "EV-ROBO", "26B91A0504")
        print(f"Status: {msg}")

        print("\n[ACTION: Attempting Overflow Registration on EV-ROBO]")
        ok, msg = register_for_event(events, "EV-ROBO", "26B91A0505")
        print(f"Status: {msg}")

        display_lab_grid(lab_seats)

        # Lab seat allocation demonstration
        print("\n[ACTION: Allocating Seat (Row 1, Col 0) for 26B91A0505]")
        ok, msg = allocate_lab_seat(lab_seats, 1, 0, "26B91A0505")
        print(f"Status: {msg}")
        display_lab_grid(lab_seats)

        generate_executive_audit_report(students, attendance, subjects, marks, events, lab_seats)
        return

    # Interactive Menu Mode
    while True:
        print("\n" + "=" * 55)
        print("     SMART CAMPUS MANAGEMENT SYSTEM - MAIN MENU")
        print("=" * 55)
        print("1. View Student Academic Registry")
        print("2. Run Attendance Monitoring & Shortage Check")
        print("3. View Internal Assessment Marks Matrix")
        print("4. Event Rosters & Register Student for Event")
        print("5. Lab Seating Grid & Allocate Workspace")
        print("6. Show Campus Summary")
        print("7. Exit Simulation")
        print("=" * 55)

        choice = input("Enter option (1-7): ").strip()
        if choice == "1":
            display_registry(students)
        elif choice == "2":
            audit_attendance(students, attendance)
        elif choice == "3":
            evaluate_marks(students, subjects, marks)
        elif choice == "4":
            display_events(events)
            ev_code = input("Enter Event Code to register (or press enter to skip): ").strip()
            if ev_code:
                s_roll = input("Enter Student Roll Number: ").strip()
                ok, msg = register_for_event(events, ev_code, s_roll)
                print(msg)
        elif choice == "5":
            display_lab_grid(lab_seats)
            ans = input("Allocate seat? (y/n): ").strip().lower()
            if ans == "y":
                try:
                    r = int(input("Enter Row Index: "))
                    c = int(input("Enter Col Index: "))
                    s_roll = input("Enter Student Roll Number: ").strip()
                    ok, msg = allocate_lab_seat(lab_seats, r, c, s_roll)
                    print(msg)
                except ValueError:
                    print("Invalid numeric row/col input.")
        elif choice == "6":
            generate_executive_audit_report(students, attendance, subjects, marks, events, lab_seats)
        elif choice == "7":
            print("Exiting Smart Campus Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    run_campus_simulation(interactive=False)
