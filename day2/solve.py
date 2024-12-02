import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()
reports = input.split("\n")

# part 1
safes = 0
for report in reports:
    levels = report.split(" ")
    decreasing = all(1 <= (int(earlier) - int(later)) <= 3 for earlier, later in zip(levels, levels[1:]))
    increasing = all(1 <= (int(later) - int(earlier)) <= 3 for earlier, later in zip(levels, levels[1:]))
    if increasing ^ decreasing: safes += 1 

print(safes, len(reports))


# part 2
safes = 0
for report in reports:
    levels = report.split(" ")
    for i in range(len(levels)):
        levels_removed = levels[:i] + levels[i+1 :]
        decreasing = all(1 <= (int(earlier) - int(later)) <= 3 for earlier, later in zip(levels_removed, levels_removed[1:]))
        increasing = all(1 <= (int(later) - int(earlier)) <= 3 for earlier, later in zip(levels_removed, levels_removed[1:]))
        if increasing ^ decreasing:
            safes += 1
            break


print(safes, len(reports))