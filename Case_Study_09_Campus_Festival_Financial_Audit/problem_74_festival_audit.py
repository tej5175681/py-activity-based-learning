"""
Case Study 09: Campus Festival Registration and Financial Audit System
=====================================================================
Syllabus Concepts Used:
- Lists and Nested Lists (Multi-Category Expense Ledgers)
- Tuples, Tuple Unpacking, and Tuple Concatenation
- String Slicing and Formatting
- Variables and Numerical Types (float, int, str, bool)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops and Membership Iteration for Duplicate Detection
- Formatted Financial Statements and Auditing Reports

Description:
Reconciles festival accounts for the annual university techno-cultural fest:
1. Audits participant registrations: flags duplicates (same student + same event)
   and isolates verified collected registration revenue.
2. Audits corporate sponsorship contributions across tiers (committed vs received).
3. Reconciles itemized expenditures against allocated budgets.
4. Computes net fiscal surplus / deficit and compiles an audit certificate.
"""

def audit_festival_finances(registrations, sponsorships, expenses):
    """
    registrations: List of tuples
      (reg_id, student_id, student_name, event_code, fee_paid, status)
    sponsorships: List of tuples
      (sponsor_id, company_name, tier, committed_amount, received_amount)
    expenses: Nested list
      [[category, item_desc, budgeted_amount, actual_amount], ...]
    """
    # 1. Audit Registrations and Detect Duplicates
    seen_student_events = []
    valid_registrations = []
    duplicate_registrations = []
    total_reg_collected = 0.0
    pending_reg_fees = 0.0

    for reg in registrations:
        reg_id, s_id, s_name, ev_code, fee, status = reg
        pair_key = s_id.upper() + "::" + ev_code.upper()

        if pair_key in seen_student_events:
            duplicate_registrations.append(reg)
        else:
            seen_student_events.append(pair_key)
            if status.upper() == "PAID":
                valid_registrations.append(reg)
                total_reg_collected += fee
            else:
                pending_reg_fees += fee

    # 2. Audit Sponsorship Contributions
    total_sponsorship_committed = 0.0
    total_sponsorship_received = 0.0
    sponsorship_shortfalls = []

    for sp in sponsorships:
        sp_id, comp, tier, committed, received = sp
        total_sponsorship_committed += committed
        total_sponsorship_received += received
        shortfall = committed - received
        if shortfall > 0:
            sponsorship_shortfalls.append((sp_id, comp, tier, committed, received, shortfall))

    # 3. Audit Itemized Expenditures and Variance
    total_budgeted_exp = 0.0
    total_actual_exp = 0.0
    expense_summary = []

    for exp in expenses:
        cat, item, budgeted, actual = exp
        total_budgeted_exp += budgeted
        total_actual_exp += actual
        variance = budgeted - actual  # Positive means under budget (savings)
        is_overbudget = (actual > budgeted)
        expense_summary.append((cat, item, budgeted, actual, variance, is_overbudget))

    # 4. Net Financial Reconciliation
    total_income = total_reg_collected + total_sponsorship_received
    net_balance = total_income - total_actual_exp
    is_surplus = (net_balance >= 0.0)

    audit_summary = (
        len(valid_registrations),
        len(duplicate_registrations),
        total_reg_collected,
        pending_reg_fees,
        total_sponsorship_received,
        total_actual_exp,
        total_income,
        net_balance,
        is_surplus
    )

    return (
        valid_registrations,
        duplicate_registrations,
        sponsorship_shortfalls,
        expense_summary,
        audit_summary
    )


