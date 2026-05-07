from collections import defaultdict

import pprint

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

points = defaultdict(int)

for line in lines:
    v1, _, v2 = line.split()
    x1, y1 = [int(x) for x in v1.strip().split(",")]
    x2, y2, = [int(x) for x in v2.strip().split(",")]
    
    if x1 == x2:
        lo = min(y1, y2)
        hi = max(y1, y2)
        
        for i in range(lo, hi + 1):
            points[(x1, i)] += 1
    elif y1 == y2:
        lo = min(x1, x2)
        hi = max(x1, x2)
        
        for i in range(lo, hi + 1):
            points[(i, y1)] += 1

count = 0
for freq in points.values():
    if freq > 1:
        count += 1
print(count)
