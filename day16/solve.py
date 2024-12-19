import os
import numpy as np


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()


def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


grid = [list(row) for row in input.split("\n") if row]

start_pos = ()
for row in range(len(grid)):
    for col in range(len(grid[row])):
        

