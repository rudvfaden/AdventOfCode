from itertools import product

test_values = []
numbers = []

with open("2024/day7/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split(': ')
        test_values.append(int(parts[0]))
        number = [int(num) for num in parts[1].split()]
        numbers.append(number)


def evalueate(numbers: list, operations: list) -> int:
    result = numbers[0]
    for i, operation in enumerate(operations):
        if operation == '+':
            result += numbers[i + 1]
        elif operation == '*':
            result *= numbers[i + 1]
        elif operation == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result


sum_result = 0
for test_value, number in zip(test_values, numbers):
    operation_combinations = product('+*', repeat=len(number) - 1)
    for operations in operation_combinations:
        result = evalueate(number, operations)
        # print(result, test_value, number, operations)
        if result == test_value:
            sum_result += test_value
            break

print('part1:', sum_result)

sum_result = 0
for test_value, number in zip(test_values, numbers):
    operation_combinations = product('+*|', repeat=len(number) - 1)
    for operations in operation_combinations:
        result = evalueate(number, operations)
        # print(result, test_value, number, operations)
        if result == test_value:
            sum_result += test_value
            break

print('part2:', sum_result)
