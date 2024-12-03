import re
import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

# part 1

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, input)
tot = sum([(int(num1) * int(num2)) for num1, num2 in matches])
print(tot)


# part 1
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"
matches = re.finditer(pattern, input)

tot = 0
do = True
for match in matches:
    if match.group(1) and match.group(2) and do:
        tot += int(match.group(1)) * int(match.group(2))
    elif match.group(0) == "don't()":
        do = False
    elif match.group(0) == "do()":
        do = True

print(tot)
