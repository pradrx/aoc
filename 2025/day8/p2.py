import math
import heapq

from collections import defaultdict

def calc_distance(a, b):
    x = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    return math.sqrt(x)
    
def is_graph_connected(boxes):
    visited = set()
    def dfs(box):
        if box in visited:
            return
        
        visited.add(box)
        for adj in adj_map[box]:
            dfs(adj)
    dfs(boxes[0])
    return len(visited) == len(boxes)

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
for i in range(len(distances)):
    d, boxa, boxb = distances[i]
    adj_map[boxa].append(boxb)
    adj_map[boxb].append(boxa)
    
    if is_graph_connected(boxes):
        print(boxa[0] * boxb[0])
        break

print("done")
