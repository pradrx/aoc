from collections import deque

from functools import lru_cache

from utils.read_str_grid import read_str_grid

dirs = [-1, 1]
grid = read_str_grid()

@lru_cache
def dfs(r, c):
    if r == len(grid) - 1:
        return 1
        
    if grid[r][c] == "^":
        total = 0
        for dc in dirs:
            if grid[r][c + dc] == ".":
                total += dfs(r, c + dc)
        return total
    
    return dfs(r + 1, c)

for j in range(len(grid[0])):
    if grid[0][j] == "S":
        startc = j
        break
    
print(dfs(0, startc))
