import os
import numpy as np
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

a_buttons, b_buttons, prices = [], [], []
for i in range(0, len(input.split("\n")), 4):
    a_button = [int(dir[2:]) for dir in input.split("\n")[i].replace("Button A: ", "").split(", ")]
    b_button = [int(dir[2:]) for dir in input.split("\n")[i+1].replace("Button B: ", "").split(", ")]
    price = [int(dir[2:]) for dir in input.split("\n")[i+2].replace("Prize: ", "").split(", ")]
    
    a_buttons.append(a_button)
    b_buttons.append(b_button)
    prices.append(price)

# part 1
spent = 0
for i in range(len(a_buttons)):
    a_button = a_buttons[i]
    b_button = b_buttons[i]
    price = prices[i]

    A = np.column_stack((a_button, b_button))
    coeffs = np.linalg.solve(A, price)

    a, b = coeffs
    a_og, b_og = round(a, 4), round(b, 4)
    a, b = math.ceil(a_og), math.ceil(b_og) 
    print(a, b)
    if a >= 0 and b >= 0 and a <= 100 and b <= 100 and a==a_og and b == b_og:
        spent += a*3 + b*1

print(spent)

# part 2

spent = 0
for i in range(len(a_buttons)):
    a_button = a_buttons[i]
    b_button = b_buttons[i]
    price = [x+10000000000000 for x in prices[i]]

    A = np.column_stack((a_button, b_button))
    coeffs = np.linalg.solve(A, price)

    a, b = coeffs
    a_og, b_og = round(a, 4), round(b, 4)
    a, b = math.ceil(a_og), math.ceil(b_og) 
    if a >= 0 and b >= 0 and a==a_og and b == b_og:
        spent += a*3 + b*1

print(spent)
