"""
Case Study 05: Student Email and Registration Identifier Validation Engine
==========================================================================
Syllabus Concepts Used:
- Strings (indexing, slicing, character iteration, traversal)
- String Methods (split, count, startswith, endswith, isalpha, isdigit, isalnum)
- Variables, Data Types (str, bool, list, tuple)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Loops (for, while)
- Lists and Tuples (accumulating error messages, unpacking)
- String Formatting

Description:
Validates institutional email addresses and university student registration identifiers
WITHOUT using regular expressions (re module). Implements rigorous deterministic
string-parsing automata to detect:
- Malformed or misplaced separators (@, ., -)
- Missing prefix or suffix components
- Invalid character categories (symbols where letters/digits required)
- Invalid branch codes and year ranges
"""

VALID_BRANCHES = ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT", "CSM", "CSD"]
VALID_SECTIONS = ["A", "B", "C", "D"]
EXPECTED_DOMAIN = "student.rvrnriit.edu.in"

def validate_student_email(email_str):
    """
    Validates institutional student email format:
    <roll_number>.<student_name>@student.rvrnriit.edu.in
    Returns tuple: (is_valid, extracted_info_tuple, errors_list)
    """
    errors = []
    email = email_str.strip()

    # Rule 1: Whitespace check
    for ch in email:
        if ch == " " or ch == "\t" or ch == "\n":
            errors.append("Email contains illegal whitespace characters.")
            break

    # Rule 2: Exactly one '@' symbol
    at_count = email.count("@")
    if at_count == 0:
        errors.append("Missing '@' separator.")
        return (False, None, errors)
    elif at_count > 1:
        errors.append(f"Multiple '@' separators detected ({at_count} found).")
        return (False, None, errors)

    # Split into local part and domain part
    parts = email.split("@")
    local_part = parts[0]
    domain_part = parts[1]

    # Rule 3: Domain validation
    if domain_part.lower() != EXPECTED_DOMAIN:
        errors.append(f"Invalid domain '{domain_part}'; expected exactly '{EXPECTED_DOMAIN}'.")

    # Rule 4: Local part dot check
    dot_count = local_part.count(".")
    if dot_count == 0:
        errors.append("Missing dot '.' separator in local part; expected format <roll_number>.<name>.")
        return (False, None, errors)
    elif dot_count > 1:
        errors.append(f"Malformed separators: local part contains {dot_count} dots (expected exactly 1).")
        return (False, None, errors)

    local_tokens = local_part.split(".")
    roll_token = local_tokens[0]
    name_token = local_tokens[1]

    # Rule 5: Roll Number in Email (must be 10 alphanumeric chars, e.g., 26B91A0501)
    if len(roll_token) != 10:
        errors.append(f"Roll number token '{roll_token}' has invalid length {len(roll_token)} (must be 10 characters).")
    else:
        if not roll_token.isalnum():
            errors.append(f"Roll number token '{roll_token}' must contain only alphanumeric characters.")

    # Rule 6: Name Token in Email (must be alphabetical, 2 to 30 chars)
    if len(name_token) < 2 or len(name_token) > 30:
        errors.append(f"Student name token '{name_token}' length must be between 2 and 30 characters.")
    if not name_token.isalpha():
        errors.append(f"Student name token '{name_token}' contains invalid non-alphabetic characters.")

    is_valid = (len(errors) == 0)
    info = (roll_token.upper(), name_token.capitalize(), domain_part.lower()) if is_valid else None
    return (is_valid, info, errors)


