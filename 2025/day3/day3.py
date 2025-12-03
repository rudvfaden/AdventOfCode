from itertools import combinations

# source digits
l = list('811111111111119')

# produce all 2-combinations and convert each tuple of chars into a concatenated int
# use a set to keep only distinct values, then sort for deterministic output
print(max(sorted({int(''.join(pair)) for pair in combinations(l, 2)})))