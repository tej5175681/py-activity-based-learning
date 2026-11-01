"""
Case Study 04: Advanced Numeric Pattern Generator
=================================================
Syllabus Concepts Used:
- Variables, Data Types, and Type Conversion
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops (for within for, while loops)
- String Manipulation and Character Formatting
- Lists for Row Buffering and Validation

Description:
Produces complex mathematical numerical patterns:
Pattern 1: Hollow Symmetric Number Diamond
  - Dimension must be an odd positive integer between 3 and 19.
  - Validates dimension constraints.
  - Outer border and inner diagonal boundaries populated with row-dependent numbers,
    with precisely calculated hollow whitespace.

Pattern 2: Symmetric Palindromic Number Pyramid
  - Each level i displays numbers counting up to i and back down to 1.
  - Fully centered with dynamic whitespace padding.
"""

def validate_dimension(dim_input):
    """
    Validates user input dimension:
    - Must be convertable to positive integer
    - Must be an odd number
    - Must fall between 3 and 19 inclusive
    Returns tuple: (is_valid, dimension_or_none, error_message)
    """
    try:
        dim = int(dim_input)
    except (ValueError, TypeError):
        return (False, None, "Invalid input: Dimension must be an integer.")

    if dim < 3 or dim > 19:
        return (False, None, f"Out of bounds: Dimension {dim} must be between 3 and 19.")

    if dim % 2 == 0:
        return (False, None, f"Invalid parity: Dimension {dim} is even; hollow diamonds require an odd dimension.")

    return (True, dim, "Dimension is valid.")


def generate_hollow_numeric_diamond(n):
    """
    Generates lines of a hollow numerical diamond of odd dimension n.
    Returns list of formatted strings.
    """
    lines = []
    mid = n // 2  # Zero-indexed middle row

    for i in range(n):
        row_str = ""
        # Distance from middle row
        if i <= mid:
            dist = mid - i
            row_num = i + 1
        else:
            dist = i - mid
            row_num = n - i

        leading_spaces = dist * 2
        row_str += " " * leading_spaces

        # Number of positions between outer numbers
        inner_gap = (n - 2 * dist - 2) * 2

        if dist == mid:
            # Tip of the diamond (top and bottom single vertex)
            row_str += str(row_num)
        else:
            # Left number
            row_str += str(row_num) + " "
            # Inner hollow spaces
            row_str += " " * (inner_gap - 1)
            # Right number
            row_str += str(row_num)

        lines.append(row_str)

    return lines


def generate_palindromic_number_pyramid(height):
    """
    Generates a centered palindromic numerical pyramid of specified height.
    Row i: 1 2 ... i ... 2 1
    """
    lines = []
    for i in range(1, height + 1):
        # Build numbers: up to i, then back to 1
        nums = []
        for j in range(1, i + 1):
            nums.append(str(j))
        for j in range(i - 1, 0, -1):
            nums.append(str(j))

        # Join numbers with single space
        num_str = " ".join(nums)

        # Center align with leading spaces
        leading = (height - i) * 2
        line = (" " * leading) + num_str
        lines.append(line)

    return lines


def print_patterns(dim):
    is_valid, n, msg = validate_dimension(dim)
    print("=" * 70)
    print("              ADVANCED NUMERIC PATTERN GENERATOR")
    print("=" * 70)
    print(f"Requested Dimension : {dim}")
    print(f"Validation Status   : {'SUCCESS' if is_valid else 'FAILED'}")
    print(f"Audit Feedback      : {msg}")
    print("-" * 70)

    if not is_valid:
        print("[!] Cannot render pattern due to validation errors.\n")
        return

    print(f"\n[PATTERN 1: HOLLOW SYMMETRIC NUMERICAL DIAMOND (N = {n})]")
    diamond_lines = generate_hollow_numeric_diamond(n)
    for line in diamond_lines:
        print(line)

    pyramid_height = (n // 2) + 1
    print(f"\n[PATTERN 2: SYMMETRIC PALINDROMIC PYRAMID (Height = {pyramid_height})]")
    pyramid_lines = generate_palindromic_number_pyramid(pyramid_height)
    for line in pyramid_lines:
        print(line)
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # Test sample with valid odd dimension
    print_patterns(9)
