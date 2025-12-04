from pprint import pprint

f = open("input2", "r")

m = []

for i, line in enumerate(f):
    l = line.strip()
    m.append(list(l))

guard = None

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "^":
            guard = [i, j]

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

while True:
    next_move = next_area(cur_dir, guard)
    next_row, next_col = next_move
    if oob(next_row, next_col):
        break

    if m[next_row][next_col] == "#":
        dir_changes += 1
        cur_dir = dirs[dir_changes % 4]
        continue

    guard = next_move
    m[next_row][next_col] = "X"


x_cnt = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "X":
            x_cnt += 1

print(x_cnt)
