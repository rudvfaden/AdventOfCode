
data = [list(line.strip()) for line in open("2025/day7/input.txt").readlines()]

# Find starting position 'S' in first row
current_positions = [data[0].index('S')]
split_count = 0

# Trace through each row
for row_idx in range(1, len(data)):
    row = data[row_idx]
    next_positions = []

    for pos in current_positions:
        # Check if there's a '^' at current position
        if row[pos] == '^':
            # Count this split
            split_count += 1
            # Add left and right positions
            next_positions.append(pos - 1)
            next_positions.append(pos + 1)
        elif row[pos] == '.':
            # Continue straight down through empty space
            next_positions.append(pos)

    # Remove duplicates and update current positions
    current_positions = list(set(next_positions))

    # Stop if no more positions to trace
    if not current_positions:
        break

print(f"Total splits: {split_count}")

