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


def find_accessible_rolls(grid):
    """Find all '@' symbols that have fewer than 4 adjacent '@' symbols."""
    results = []

    # Iterate through each position in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_symbols(grid, row, col)
                if adjacent_count < 4:
                    results.append((row, col, adjacent_count))

    return results


def remove_accessible_rolls(filename):
    """Iteratively remove rolls that can be accessed by forklifts."""
    # Read the input file
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    total_removed = 0
    iteration = 0

    while True:
        iteration += 1
        # Find accessible rolls in current state
        accessible = find_accessible_rolls([''.join(row) for row in grid])

        if not accessible:
            print(f"\nStopped after {iteration - 1} iterations")
            break

        # Remove accessible rolls
        for row, col, _ in accessible:
            grid[row][col] = '.'

        total_removed += len(accessible)
        print(f"Iteration {iteration}: Removed {len(accessible)} rolls (total: {total_removed})")

    return total_removed


if __name__ == "__main__":
    filename = "2025/day4/input.txt"

    # Part 1: Count accessible rolls in initial state
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    results = find_accessible_rolls(grid)
    print("=== Part 1 ===")
    if results:
        from collections import Counter
        count_distribution = Counter([count for _, _, count in results])
        print(f"Distribution of adjacent counts: {dict(count_distribution)}")
        print(f"Total accessible rolls (fewer than 4 adjacent): {len(results)}")

    # Part 2: Iteratively remove accessible rolls
    print("\n=== Part 2 ===")
    total_removed = remove_accessible_rolls(filename)
    print(f"\nTotal rolls removed: {total_removed}")