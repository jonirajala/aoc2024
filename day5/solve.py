import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

rules = []
for idx, rule in enumerate(input.split("\n")):
    if rule == "": break
    a, b = rule.split("|")    
    rules.append([int(a), int(b)])
updates = [inp.split(",") for inp in input.split("\n")[idx:] if len(inp) > 1]

# part 1

middles = []
incorrect_ids = []
for update_id, update in enumerate(updates):
    correct = True

    for i in range(len(update)):
        curr = int(update[i])
        for j in range(i, len(update)):
            if [int(update[j]), curr] in rules:
                correct = False

    if correct: middles.append(int(update[len(update)//2]))
    else: incorrect_ids.append(update_id)

print(sum(middles))

# part 2
middles = []
for incorrect_id in incorrect_ids:
    update = updates[incorrect_id]
    while True:
        last_update = update.copy()
        for i in range(len(update)):
            curr = int(update[i])
            for j in range(i, len(update)):
                if [int(update[j]), curr] in rules:
                    update[i], update[j] = update[j], update[i]
        if update == last_update:
            break

    middles.append(int(update[len(update)//2]))

print(sum(middles))
