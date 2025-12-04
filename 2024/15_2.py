from pprint import pprint

f = open("input1", "r")


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()
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

def expand_grid():
    biggrid = []

    for g in grid:
        a = []
        for c in g:
            if c == "#":
                a.append("#")
                a.append("#")
            elif c == "O":
                a.append("[")
                a.append("]")
            elif c == ".":
                a.append(".")
                a.append(".")
            elif c == "@":
                a.append("@")
                a.append(".")
        biggrid.append(a)
    return biggrid

biggrid = expand_grid()

def get_lanternfish():
    for i in range(len(biggrid)):
        for j in range(len(biggrid[0])):
            if biggrid[i][j] == "@":
                return (i, j)

lanternfish = get_lanternfish()
print(lanternfish)
print_grid(biggrid)

def can_move(posx, posy, command):


# command_to_dir = {
#     "^": (-1, 0),
#     "v": (1, 0),
#     "<": (0, -1),
#     ">": (0, 1),
# }

def move(posx, posy, command):
    dx, dy = command_to_dir[command]

    new_x = posx + dx
    new_y = posy + dy

    if grid[new_x][new_y] == ".":
        return True
    elif grid[new_x][new_y] == "[" or grid[new_x][new_y] == "]":
        if not move(new_x, new_y, command):
            return False
        return True
    elif grid[new_x][new_y] == "#":
        return False

# for command in commands:
#     move(lanternfish[0], lanternfish[1], command)

#     dx, dy = command_to_dir[command]
#     if grid[lanternfish[0] + dx][lanternfish[1] + dy] == "@":
#         grid[lanternfish[0]][lanternfish[1]] = "."
#         lanternfish = (lanternfish[0] + dx, lanternfish[1] + dy)

# def calc_score():
#     score = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == "O":
#                 top_dist = i * 100
#                 left_dist = j

#                 score += top_dist + left_dist

#     return score

# print(calc_score())
