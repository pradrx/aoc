with open("input.txt", "r") as f:
    depths = [int(x) for x in f.read().splitlines()]

increases = 0
for i in range(len(depths) - 3):
    w1 = depths[i] + depths[i + 1] + depths[i + 2]
    w2 = depths[i + 1] + depths[i + 2] + depths[i + 3]
    if w1 < w2:
        increases += 1

print(increases)
