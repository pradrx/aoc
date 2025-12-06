from collections import defaultdict

f = open("input", "r")

total = 0

for line in f:
    line = line.strip()

    largest_num_ahead = [0] * (len(line) - 1)
    num_to_idx = defaultdict(list)
    batteries = [int(x) for x in line]
    largest = batteries[-1]

    for i in range(len(batteries) -2, -1, -1):
        n = batteries[i]
        largest_num_ahead[i] = largest
        largest = max(largest, n)
        num_to_idx[n].append(i)
        
    for i in range(9, -1, -1):
        indexes = num_to_idx[i]
        if not indexes:
            continue
        
        max_ahead = 0
        for idx in indexes:
            max_ahead = max(max_ahead, largest_num_ahead[idx])
        
        total += (i * 10) + max_ahead
        break

print(total)
