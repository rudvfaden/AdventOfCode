
with open('2024/day4/input.txt') as file:
    data = file.read()

# row
input = [list(line) for line in data.strip().split('\n')]


def xmas_check(grid: list):
    n = len(grid)
    count = 0
    for c in range(n):
        for r in range(n):

            if 0 <= r-1 < n and 0 <= r+1 < n and 0 <= c-1 < n and 0 <= c+1 < n:
                top_left_bottom = str(grid[r-1][c-1]+grid[r][c]+grid[r+1][c+1])
                bottom_left_top = str(grid[r-1][c+1]+grid[r][c]+grid[r+1][c-1])
                if (top_left_bottom in ['MAS', 'SAM']) and (bottom_left_top in ['MAS', 'SAM']):
                    count += 1
    return count


print(xmas_check(input))
