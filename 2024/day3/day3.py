import re

with open('2024/day3/input.txt') as file:
    instructions = file.read()

tokens = re.findall(r"mul\((\d+),(\d+)\)", instructions)

result = 0
for token in tokens:
    result += int(token[0])*int(token[1])

print(result)

mul_enabled = True

tokens = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", instructions)

result = 0
for token in tokens:
    if token == "do()":
        mul_enabled = True
    elif token == "don't()":
        mul_enabled = False
    elif mul_enabled and token.startswith("mul"):
        numbers = re.findall(r'\d+', token)
        result += int(numbers[0]) * int(numbers[1])

print(result)