def validate_registration_identifier(reg_id_str):
    """
    Validates student registration identifier with format:
    YY-BRANCH-SEC-ROLL (e.g. '26-CSE-A-0501')
    Returns tuple: (is_valid, extracted_info_tuple, errors_list)
    """
    errors = []
    reg_id = reg_id_str.strip()

    # Separator check
    if "-" not in reg_id:
        errors.append("Malformed separator: Missing hyphen '-' delimiters.")
        return (False, None, errors)

    tokens = reg_id.split("-")
    if len(tokens) != 4:
        errors.append(f"Structural error: Expected 4 hyphen-delimited tokens, found {len(tokens)}.")
        return (False, None, errors)

    year_tok, branch_tok, sec_tok, roll_tok = tokens

    # 1. Year Validation (2 digits)
    if len(year_tok) != 2 or not year_tok.isdigit():
        errors.append(f"Invalid admission year token '{year_tok}'; must be a 2-digit number (e.g., '26').")
    else:
        yr_val = int(year_tok)
        if yr_val < 20 or yr_val > 30:
            errors.append(f"Admission year '{year_tok}' is outside allowed range (20 to 30).")

    # 2. Branch Validation
    branch_clean = branch_tok.upper()
    if branch_clean not in VALID_BRANCHES:
        errors.append(f"Invalid branch code '{branch_tok}'; permitted branches: {', '.join(VALID_BRANCHES)}.")

    # 3. Section Validation
    sec_clean = sec_tok.upper()
    if sec_clean not in VALID_SECTIONS:
        errors.append(f"Invalid section code '{sec_tok}'; permitted sections: {', '.join(VALID_SECTIONS)}.")

    # 4. Roll sequence number (4 digits)
    if len(roll_tok) != 4 or not roll_tok.isdigit():
        errors.append(f"Invalid roll sequence '{roll_tok}'; must be exactly 4 numeric digits (e.g., '0501').")

    is_valid = (len(errors) == 0)
    info = (year_tok, branch_clean, sec_clean, roll_tok) if is_valid else None
    return (is_valid, info, errors)


def audit_student_credentials(records):
    """
    records: List of tuples (email, registration_id)
    """
    results = []
    for email, reg_id in records:
        e_valid, e_info, e_err = validate_student_email(email)
        r_valid, r_info, r_err = validate_registration_identifier(reg_id)
        overall_valid = e_valid and r_valid
        results.append((email, reg_id, overall_valid, e_valid, e_info, e_err, r_valid, r_info, r_err))
    return results


def print_audit_report(results):
    print("=" * 115)
    print("                      DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("             STUDENT EMAIL & REGISTRATION IDENTIFIER VALIDATION REPORT")
    print("=" * 115)
    print(f"{'Email Identifier':<46}{'Registration ID':<18}{'Email Val':<12}{'Reg ID Val':<12}{'Verdict'}")
    print("-" * 115)

    passed_count = 0
    for row in results:
        email, reg_id, overall, ev, einfo, eerr, rv, rinfo, rerr = row
        if overall:
            passed_count += 1
        e_status = "VALID" if ev else "INVALID"
        r_status = "VALID" if rv else "INVALID"
        verdict = "APPROVED" if overall else "REJECTED"
        print(f"{email:<46}{reg_id:<18}{e_status:<12}{r_status:<12}{verdict}")

    print("-" * 115)
    print(f"Summary: Total Audited = {len(results)} | Approved = {passed_count} | Rejected = {len(results) - passed_count}")

    print("\n[ITEMIZED ERROR AUDIT LOG FOR REJECTED ENTRIES]")
    print("-" * 115)
    for row in results:
        email, reg_id, overall, ev, einfo, eerr, rv, rinfo, rerr = row
        if not overall:
            print(f"> Target: {email} | {reg_id}")
            if not ev:
                for err in eerr:
                    print(f"    [Email Defect] {err}")
            if not rv:
                for err in rerr:
                    print(f"    [Reg ID Defect] {err}")
            print("-" * 115)
    print("=" * 115)


if __name__ == "__main__":
    test_data = [
        ("26B91A0501.manikanta@student.rvrnriit.edu.in", "26-CSE-A-0501"),  # Valid
        ("26B91A0502.bhavya@student.rvrnriit.edu.in",    "26-ECE-B-0412"),  # Valid
        ("26B91A0503.suresh#kumar@gmail.com",            "26-XYZ-A-0101"),  # Wrong domain, # in name, wrong branch
        ("invalid_email_format",                         "26-CSE-A-12"),    # No @, short roll
        ("26B91A0505..rajesh@student.rvrnriit.edu.in",   "26-IT-Z-0505"),   # Double dot, invalid section Z
        ("26B91A0506.ananya@student.rvrnriit.edu.in",    "26-MECH-C-0301"), # Valid
    ]
    audit_results = audit_student_credentials(test_data)
    print_audit_report(audit_results)
