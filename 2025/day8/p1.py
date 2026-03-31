import math
import heapq

from collections import defaultdict

CONNECTIONS = 1000
K_LARGEST = 3

def calc_distance(a, b):
    x = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    return math.sqrt(x)
    
def dfs(box, visited, adj_map):
    if box in visited:
        return 0
    
    visited.add(box)
    total = 0
    for adj in adj_map[box]:
        total += dfs(adj, visited, adj_map)
    return 1 + total

boxes = []
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        coords = [int(x) for x in line.split(",")]
        boxes.append((*coords,))

distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        a = boxes[i]
        b = boxes[j]
        
        distances.append((calc_distance(a, b), a, b))
distances.sort()

adj_map = defaultdict(list)
for i in range(CONNECTIONS):
    d, boxa, boxb = distances[i]
    adj_map[boxa].append(boxb)
    adj_map[boxb].append(boxa)

visited = set()
heap = [0 for _ in range(K_LARGEST)]
for box in boxes:
    circuit_size = dfs(box, visited, adj_map)
    heapq.heappushpop(heap, circuit_size)

print(math.prod(heap))
