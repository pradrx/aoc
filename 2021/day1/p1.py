with open("input.txt", "r") as f:
    depths = [int(x) for x in f.read().splitlines()]

increases = 0
for i in range(len(depths) - 1):
    curr = depths[i]
    next = depths[i + 1]
    if curr < next:
        increases += 1

print(increases)
