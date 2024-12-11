

# from read_aoc_data import read_aoc_data

# data = read_aoc_data()
# input = [list(line) for line in data.split('\n')]

from collections import defaultdict
from itertools import permutations

data = defaultdict(list)
input = [line.strip() for line in open('2024/day8/input.txt')]
max_r, max_c = len(input), len(input[0])
antinodes = set()

# finder alle værdier og gemmer dem i en dictionary
for r, l in enumerate(input):
    for c, s in enumerate(l):
        if s != '.':
            data[s].append((r, c))

# finder alle antinodes
for v in data.values():
    for (x1, y1), (x2, y2) in permutations(v, 2):
        dx, dy = x2 - x1, y2 - y1
        antinodes.add((x1-dx, y1-dy))
        antinodes.add((x2+dx, y2+dy))

# tjekker antal antinodes der ligger inden for koret
print(
    len({(x, y) for (x, y) in antinodes if 0 <= x < max_r and 0 <= y < max_c})
    )
