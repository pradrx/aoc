f = open("input1", "r")

a = []

for line in f:
    l = line.strip()
    a.append(list(l))

# print(a)


def check_corners(i, j):
    corners = 0
    # top right corner
    if (oob(i - 1, j) or a[i - 1][j] != a[i][j]) and (oob(i - 1, j + 1) or a[i - 1][j + 1] != a[i][j]) and (oob(i, j + 1) or a[i][j + 1] != a[i][j]):
        corners += 1
    elif (not oob(i - 1, j) and a[i - 1][j] == a[i][j]) and (not oob(i, j + 1) and a[i][j + 1] == a[i][j]) and a[i - 1][j + 1] != a[i][j]:
        corners += 1
    elif (not oob(i - 1, j) and a[i - 1][j] != a[i][j]) and (not oob(i, j + 1) and a[i][j + 1] != a[i][j]) and (not oob(i - 1, j + 1) and a[i - 1][j + 1] == a[i][j]):
        corners += 1

    # top left corner
    if (oob(i - 1, j) or a[i - 1][j] != a[i][j]) and (oob(i - 1, j - 1) or a[i - 1][j - 1] != a[i][j]) and (oob(i, j - 1) or a[i][j - 1] != a[i][j]):
        corners += 1
    elif (not oob(i - 1, j) and a[i - 1][j] == a[i][j]) and (not oob(i, j - 1) and a[i][j - 1] == a[i][j]) and a[i - 1][j - 1] != a[i][j]:
        corners += 1
    elif (not oob(i - 1, j) and a[i - 1][j] != a[i][j]) and (not oob(i, j - 1) and a[i][j - 1] != a[i][j]) and (not oob(i - 1, j - 1) and a[i - 1][j - 1] == a[i][j]):
        corners += 1
    # bottom right corner
    if (oob(i + 1, j) or a[i + 1][j] != a[i][j]) and (oob(i + 1, j + 1) or a[i + 1][j + 1] != a[i][j]) and (oob(i, j + 1) or a[i][j + 1] != a[i][j]):
        corners += 1
    elif (not oob(i + 1, j) and a[i + 1][j] == a[i][j]) and (not oob(i, j + 1) and a[i][j + 1] == a[i][j]) and a[i + 1][j + 1] != a[i][j]:
        corners += 1
    elif (not oob(i + 1, j) and a[i + 1][j] != a[i][j]) and (not oob(i, j + 1) and a[i][j + 1] != a[i][j]) and (not oob(i + 1, j + 1) and a[i + 1][j + 1] == a[i][j]):
        corners += 1
    # bottom left corner
    if (oob(i + 1, j) or a[i + 1][j] != a[i][j]) and (oob(i + 1, j - 1) or a[i + 1][j - 1] != a[i][j]) and (oob(i, j - 1) or a[i][j - 1] != a[i][j]):
        corners += 1
    elif (not oob(i + 1, j) and a[i + 1][j] == a[i][j]) and (not oob(i, j - 1) and a[i][j - 1] == a[i][j]) and a[i + 1][j - 1] != a[i][j]:
        corners += 1
    elif (not oob(i + 1, j) and a[i + 1][j] != a[i][j]) and (not oob(i, j - 1) and a[i][j - 1] != a[i][j]) and (not oob(i + 1, j - 1) and a[i + 1][j - 1] == a[i][j]):
        corners += 1

    return corners

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def oob(i, j):
    if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]):
        return True
    return False

def calc_perimeter(i, j):
    p = 0
    for di, dj in dirs:
        new_i = i + di
        new_j = j + dj

        if oob(new_i, new_j) or a[i][j] != a[new_i][new_j]:
            p += 1

    return p

def dfs(i, j, visited):
    if (i, j) in visited:
        return -1, -1
    visited.add((i, j))
    area = 0
    sides = 0

    for di, dj in dirs:
        new_i = i + di
        new_j = j + dj

        if not oob(new_i, new_j) and a[new_i][new_j] == a[i][j] and (new_i, new_j) not in visited:
            ar, s = dfs(new_i, new_j, visited)
            area += ar
            sides += s

    


    return area + 1, sides + check_corners(i, j)


res = 0

visited = set()
for i in range(len(a)):
    for j in range(len(a[0])):
        area, perimeter = dfs(i, j, visited)
        if area == -1:
            continue
        res += area * perimeter

print(res)