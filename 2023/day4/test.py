from collections import deque

# Part 1
data = [[set([int(s) for s in n.split()]) for n in l.strip().split(":")[1].split("|")] for l in open("2023/day4/input.txt")]  # fmt: skip

winning_sets = {i: len(s1 & s2) for i, (s1, s2) in enumerate(data, 1)}
winning_numbers = [1 * 2 ** (s - 1) for s in winning_sets.values() if s > 0]
print(sum(winning_numbers))

# Part 2
q = deque(winning_sets.keys())