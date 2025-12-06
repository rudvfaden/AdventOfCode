from itertools import zip_longest
import math

# Part 1: Read as normal (split by whitespace)
math_problem_part1 = [line.strip().split() for line in open("2025/day6/input.txt").readlines()]
math_problem_transpose_part1 = list(zip_longest(*math_problem_part1))

def solve_math_problem(math_problem: tuple) -> int:
    result = 0
    if '+' in math_problem:
        result = sum([int(j) for j in math_problem if j != '+'])
    elif '*' in math_problem:
        result = math.prod([int(j) for j in math_problem if j != '*'])
    else:
        result = 0
    return result

total = 0
for problem in math_problem_transpose_part1:
    total += solve_math_problem(problem)

print(f"Part 1: {total}")

# Part 2: Cephalopod math (vertical columns, right-to-left)
def parse_cephalopod_worksheet(lines):
    """Parse the worksheet by finding column separators and extracting problems"""
    # Remove empty lines and strip newlines, get number rows (all except last which has operators)
    clean_lines = [line.rstrip('\n') for line in lines if line.strip()]
    number_lines = clean_lines[:-1]
    operator_line = clean_lines[-1]

    # Pad all lines to same length
    max_len = max(len(line) for line in number_lines + [operator_line])
    padded_numbers = [line.ljust(max_len) for line in number_lines]
    padded_operator = operator_line.ljust(max_len)

    # Find column separators (all spaces in number rows)
    separators = []
    for pos in range(max_len):
        if all(line[pos] == ' ' for line in padded_numbers):
            separators.append(pos)

    # Split into problem sections
    problems = []
    start = 0
    for sep in separators + [max_len]:
        if start < sep:
            # Extract this problem section
            problem_chars = []
            for line in padded_numbers:
                problem_chars.append(line[start:sep])
            operator = padded_operator[start:sep].strip()
            if operator:
                problems.append((problem_chars, operator))
        start = sep + 1

    return problems


def extract_numbers_from_cephalopod_section(number_rows, operator):
    """Extract numbers from a problem section reading right-to-left"""
    if not number_rows or not number_rows[0]:
        return [], operator

    section_len = len(number_rows[0])
    numbers = []

    # Read each character position right-to-left
    for col_idx in range(section_len - 1, -1, -1):
        digit_string = ""
        # Read top to bottom at this position
        for row in number_rows:
            if col_idx < len(row) and row[col_idx] != ' ':
                digit_string += row[col_idx]

        # If we collected any digits, convert to number
        if digit_string:
            numbers.append(int(digit_string))

    return numbers, operator


def solve_cephalopod_problem(number_rows, operator):
    """Solve a single cephalopod math problem"""
    numbers, op = extract_numbers_from_cephalopod_section(number_rows, operator)

    if not numbers:
        return 0

    if op == '+':
        return sum(numbers)
    elif op == '*':
        return math.prod(numbers)
    else:
        return 0


# Parse and solve Part 2
lines = open("2025/day6/input.txt").readlines()
problems = parse_cephalopod_worksheet(lines)

total_cephalopod = 0
for number_rows, operator in problems:
    result = solve_cephalopod_problem(number_rows, operator)
    total_cephalopod += result

print(f"Part 2: {total_cephalopod}")