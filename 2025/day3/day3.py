from itertools import combinations

l = []
with open('2025/day3/input.txt') as f:
    for line in f:
        l.append(line.strip())

total = 0
for i in l:
    set_of_combinations ={int(''.join(pair)) for pair in combinations(i, 2)}
    total += max(set_of_combinations)

print(total)