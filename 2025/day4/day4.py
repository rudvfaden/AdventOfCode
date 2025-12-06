from pathlib import Path
from typing import List, Tuple

TARGET_CHAR = '@'

def count_adjacent_target_symbols(grid: List[str], row: int, col: int) -> int:
    """Count the number of target symbols in the 8 adjacent positions."""
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
            if grid[new_row][new_col] == TARGET_CHAR:
                count += 1

    return count


def find_targets_with_fewer_than_eight_adjacent(file_path: Path) -> Tuple[List[Tuple[int, int, int]], List[str]]:
    """Find all target symbols that have fewer than 8 adjacent target symbols."""
    # Read the input file
    with file_path.open('r') as f:
        grid = [line.strip() for line in f.readlines()]

    results = []

    # Iterate through each position in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == TARGET_CHAR:
                adjacent_count = count_adjacent_target_symbols(grid, row, col)
                if adjacent_count < 8:
                    results.append((row, col, adjacent_count))

    return results, grid


if __name__ == "__main__":
    # Use pathlib to resolve the input file path relative to this script
    input_file = Path(__file__).parent / "input.txt"
    
    if not input_file.exists():
        print(f"Error: Input file not found at {input_file}")
    else:
        results, grid = find_targets_with_fewer_than_eight_adjacent(input_file)

        # Show some statistics
        if results:
            from collections import Counter
            count_distribution = Counter([count for _, _, count in results])
            total_less_than_4 = sum(v for k,v in count_distribution.items() if k < 4)
            print(f"\nTotal positions with fewer than 4 adjacent '{TARGET_CHAR}' symbols: {total_less_than_4}")