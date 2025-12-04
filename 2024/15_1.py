from pprint import pprint

f = open("input1", "r")

grid = []
commands = []

p2 = False
for line in f:
    if not p2:
        l = line.strip()
        if l == "":
            p2 = True
            continue
        grid.append(list(l))
    else:
        l = line.strip()
        commands += list(l)

def get_lanternfish():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)

lanternfish = get_lanternfish()
# print(lanternfish)

command_to_dir = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

def move(posx, posy, command):
    dx, dy = command_to_dir[command]

    new_x = posx + dx
    new_y = posy + dy

    if grid[new_x][new_y] == ".":
        grid[new_x][new_y] = grid[posx][posy]
        return True
    elif grid[new_x][new_y] == "O":
        if move(new_x, new_y, command):
            grid[new_x][new_y] = grid[posx][posy]
            return True
        return False
    elif grid[new_x][new_y] == "#":
        return False

for command in commands:
    move(lanternfish[0], lanternfish[1], command)

    dx, dy = command_to_dir[command]
    if grid[lanternfish[0] + dx][lanternfish[1] + dy] == "@":
        grid[lanternfish[0]][lanternfish[1]] = "."
        lanternfish = (lanternfish[0] + dx, lanternfish[1] + dy)

def calc_score():
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                top_dist = i * 100
                left_dist = j

                score += top_dist + left_dist

    return score

print(calc_score())
