"""
Case Study 02: Progressive Electricity Billing and Spike Detection System
========================================================================
Syllabus Concepts Used:
- Variables, Data Types (int, float, str, bool)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Loops (for, while)
- Lists and Nested Lists
- Tuples and Tuple Unpacking
- String Formatting

Description:
Calculates household electricity bills using progressive consumption slabs:
- Slab 1: 0 to 100 units       @ INR 1.50 per unit
- Slab 2: 101 to 200 units     @ INR 3.00 per unit
- Slab 3: 201 to 400 units     @ INR 4.50 per unit
- Slab 4: Above 400 units      @ INR 6.00 per unit
- Fixed Meter Infrastructure Charge: INR 100.00
- High Consumption Surcharge: 10% on energy charge if energy charge > INR 1,500.00
- Early Prompt Payment Rebate: 5% discount on total if paid on or before due date

Compares multi-month billing trends and flags unusual spikes (> 25% increase).
"""

def calculate_single_bill(units, paid_on_time):
    """
    Computes itemized electricity bill for a given consumption in units.
    Returns tuple: (units, energy_charge, fixed_charge, surcharge, rebate, net_bill)
    """
    if units < 0:
        return (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    # Slabs definition: List of tuples (slab_limit, rate_per_unit)
    slabs = [
        (100, 1.50),  # First 100 units
        (100, 3.00),  # Next 100 units (101-200)
        (200, 4.50),  # Next 200 units (201-400)
    ]
    rate_above = 6.00  # Beyond 400 units

    remaining_units = float(units)
    energy_charge = 0.0

    # Progressive slab calculation using loop and tuple unpacking
    for slab_limit, slab_rate in slabs:
        if remaining_units > 0:
            units_in_slab = min(remaining_units, float(slab_limit))
            energy_charge += units_in_slab * slab_rate
            remaining_units -= units_in_slab
        else:
            break

    # If any units remain beyond the last slab
    if remaining_units > 0:
        energy_charge += remaining_units * rate_above

    fixed_charge = 100.0

    # Surcharge of 10% if energy charge exceeds 1500
    surcharge = 0.0
    if energy_charge > 1500.0:
        surcharge = 0.10 * energy_charge

    subtotal = energy_charge + fixed_charge + surcharge

    # Early payment rebate of 5% on subtotal
    rebate = 0.0
    if paid_on_time:
        rebate = 0.05 * subtotal

    net_bill = subtotal - rebate

    return (units, energy_charge, fixed_charge, surcharge, rebate, net_bill)


def analyze_multimonth_consumption(consumer_info, monthly_readings, spike_threshold_pct=25.0):
    """
    consumer_info: (consumer_no, consumer_name, meter_no)
    monthly_readings: List of tuples: (month_name, units_consumed, paid_on_time)
    """
    c_no, c_name, m_no = consumer_info
    billing_history = []

    # Calculate bills for each month
    for reading in monthly_readings:
        month_name, units, on_time = reading
        bill_tuple = calculate_single_bill(units, on_time)
        billing_history.append((month_name, on_time) + bill_tuple)

    # Spike and trend analysis
    analysis_records = []
    prev_units = None
    prev_bill = None

    for record in billing_history:
        month, on_time, units, energy_chg, fixed_chg, surchg, rebate, net_bill = record
        
        if prev_units is None:
            pct_change_units = 0.0
            pct_change_bill = 0.0
            is_spike = False
            flag_note = "Baseline Month"
        else:
            if prev_units > 0:
                pct_change_units = ((units - prev_units) / prev_units) * 100.0
            else:
                pct_change_units = 100.0 if units > 0 else 0.0

            if prev_bill > 0:
                pct_change_bill = ((net_bill - prev_bill) / prev_bill) * 100.0
            else:
                pct_change_bill = 100.0 if net_bill > 0 else 0.0

            if pct_change_units >= spike_threshold_pct:
                is_spike = True
                flag_note = f"ALERT: High Surge (+{pct_change_units:.1f}%)"
            elif pct_change_units <= -spike_threshold_pct:
                is_spike = False
                flag_note = f"Notice: Sharp Decline ({pct_change_units:.1f}%)"
            else:
                is_spike = False
                flag_note = "Normal Range"

        analysis_records.append((
            month, units, net_bill, pct_change_units, pct_change_bill, is_spike, flag_note
        ))

        prev_units = units
        prev_bill = net_bill

    return billing_history, analysis_records


def print_electricity_report(consumer_info, billing_history, analysis_records):
    c_no, c_name, m_no = consumer_info
    print("=" * 95)
    print("               DR. RVR NRI POWER DISTRIBUTION CORPORATION")
    print("         PROGRESSIVE HOUSEHOLD ELECTRICITY BILL & AUDIT STATEMENT")
    print("=" * 95)
    print(f"Consumer No: {c_no:<15} Consumer Name: {c_name:<25} Meter No: {m_no}")
    print("-" * 95)

    print("\n[PART 1: MONTHLY PROGRESSIVE BILL BREAKDOWN]")
    print(f"{'Month':<10}{'Units':<8}{'Energy(INR)':<14}{'Fixed(INR)':<12}{'Surcharge':<12}{'Rebate':<10}{'Net Bill(INR)':<14}{'Prompt Pay'}")
    print("-" * 95)
    total_units = 0
    total_amount = 0.0

    for rec in billing_history:
        month, on_time, units, echg, fchg, sur, reb, net = rec
        total_units += units
        total_amount += net
        status_str = "YES (-5%)" if on_time else "NO"
        print(f"{month:<10}{units:<8.1f}{echg:<14.2f}{fchg:<12.2f}{sur:<12.2f}{reb:<10.2f}{net:<14.2f}{status_str}")

    print("-" * 95)
    avg_units = total_units / len(billing_history) if len(billing_history) > 0 else 0.0
    avg_bill = total_amount / len(billing_history) if len(billing_history) > 0 else 0.0
    print(f"Total Consumption: {total_units:.1f} Units | Average: {avg_units:.1f} Units/Month | Total Paid: INR {total_amount:,.2f}")

    print("\n[PART 2: MULTI-MONTH SPIKE DETECTION & TREND MONITORING]")
    print(f"{'Month':<10}{'Units':<8}{'Net Bill(INR)':<15}{'Unit Change %':<16}{'Bill Change %':<16}{'Audit Classification'}")
    print("-" * 95)
    spike_count = 0
    for item in analysis_records:
        month, units, net_bill, chg_u, chg_b, is_spike, note = item
        if is_spike:
            spike_count += 1
        sign_u = "+" if chg_u > 0 else ""
        sign_b = "+" if chg_b > 0 else ""
        print(f"{month:<10}{units:<8.1f}{net_bill:<15.2f}{sign_u + f'{chg_u:.1f}%':<16}{sign_b + f'{chg_b:.1f}%':<16}{note}")

    print("-" * 95)
    print(f"Audit Summary: {spike_count} unusual consumption spike(s) detected (>25% increase).")
    print("=" * 95)


if __name__ == "__main__":
    consumer = ("APSPDCL-88421", "M. K. Satyanarayana", "MTR-2026-X9")
    readings = [
        ("January",   140, True),
        ("February",  165, True),
        ("March",     210, False),  # +27.3% spike!
        ("April",     380, True),   # +81.0% massive summer surge!
        ("May",       450, True),   # +18.4%
        ("June",      310, False),  # -31.1% drop
    ]
    history, analysis = analyze_multimonth_consumption(consumer, readings, spike_threshold_pct=25.0)
    print_electricity_report(consumer, history, analysis)
