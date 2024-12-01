import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

rows = input.split("\n")
list1, list2 = [], []
for row in rows[:-1]:
    entries = row.split("   ")
    list1.append(int(entries[0]))
    list2.append(int(entries[1]))

### part 1
        
list1, list2 = np.array(sorted(list1)), np.array(sorted(list2))
dist_sum = np.sum(np.abs(list1-list2))
print(dist_sum)

### part 2
simscore = np.sum([(list2 == num) * num for num in list1])
print(simscore)