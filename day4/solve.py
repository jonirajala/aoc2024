import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

# part 1
word = "XMAS"
grid = input.strip().split('\n')
grid = [list(row) for row in grid]

count = 0
rows = len(grid)
cols = len(grid[0])
word_len = len(word)
directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]

for i in range(rows):
    for j in range(cols):
        for dx, dy in directions:
            x, y = i, j
            for k in range(word_len):
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == word[k]:
                    x += dx
                    y += dy
                else:
                    break
            else:
                count += 1

print(count)

# part 2

count = 0
patterns = [['M', 'A', 'S'], ['S', 'A', 'M']]
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if grid[i][j] != 'A':
            continue
        d1 = [grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]]
        d2 = [grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]]
        if any(d1 == p or d1 == p[::-1] for p in patterns) and any(d2 == p or d2 == p[::-1] for p in patterns):
            count += 1

print(count)
