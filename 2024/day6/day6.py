with open("2024/day6/input.txt", "r") as file:
    data = file.read()

input = [line.strip() for line in data.strip().split("\n")]


def patrol(grid):
    # op, højre, ned, venstre
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_indices = {"^": 0, ">": 1, "v": 2, "<": 3}

    num_rows = len(grid)
    num_cols = len(grid[0]) - 1

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char in dir_indices:
                guard_x, guard_y = i, j
                cur_dir = dir_indices[char]
                break

    visited = {(guard_x, guard_y)}

    new_x, new_y = guard_x, guard_y
    while 0 < new_x < num_rows - 1 and 0 < guard_y < num_cols - 1:
        dx, dy = directions[cur_dir]
        new_x, new_y = guard_x + dx, guard_y + dy
        if grid[new_x][new_y] != "#":
            new_x, new_y = guard_x + dx, guard_y + dy
            guard_x, guard_y = new_x, new_y
            visited.add((guard_x, guard_y))
        else:
            # drej til venstre
            cur_dir = (cur_dir + 1) % 4
    print(len(visited))


patrol(input)
