import os
import numpy as np
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()


positions = []
velocities = []
for row in input.split("\n"):
    row = row.replace("p=", "").replace("v=", "").split(" ")
    if len(row) < 2: continue
    positions.append([int(i) for i in row[0].split(",")])
    velocities.append([int(i) for i in row[1].split(",")])


# part 1
quadrants = [0,0,0,0]

for i in range(len(positions)):
    pos = positions[i]
    velocity = velocities[i]

    pos[0] += 100 * velocity[0]
    pos[1] += 100 * velocity[1]
    
    pos[0] = pos[0] % 101
    pos[1] = pos[1] % 103
    x, y = pos[0], pos[1]

    
    print(pos)
    if x == 50 or y == 51:
        continue

    if x < 50:
        if y < 51:
            quadrants[0] += 1
        else:
            quadrants[1] += 1
    else:  # x > 50
        if y < 51:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])

# part 2

def compute_entropy(points, x_bins=101, y_bins=103):
    """
    Compute the Shannon entropy of a 2D point distribution.
    
    points: List of (x, y) tuples.
    x_bins, y_bins: Number of bins along each dimension. 
                    Adjust based on your coordinate system and data.
    """
    # Extract x, y coordinates
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    # Create 2D histogram of points
    # Assuming coordinates already wrapped to [0, x_bins) and [0, y_bins)
    # If not, consider passing in proper range like range=[[0, x_bins],[0, y_bins]]
    H, xedges, yedges = np.histogram2d(xs, ys, bins=[x_bins, y_bins], range=[[0, x_bins],[0, y_bins]])

    # Convert counts to probabilities
    total_points = np.sum(H)
    if total_points == 0:
        # No points, no entropy
        return 0.0
    
    # Flatten histogram into probabilities
    p = H.flatten() / total_points
    
    # Compute entropy: sum of p_i * log(p_i)
    # We only sum over nonzero p to avoid log(0)
    p_nonzero = p[p > 0]
    entropy = -np.sum(p_nonzero * np.log2(p_nonzero))
    
    return entropy


def draw_grid(curr_positions, j):
    width, height = 101, 103  # from the modulo used in the code
    # Create a blank grid
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Place each robot
    for (x, y) in curr_positions:
        # Make sure indices are integers
        x = int(x)
        y = int(y)
        grid[y][x] = '#'

    ret = ""
    for row in grid:
        ret += "".join(row)

    if "#####################" in ret:
        print(j)
    
        # Print the grid row by row
        # Note: if you want y=0 at the bottom, print in reverse order: for row in reversed(grid):
        for row in grid:
            print("".join(row))
        print("------------------------------------")


positions = []
velocities = []
for row in input.split("\n"):
    row = row.replace("p=", "").replace("v=", "").split(" ")
    if len(row) < 2: continue
    positions.append([int(i) for i in row[0].split(",")])
    velocities.append([int(i) for i in row[1].split(",")])


curr_positions = []

for j in range(10000):
    curr_positions = []
    for i in range(len(positions)):
        pos = positions[i]
        velocity = velocities[i]

        pos[0] += 1 * velocity[0]
        pos[1] += 1 * velocity[1]
        
        pos[0] = pos[0] % 101
        pos[1] = pos[1] % 103
        x, y = pos[0], pos[1]

        
        curr_positions.append([x, y])
    
    ret = draw_grid(curr_positions, j+1)

    


# 6886 too low
# 7401 too low