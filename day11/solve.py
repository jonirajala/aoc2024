import os
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")
with open(file_path, "r") as f:
    input = f.read()

# part 1
    
stones = [int(i) for i in input.replace("\n", "").split(" ")]
blinks = 25
for i in range(blinks):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
        else:
            new_stones.append(stone*2024)

    stones = new_stones

print(len(stones))


# part 2

stones = [int(i) for i in input.replace("\n", "").split(" ")]

blinks = 75
stone_counts = Counter(stones)
for _ in range(blinks):
    new_stone_counts = Counter()

    for stone, count in stone_counts.items():
        if stone == 0:
            new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            digits = str(stone)
            mid = len(digits) // 2
            left = int(digits[:mid])
            right = int(digits[mid:])
            new_stone_counts[left] += count
            new_stone_counts[right] += count
        else:
            new_stone_counts[stone * 2024] += count

    stone_counts = new_stone_counts

print(sum(stone_counts.values()))
