def count_adjacent_at_symbols(grid, row, col):
    """Count the number of '@' symbols in the 8 adjacent positions."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define the 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1

    return count


def find_at_with_fewer_than_eight_adjacent(filename):
    """Find all '@' symbols that have fewer than 8 adjacent '@' symbols."""
    # Read the input file
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    results = []

    # Iterate through each position in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_symbols(grid, row, col)
                if adjacent_count < 8:
                    results.append((row, col, adjacent_count))

    return results, grid


if __name__ == "__main__":
    filename = "2025/day4/input.txt"
    results, grid = find_at_with_fewer_than_eight_adjacent(filename)

    # Show some statistics
    if results:
        from collections import Counter
        count_distribution = Counter([count for _, _, count in results])
        total_less_than_4 = sum(v for k,v in count_distribution.items() if k<4)
        print(f"\nTotal positions with fewer than 4 adjacent '@' symbols: {total_less_than_4}")