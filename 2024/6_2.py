from pprint import pprint

f = open("input2", "r")

m = []

for i, line in enumerate(f):
    l = line.strip()
    m.append(list(l))

guard = None
og_guard_pos = None
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "^":
            guard = [i, j]
            og_guard_pos = [i, j]

def oob(i, j):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return True
    return False

def next_area(direc, guard_idx):
    if direc == "up":
        return [guard_idx[0] - 1, guard_idx[1]]
    elif direc == "right":
        return [guard_idx[0], guard_idx[1] + 1]
    elif direc == "down":
        return [guard_idx[0] + 1, guard_idx[1]]
    elif direc == "left":
        return [guard_idx[0], guard_idx[1] - 1]

dir_changes = 0
dirs = ["up", "right", "down", "left"]
cur_dir = "up"


traps = 0

for i in range(len(m)):
    for j in range(len(m[0])):
        dir_changes = 0
        cur_dir = "up"
        move_count = 0
        loop_cap = len(m) * len(m[0]) * 3

        if m[i][j] == "#" or m[i][j] == "^":
            continue
        
        m[i][j] = "#"

        while move_count < loop_cap:
            next_move = next_area(cur_dir, guard)
            next_row, next_col = next_move
            if oob(next_row, next_col):
                break

            if m[next_row][next_col] == "#":
                dir_changes += 1
                cur_dir = dirs[dir_changes % 4]
                continue

            guard = next_move
            move_count += 1
        else:
            traps += 1

        m[i][j] = "."
        guard = og_guard_pos

print(traps)