import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()



# part 1
blocks = []
j = 0
for i, inp in enumerate(input):

    if i % 2 == 0:
        blocks.extend([str(j)] * int(inp))
        j += 1
    else:
        blocks.extend(["."] * int(inp))

last_dot = 0
for i in range(len(blocks)-1, -1, -1):
    if blocks[i] != ".":
        for j in range(last_dot, i):
            if blocks[j] == ".":
                blocks[j], blocks[i] = blocks[i], blocks[j]
                last_dot = j
                break

checksum = 0
print(last_dot, len(blocks))
for i in range(len(blocks)):
    if blocks[i] != ".":
        checksum += i * int(blocks[i])

print(checksum)

# part 2
blocks = []
j = 0
for i, inp in enumerate(input):

    if i % 2 == 0:
        blocks.append([str(j)] * int(inp))
        j += 1
    else:
        if ["."] * int(inp) != []:
            blocks.append(["."] * int(inp))


blocks = [item for sublist in blocks for item in sublist]
print(blocks)
file_ids = sorted(set(blocks) - {"."}, key=int, reverse=True)

for file_id in file_ids:
    print(file_id)

    file_blocks = [i for i, x in enumerate(blocks) if x == file_id]
    if not file_blocks:
        continue
    file_length = len(file_blocks)

    free_space_start = None
    file_start = blocks.index(file_id)
    for i in range(0, file_start):
        if all(x == "." for x in blocks[i:i + file_length]):
            free_space_start = i
            break

    if free_space_start is not None:
        for idx in file_blocks:
            blocks[idx] = "."
        for i in range(file_length):
            blocks[free_space_start + i] = file_id

checksum = 0
for i, block in enumerate(blocks):
    if block != ".":
        checksum += i * int(block)

print(checksum)


