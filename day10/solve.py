import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()


grid = [list(row) for row in input.split("\n") if row]
print(grid)

dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]

def is_out_of_bounds(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

# part 1

def travel(row, col, num, visited):
    if is_out_of_bounds(grid, row, col) or grid[row][col] != str(num): return 0
    if grid[row][col] == "9" and (row, col) not in visited:
        visited.add((row, col))
        return 1
        
    trails = 0
    for dir in dirs:
        trails += travel(row+dir[0], col+dir[1], num+1, visited)
    return trails


sum_of_scores = 0
for row in range(len(grid)):
    print(row, len(grid))
    for col in range(len(grid[row])):
        if grid[row][col] == "0":
            visited = set()
            for dir in dirs:
                sum_of_scores += travel(row+dir[0], col+dir[1], 1, visited)

print(sum_of_scores)

# part 2

def travel(row, col, num):
    if is_out_of_bounds(grid, row, col) or grid[row][col] != str(num): return 0
    if grid[row][col] == "9": return 1
    
    trails = 0
    for dir in dirs:
        trails += travel(row+dir[0], col+dir[1], num+1)
    return trails


sum_of_scores = 0
for row in range(len(grid)):
    print(row, len(grid))
    for col in range(len(grid[row])):
        if grid[row][col] == "0":
            visited = set()
            for dir in dirs:
                sum_of_scores += travel(row+dir[0], col+dir[1], 1)

print(sum_of_scores)