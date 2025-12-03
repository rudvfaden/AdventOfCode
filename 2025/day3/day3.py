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


def max_number_from_digits(s: str, k: int) -> int:
    """Return the maximum integer obtainable by selecting k digits from s
    while preserving their relative order. Uses a monotonic stack in O(n).
    """
    n = len(s)
    if k >= n:
        return int(s)

    remove = n - k  # how many digits we can drop
    stack = []
    for ch in s:
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    if remove > 0:  # still need to drop from the end
        stack = stack[:-remove]

    return int(''.join(stack[:k]))


total = 0
K = 12
for i in l:
    total += max_number_from_digits(i, K)

print(total)