"""
Case Study 03: Employee Payroll and Progressive Deduction Analysis System
========================================================================
Syllabus Concepts Used:
- Variables and Numerical Data Types
- Arithmetic, Relational, and Logical Operators
- Conditional Statements (if, elif, else)
- Loops (for, while)
- Lists and Nested Lists
- Tuples and Tuple Unpacking
- String Formatting and Formatted Statements

Description:
Calculates gross salary from basic pay, progressive allowances, overtime wages,
and performance incentives.
Computes progressive income tax deductions along with statutory deductions:
- Provident Fund (12% of Basic)
- Professional Tax (Flat INR 200)
- Group Health Insurance (Flat INR 1,000)
- Progressive Income Tax Slabs:
    0 - 30,000       : 0%
    30,001 - 60,000  : 5%
    60,001 - 100,000 : 10%
    Above 100,000    : 20%

Generates itemized payslips and a small payroll summary.
"""

def compute_employee_payroll(employee_record):
    """
    employee_record: (emp_id, name, designation, basic_pay, ot_hours, rating)
    Returns:
    earnings_tuple: (basic, da, hra, special_allw, ot_pay, incentive, gross)
    deductions_tuple: (income_tax, pf, prof_tax, health_ins, total_deductions)
    net_salary: float
    """
    emp_id, name, designation, basic_pay, ot_hours, rating = employee_record

    # 1. Allowances
    da = 0.15 * basic_pay
    hra = 0.20 * basic_pay
    special_allowance = 0.10 * basic_pay

    # 2. Overtime Pay (160 standard working hours per month, 1.5x multiplier)
    hourly_rate = basic_pay / 160.0
    ot_pay = ot_hours * hourly_rate * 1.50

    # 3. Performance Incentives
    if rating == 5:
        incentive = 12000.0
    elif rating == 4:
        incentive = 8000.0
    elif rating == 3:
        incentive = 4000.0
    else:
        incentive = 0.0

    gross_salary = basic_pay + da + hra + special_allowance + ot_pay + incentive

    # 4. Progressive Income Tax Calculation
    taxable_gross = gross_salary
    income_tax = 0.0

    # Tax slabs: (slab_range, rate)
    tax_slabs = [
        (30000.0, 0.00),   # 0 to 30,000
        (30000.0, 0.05),   # 30,001 to 60,000
        (40000.0, 0.10),   # 60,001 to 100,000
    ]
    tax_rate_above = 0.20  # Above 100,000

    rem_gross = taxable_gross
    for slab_span, rate in tax_slabs:
        if rem_gross > 0:
            taxable_chunk = min(rem_gross, slab_span)
            income_tax += taxable_chunk * rate
            rem_gross -= taxable_chunk
        else:
            break

    if rem_gross > 0:
        income_tax += rem_gross * tax_rate_above

    # 5. Statutory Deductions
    pf = 0.12 * basic_pay
    prof_tax = 200.0
    health_insurance = 1000.0
    total_deductions = income_tax + pf + prof_tax + health_insurance

    # 6. Net Take-Home Salary
    net_salary = gross_salary - total_deductions

    earnings = (basic_pay, da, hra, special_allowance, ot_pay, incentive, gross_salary)
    deductions = (income_tax, pf, prof_tax, health_insurance, total_deductions)

    return (earnings, deductions, net_salary)


def generate_batch_payroll(employees):
    """
    Processes a list of employee records and prints a simple payroll register.
    """
    processed_records = []
    total_gross_disbursed = 0.0
    total_tax_collected = 0.0
    total_pf_collected = 0.0
    total_net_disbursed = 0.0

    for emp in employees:
        emp_id, name, designation, basic, ot, rating = emp
        earnings, deductions, net = compute_employee_payroll(emp)
        processed_records.append((emp, earnings, deductions, net))

        # Unpack earnings and deductions for aggregations
        _, _, _, _, _, _, gross = earnings
        tax, pf, _, _, _ = deductions

        total_gross_disbursed += gross
        total_tax_collected += tax
        total_pf_collected += pf
        total_net_disbursed += net

    totals = (total_gross_disbursed, total_tax_collected, total_pf_collected, total_net_disbursed)
    return processed_records, totals


