import os
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

# part 1
    
grid = [list(row) for row in input.split("\n") if row]


def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

price = 0
seen = []
for row in range(len(grid)):
    print(row, len(grid))
    for col in range(len(grid[row])):
        friends = []
        tot = [1]
        def traverse(row, col, region):
            if is_out_of_bounds(grid, row, col) or  grid[row][col] != region or [row, col] in seen: return 0

            seen.append([row, col])
            tot.append(1)
            fr = 0
            for dir in dirs:
                if [row+dir[0], col+dir[1]] in seen and grid[row+dir[0]][col+dir[1]] == region:
                    fr += 1
                traverse(row+dir[0], col+dir[1], region)
            friends.append(4-fr)


        # tot = 1
        fr = 0
        if [row, col] not in seen:
            for dir in dirs:
                if [row+dir[0], col+dir[1]] in seen and grid[row+dir[0]][col+dir[1]] == grid[row][col]:
                    fr += 1
                traverse(row+dir[0], col+dir[1], grid[row][col])
        
        friends.append(4-fr)
        
        
        price += sum(friends) * len(tot)

print(price)
