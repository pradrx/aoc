from collections import deque

from utils.read_str_grid import read_str_grid

def at_end(beam):
    return 

grid = read_str_grid()
splits = set()
queue = deque()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            queue.append((i, j))
            break

while queue:
    beamr, beamc = queue.popleft()
    # beam at bottom of grid
    if beamr == len(grid) - 1:
        continue
    if grid[beamr + 1][beamc] == "|":
        continue

    if grid[beamr + 1][beamc] == ".":
        grid[beamr + 1][beamc] = "|"
        queue.append((beamr + 1, beamc))
    elif grid[beamr + 1][beamc] == "^":
        # splitter
        splits.add((beamr + 1, beamc))
        dirs = [-1, 1]
        for dc in dirs:
            if grid[beamr][beamc + dc] == ".":
                grid[beamr][beamc + dc] = "|"
                queue.append((beamr, beamc + dc))

print(len(splits))