def print_single_payslip(emp_payroll_entry):
    emp, earnings, deductions, net = emp_payroll_entry
    emp_id, name, desig, basic, ot_hrs, rating = emp
    b, da, hra, sp_allw, ot_pay, inc, gross = earnings
    tax, pf, pt, hi, tot_ded = deductions

    print("+" + "-" * 78 + "+")
    print(f"| {'DR. RVR NRI INSTITUTE OF TECHNOLOGY - MONTHLY PAYSLIP':^76} |")
    print("+" + "-" * 78 + "+")
    print(f"| Emp ID      : {emp_id:<20} Designation : {desig:<26} |")
    print(f"| Employee    : {name:<20} Performance : Rating {rating}/5 (OT: {ot_hrs} hrs)     |")
    print("+" + "-" * 38 + "+" + "-" * 39 + "+")
    print(f"| {'EARNINGS (CREDITS)':<36} | {'DEDUCTIONS (DEBITS)':<37} |")
    print("+" + "-" * 38 + "+" + "-" * 39 + "+")
    print(f"| Basic Pay            : INR {b:>9,.2f} | Income Tax (Slab)   : INR {tax:>9,.2f} |")
    print(f"| Dearness Allw (15%)  : INR {da:>9,.2f} | Provident Fund (12%): INR {pf:>9,.2f} |")
    print(f"| House Rent Allw (20%): INR {hra:>9,.2f} | Professional Tax    : INR {pt:>9,.2f} |")
    print(f"| Special Allw (10%)   : INR {sp_allw:>9,.2f} | Health Insurance    : INR {hi:>9,.2f} |")
    print(f"| Overtime Compensation: INR {ot_pay:>9,.2f} |                                       |")
    print(f"| Performance Incentive: INR {inc:>9,.2f} |                                       |")
    print("+" + "-" * 38 + "+" + "-" * 39 + "+")
    print(f"| GROSS SALARY         : INR {gross:>9,.2f} | TOTAL DEDUCTIONS    : INR {tot_ded:>9,.2f} |")
    print("+" + "-" * 78 + "+")
    print(f"| >>> NET TAKE-HOME SALARY DISBURSED : INR {net:>14,.2f}                          |")
    print("+" + "-" * 78 + "+\n")


def print_payroll_register(processed_records, totals):
    print("=" * 102)
    print("                  DR. RVR NRI INSTITUTE OF TECHNOLOGY - PAYROLL REGISTER")
    print("=" * 102)
    print(f"{'Emp ID':<10}{'Name':<18}{'Designation':<16}{'Basic(INR)':<12}{'Gross(INR)':<14}{'Deductions':<14}{'Net Pay(INR)':<14}")
    print("-" * 102)

    for item in processed_records:
        emp, earnings, deductions, net = item
        emp_id, name, desig, basic, _, _ = emp
        _, _, _, _, _, _, gross = earnings
        _, _, _, _, tot_ded = deductions
        print(f"{emp_id:<10}{name:<18}{desig:<16}{basic:<12,.2f}{gross:<14,.2f}{tot_ded:<14,.2f}{net:<14,.2f}")

    print("-" * 102)
    tot_gross, tot_tax, tot_pf, tot_net = totals
    print(f"TOTALS: Gross: INR {tot_gross:,.2f} | Tax: INR {tot_tax:,.2f} | PF: INR {tot_pf:,.2f} | Net Disbursed: INR {tot_net:,.2f}")
    print("=" * 102)


if __name__ == "__main__":
    employee_roster = [
        ("EMP-101", "Dr. K. Srinivas",    "Professor",         85000.0, 10, 5),
        ("EMP-102", "P. Anitha Reddy",    "Assoc. Professor",  62000.0,  5, 4),
        ("EMP-103", "V. Suresh Kumar",    "Asst. Professor",   45000.0, 15, 3),
        ("EMP-104", "M. Lakshmi",         "Lab Instructor",    28000.0, 20, 4),
        ("EMP-105", "T. Rajesh",          "Office Admin",      22000.0,  0, 2),
    ]

    records, batch_totals = generate_batch_payroll(employee_roster)
    print_single_payslip(records[0])
    print_payroll_register(records, batch_totals)
