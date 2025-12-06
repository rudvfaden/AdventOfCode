
from pathlib import Path
import re

input_path = Path(__file__).parent / "input.txt"
ingredient_range = [line.strip() for line in input_path.read_text().splitlines() if '-' in line]
ingredient = [line.strip() for line in input_path.read_text().splitlines() if '-' not in line and line.strip() != '']


def check_ingridient(ingridient: list, ingridient_range: list) -> set:
    
    fresh_ingridient = set()
    for i in range(len(ingridient_range)):
        ingridient_range_split = ingridient_range[i].split('-')
        ingridient_range_start = int(ingridient_range_split[0])
        ingridient_range_end = int(ingridient_range_split[1])

        for j in range(len(ingridient)):
           # print(ingridient[j], ingridient_range_start, ingridient_range_end, int(ingridient[j]) >= ingridient_range_start and int(ingridient[j]) <= ingridient_range_end)
            if int(ingridient[j]) >= ingridient_range_start and int(ingridient[j]) <= ingridient_range_end:
                fresh_ingridient.add(ingridient[j])
    
    return fresh_ingridient


print(len(check_ingridient(ingredient, ingredient_range)))


def fresh_ingridient_id(ingridient_range: list) -> int:
    # Parse all ranges into (start, end) tuples
    ranges = []
    for range_str in ingridient_range:
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))

    # Sort ranges by start position
    ranges.sort()

    # Merge overlapping ranges and count total unique numbers
    if not ranges:
        return 0

    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        # If current range overlaps or touches the last merged range
        if start <= last_end + 1:
            # Extend the last merged range
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))

    # Count total numbers in all merged ranges
    total = sum(end - start + 1 for start, end in merged)
    return total

print(fresh_ingridient_id(ingredient_range))