def print_financial_audit_report(registrations, sponsorships, expenses, audit_data):
    valid_regs, dup_regs, shortfalls, exp_summary, summary = audit_data
    val_cnt, dup_cnt, reg_rev, pend_fees, spon_rev, tot_exp, tot_inc, net_bal, is_surplus = summary

    print("=" * 105)
    print("                    DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("        COLLEGE FESTIVAL: SIMPLE FINANCIAL SUMMARY")
    print("=" * 105)

    print("\n[SECTION 1: PARTICIPANT REGISTRATION & DUPLICATE ENTRY AUDIT]")
    print(f"Total Entries Audited   : {len(registrations)}")
    print(f"Verified Paid Entries   : {val_cnt}")
    print(f"Duplicate Entries Flagged: {dup_cnt}")
    print(f"Total Fees Collected    : INR {reg_rev:>10,.2f}")
    print(f"Unpaid / Pending Fees   : INR {pend_fees:>10,.2f}")

    if len(dup_regs) > 0:
        print("\n  >> FLAGGED DUPLICATE REGISTRATIONS (ACTION: VOID & REFUND)")
        print(f"  {'Reg ID':<10}{'Student ID':<14}{'Name':<20}{'Event':<14}{'Fee Paid':<10}")
        print("  " + "-" * 68)
        for d in dup_regs:
            rid, sid, sname, ev, f, _ = d
            print(f"  {rid:<10}{sid:<14}{sname:<20}{ev:<14}INR {f:>6,.2f}")

    print("-" * 105)
    print("\n[SECTION 2: CORPORATE SPONSORSHIP RECONCILIATION]")
    print(f"{'Sponsor ID':<12}{'Company Name':<22}{'Tier':<14}{'Committed(INR)':<16}{'Received(INR)':<16}{'Shortfall'}")
    print("-" * 105)
    for sp in sponsorships:
        sid, comp, tier, comm, rec = sp
        diff = comm - rec
        diff_str = f"INR {diff:>7,.2f}" if diff > 0 else "NIL"
        print(f"{sid:<12}{comp:<22}{tier:<14}{comm:<16,.2f}{rec:<16,.2f}{diff_str}")

    print("-" * 105)
    print("\n[SECTION 3: ITEMIZED EXPENDITURE & VARIANCE ANALYSIS]")
    print(f"{'Category':<16}{'Item Description':<24}{'Budget(INR)':<14}{'Actual(INR)':<14}{'Variance(INR)':<14}{'Audit Alert'}")
    print("-" * 105)
    for row in exp_summary:
        cat, item, b_cost, a_cost, var, over = row
        alert = "OVER-BUDGET [!]" if over else "Under Budget"
        prefix = "+" if var > 0 else ""
        print(f"{cat:<16}{item:<24}{b_cost:<14,.2f}{a_cost:<14,.2f}{prefix + f'{var:,.2f}':<14}{alert}")

    print("-" * 105)
    print("\n[SECTION 4: FINAL RECONCILIATION BALANCE SHEET]")
    print(f"  Total Revenue Collected from Registrations : INR {reg_rev:>12,.2f}")
    print(f"  Total Corporate Sponsorships Realized     : INR {spon_rev:>12,.2f}")
    print(f"  -------------------------------------------------------------")
    print(f"  TOTAL GROSS REVENUE                       : INR {tot_inc:>12,.2f}")
    print(f"  LESS: TOTAL FESTIVAL EXPENDITURES         : INR {tot_exp:>12,.2f}")
    print(f"  =============================================================")
    status_text = "NET FINANCIAL SURPLUS" if is_surplus else "NET OPERATIONAL DEFICIT"
    print(f"  >>> {status_text:<38}: INR {net_bal:>12,.2f}")
    print("=" * 105)


if __name__ == "__main__":
    registrations_data = [
        ("REG-001", "26B91A0501", "Aarav Sharma",    "CODE-HACK", 500.0, "PAID"),
        ("REG-002", "26B91A0502", "Bhavya Reddy",    "ROBOTICS",  600.0, "PAID"),
        ("REG-003", "26B91A0501", "Aarav Sharma",    "CODE-HACK", 500.0, "PAID"), # Duplicate!
        ("REG-004", "26B91A0504", "Divya Sri",       "PAPER-PRES",300.0, "PAID"),
        ("REG-005", "26B91A0505", "Eshwar Rao",      "ROBOTICS",  600.0, "PENDING"),
        ("REG-006", "26B91A0506", "Fatima Zahra",    "CODE-HACK", 500.0, "PAID"),
    ]

    sponsorships_data = [
        ("SP-01", "TechCorp Global",   "Title Sponsor",    150000.0, 150000.0),
        ("SP-02", "V-Infotech Labs",   "Platinum Sponsor",  80000.0,  70000.0), # 10k shortfall
        ("SP-03", "NextGen Robotics",  "Gold Sponsor",      40000.0,  40000.0),
    ]

    expenses_ledger = [
        ["Venue & Stage", "Main Auditorium Setup", 50000.0, 48000.0],
        ["Audio-Visual",  "Sound & LED Displays",  45000.0, 47000.0], # 2k Over
        ["Guest Honoraria","Keynote Speakers Travel",35000.0, 32000.0],
        ["Catering",      "Student & Guest Meals",  60000.0, 64000.0], # 4k Over
        ["Certificates",  "Trophies and Badges",    25000.0, 21000.0],
    ]

    audit_result = audit_festival_finances(registrations_data, sponsorships_data, expenses_ledger)
    print_financial_audit_report(registrations_data, sponsorships_data, expenses_ledger, audit_result)
