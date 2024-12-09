import os
import copy

ROTATIONS = {'<': '^', '^': '>', '>': 'v', 'v': '<'}
MAX_ITERATIONS = 20000  

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input_data = f.read()

original_map = []
start_position = None
start_direction = None
for i, row in enumerate(input_data.splitlines()):
    if len(row.strip()) > 0:
        original_map.append(list(row))
        for j, char in enumerate(row):
            if char in ROTATIONS:
                start_position = (i, j)
                start_direction = char
                break

def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def is_obstacle(grid, row, col):
    return grid[row][col] == "#"

def simulate(grid, start_row, start_col, direction):
    iteration_count = 0
    tmp_map = copy.deepcopy(grid)
    row, col = start_row, start_col

    while True:
        grid[row][col] = "X"  
        if direction == "<":
            next_row, next_col = row, col - 1
        elif direction == ">":
            next_row, next_col = row, col + 1
        elif direction == "v":
            next_row, next_col = row + 1, col
        elif direction == "^":
            next_row, next_col = row - 1, col

        if is_out_of_bounds(grid, next_row, next_col):
            break
        if is_obstacle(grid, next_row, next_col):
            direction = ROTATIONS[direction]  
        else:
            row, col = next_row, next_col  

        iteration_count += 1
        if iteration_count == MAX_ITERATIONS:
            if tmp_map == grid:
                return None
            tmp_map = copy.deepcopy(grid)
            iteration_count = 0

    return grid

# part 1

start_row, start_col = start_position
simulation_map = copy.deepcopy(original_map)
result_map = simulate(simulation_map, start_row, start_col, start_direction)

marked_count = sum(row.count("X") for row in result_map)
print(marked_count)

# part 2

valid_pos = 0
for row_idx, row in enumerate(original_map):
    print(row_idx)
    for col_idx, cell in enumerate(row):
        if (row_idx, col_idx) == start_position or cell == "#":
            continue

        test_map = copy.deepcopy(original_map)
        test_map[row_idx][col_idx] = "#"
        simulation_result = simulate(test_map, start_row, start_col, start_direction)
        if simulation_result is None:
            valid_pos += 1

print(valid_pos)
