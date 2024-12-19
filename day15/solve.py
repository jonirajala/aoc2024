import os
import numpy as np


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()


def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


grid = [list(input.split("\n")[i]) for i in range(50) if input.split("\n")]
moves = [
    x
    for xs in input.split("\n")[51:]
    for x in xs
]

# grid = [list(input.split("\n")[i]) for i in range(11) if input.split("\n")]
# moves = [
#     x
#     for xs in input.split("\n")[10:]
#     for x in xs
# ]



# grid = [list(input.split("\n")[i]) for i in range(8) if input.split("\n")]
# moves = "<^^>>>vv<v>>v<<"


for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "@":
            pos = (row, col)
            break

ret = ""
for row in grid:
    ret += "".join(row)
for row in grid:
            print("".join(row))

print(moves)
dirs = {"^":(-1, 0), ">":(0, 1), "v":(1, 0), "<":(0, -1)}

for move in moves:
    # print(move)
    dir = dirs[move]

    if grid[pos[0]+dir[0]][pos[1]+dir[1]] == "#":
        continue
    if grid[pos[0]+dir[0]][pos[1]+dir[1]] == ".":
        grid[pos[0]][pos[1]] = "."
        pos = (pos[0]+dir[0], pos[1]+dir[1])
        grid[pos[0]][pos[1]] = "@"

    else:
        dist = 2
        wall = False
        while True:
            if grid[pos[0]+dir[0]*dist][pos[1]+dir[1]*dist] == "O": pass
            elif grid[pos[0]+dir[0]*dist][pos[1]+dir[1]*dist] == "#":
                wall = True
                break
            elif grid[pos[0]+dir[0]*dist][pos[1]+dir[1]*dist] == ".":
                 break

            dist += 1
        if not wall:
            grid[pos[0]+dir[0]][pos[1]+dir[1]] = "@"
            grid[pos[0]+dir[0]*dist][pos[1]+dir[1]*dist] = "O"
            grid[pos[0]][pos[1]] = "."
            pos = (pos[0]+dir[0], pos[1]+dir[1])


ret = ""
for row in grid:
    ret += "".join(row)
for row in grid:
            print("".join(row))


score = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "O":
            score += 100 * row + col

print(score)