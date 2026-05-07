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
    else:
        # diagonal
        lo = (int(x1), int(y1)) if y1 < y2 else (x2, y2)
        hi = (int(x1), int(y1)) if y1 > y2 else (x2, y2)
        
        start = lo[0]
        if lo[0] < hi[0]:
            delta = 1
        else:
            delta = -1
        
        for i in range(lo[1], hi[1] + 1):
            points[(start, i)] += 1
            start += delta

count = 0
for freq in points.values():
    if freq > 1:
        count += 1
print(count)
