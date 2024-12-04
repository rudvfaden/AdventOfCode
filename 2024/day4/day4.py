
with open('2024/day4/input.txt') as file:
    data = file.read()

# row
input = [list(line) for line in data.strip().split('\n')]
count = 0
for row in input:
    count += ''.join(row).count('XMAS')
    count += ''.join(row).count('SAMX')

# col
num_cols = len(input[0])
col_tran = []
for col in range(num_cols):
    col_tran = []
    for row in input:
        col_tran.append(row[col])
    col_t = ''.join(col_tran)
    count += ''.join(col_t).count('XMAS')
    count += ''.join(col_t).count('SAMX')

# diagonal


def diagnonal_bottom_left_to_top(grid: list):
    n = len(grid)
    count = 0
    for d in range(2*n-1):  # der er n-1 diagonaler på hver side + midten
        diag_bottom_left_total_row = []  # iniziner idag for hver diagonal
        for i in range(n):  # loop over diagonalen
            bottom_row_start = (n-1) - d + i  # finder start koordinat
            if 0 <= bottom_row_start < n:  # sikre vi starter ny list efter end diagonal
                diag_bottom_left_total_row.append(grid[bottom_row_start][i])
        diag_bottom_left_total_row_str = ''.join(diag_bottom_left_total_row)
        count += diag_bottom_left_total_row_str.count('XMAS')
        count += diag_bottom_left_total_row_str.count('SAMX')
    return count


count += diagnonal_bottom_left_to_top(input)


def diagnonal_bottom_rigth_to_bottom(grid: list):
    n = len(grid)
    count = 0
    for d in range(2*n-1):  # der er n-1 diagonaler på hver side + midten
        diag_top_right_total_row = []  # iniziner idag for hver diagonal
        for i in range(n):  # loop over diagonalen
            bottom_row_start = d - i  # finder start koordinat
            if 0 <= bottom_row_start < n:  # sikre vi starter ny list efter end diagonal
                diag_top_right_total_row.append(grid[bottom_row_start][i])
        diag_top_right_total_row_str = ''.join(diag_top_right_total_row)
        count += diag_top_right_total_row_str.count('XMAS')
        count += diag_top_right_total_row_str.count('SAMX')
    return count


count += diagnonal_bottom_rigth_to_bottom(input)
print(count)
