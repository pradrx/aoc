from utils.read_str_grid import read_str_grid

def out_of_bounds(grid, r, c):
    return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
    
    
def count_adjacent_rolls(grid, r, c):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for dr, dc in dirs:
        newr = dr + r
        newc = dc + c
        if not out_of_bounds(grid, newr, newc) and grid[newr][newc] == "@":
            count += 1
    return count
    

def remove_rolls(grid):
    removed = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ".":
                continue
            if count_adjacent_rolls(grid, r, c) < 4:
                grid[r][c] = "."
                removed += 1
    return removed

grid = read_str_grid()

grid_cleaned = False
total_removed = 0
while not grid_cleaned:
    cur_removed = remove_rolls(grid)
    total_removed += cur_removed
    if cur_removed == 0:
        grid_cleaned = True
print(total_removed)
