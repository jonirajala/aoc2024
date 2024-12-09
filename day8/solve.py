import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

print(input)

grid = [list(row) for row in input.split("\n") if row]


# part 1

def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def find_antinode_locations(grid):
    antinode_locations = []

    for og_row in range(len(grid)):
        for og_col in range(len(grid[0])):
            current_val = grid[og_row][og_col]

            if current_val in [".", "#"]:
                continue

            for second_row in range(len(grid)):
                for second_col in range(len(grid[0])):
                    if (og_row, og_col) == (second_row, second_col):
                        continue
                    if grid[second_row][second_col] != current_val:
                        continue

                    row_dist = abs(og_row - second_row)
                    col_dist = abs(og_col - second_col)
                    is_up = og_row - second_row < 0
                    is_left = og_col - second_col < 0

                    new_row_1 = og_row - row_dist if is_up else og_row + row_dist
                    new_row_2 = second_row + row_dist if is_up else second_row - row_dist
                    new_col_1 = og_col - col_dist if is_left else og_col + col_dist
                    new_col_2 = second_col + col_dist if is_left else second_col - col_dist

                    for new_row, new_col in [(new_row_1, new_col_1), (new_row_2, new_col_2)]:
                        if not is_out_of_bounds(grid, new_row, new_col):
                            location = (new_row, new_col)
                            if location not in antinode_locations:
                                antinode_locations.append(location)

    return antinode_locations

antinode_locations = find_antinode_locations(grid)
print(len(antinode_locations))

# part 2

def find_antinode_locations(grid):
    antinode_locations = []

    for og_row in range(len(grid)):
        for og_col in range(len(grid[0])):
            current_val = grid[og_row][og_col]

            if current_val in [".", "#"]:
                continue

            for second_row in range(len(grid)):
                for second_col in range(len(grid[0])):
                    if (og_row, og_col) == (second_row, second_col):
                        continue
                    if grid[second_row][second_col] != current_val:
                        continue

                    row_dist = abs(og_row - second_row)
                    col_dist = abs(og_col - second_col)
                    is_up = og_row - second_row < 0
                    is_left = og_col - second_col < 0

                    i = 0
                    while i < 100:
                        new_row_1 = og_row - row_dist*i if is_up else og_row + row_dist*i
                        new_row_2 = second_row + row_dist*i if is_up else second_row - row_dist*i
                        new_col_1 = og_col - col_dist*i if is_left else og_col + col_dist*i
                        new_col_2 = second_col + col_dist*i if is_left else second_col - col_dist*i

                        for new_row, new_col in [(new_row_1, new_col_1), (new_row_2, new_col_2)]:
                            if not is_out_of_bounds(grid, new_row, new_col):
                                location = (new_row, new_col)
                                if location not in antinode_locations:
                                    antinode_locations.append(location)
                        i += 1


    return antinode_locations

antinode_locations = find_antinode_locations(grid)
print(len(antinode_locations))

