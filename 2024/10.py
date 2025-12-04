f = open("input1", "r")

a = []
for line in f:
    l = line.strip()
    b = []
    for c in l:
        b.append(c)
    a.append(b)

def find_trailheads():
    trailheads = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == "0":
                trailheads.append((i, j))

    return trailheads

trailheads = find_trailheads()

print(trailheads)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = set() # COMMENT FOR P2

def oob(i, j):
    if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]):
        return True
    return False

def dfs(i, j):
    if a[i][j] == "9":
        visited.add((i, j)) # COMMENT FOR P2
        return 1

    res = 0

    for pi, pj in dirs:
        new_i, new_j = i + pi, j + pj

        if not oob(new_i, new_j) and a[new_i][new_j].isdigit() and (int(a[new_i][new_j]) == int(a[i][j]) + 1):
            res += dfs(new_i, new_j)

    return res


res = 0

for i, j in trailheads:
    res += dfs(i, j)
    visited = set() # COMMENT FOR P2


print(res)