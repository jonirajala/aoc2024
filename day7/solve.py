import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

print(input)
equations = []
for row in input.split("\n"):
    if len(row) < 1: continue
    tot, vals = row.split(":")
    print(vals.split(" "))
    equations.append((int(tot), [int(val) for val in vals.split(" ")[1:]]))


# part 1
def calculate(tot, vals, operators):
    result = vals[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += vals[i + 1]
        elif op == "*":
            result *= vals[i + 1]
    return result == tot

def valid_ops(tot, vals, operators):
    if len(operators) == len(vals) - 1:
        return calculate(tot, vals, operators)
    
    for op in ["+", "*"]:
        if valid_ops(tot, vals, operators + [op]):
            return True
        
    return False

corr = 0
for i, (tot, vals) in enumerate(equations):
    print(f"{i + 1}/{len(equations)}")
    if valid_ops(tot, vals, []):
        corr += tot
print(corr)

# part 2
def calculate(tot, vals, operators):

    result = vals[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += vals[i + 1]
        elif op == "*":
            result *= vals[i + 1]
        elif op == "||":
            result = int(str(result) + str(vals[i + 1]))
            
    return result == tot

def valid_ops(tot, vals, operators):
    if len(operators) == len(vals) - 1:
        return calculate(tot, vals, operators)
    for op in ["+", "*", "||"]:
        if valid_ops(tot, vals, operators + [op]):
            return True
        
    return False

corr = 0
for i, (tot, vals) in enumerate(equations):
    print(f"{i + 1}/{len(equations)}")
    if valid_ops(tot, vals, []):
        corr += tot
print(corr)