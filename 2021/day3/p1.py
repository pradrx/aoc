from itertools import chain

with open("input.txt", "r") as f:
    lines = (line.strip() for line in f)
    first = next(lines)
    counts = [0] * len(first)
    num_lines = 0
    
    for line in chain([first], lines):
        num_lines += 1
        for i, ch in enumerate(line):
            if ch == "1":
                counts[i] += 1

gamma = 0
half = num_lines // 2
for i, count in enumerate(counts):
    if count > half:
        gamma += 2**(len(counts) - (i + 1))

epsilon = gamma ^ ((1 << len(counts)) - 1)
print(gamma * epsilon)
