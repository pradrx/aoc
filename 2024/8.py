f = open("input2", "r")

a = []
for line in f:
    l = line.strip()
    a.append(l)

from collections import defaultdict

node_map = defaultdict(list)

antinodes = set()

def calc_antinodes(node1, node2):
    i1, j1 = node1
    i2, j2 = node2

    idelta = abs(i1 - i2) # -2 
    jdelta = abs(j1 - j2) # -1

    i1smaller = True if i1 < i2 else False
    j1smaller = True if j1 < j2 else False

    antinodes = []

    antinodes.append((i1, j1))
    antinodes.append((i2, j2))

    while True:
        antinode1 = [0, 0]
        if i1smaller:
            antinode1[0] = i1 - idelta
        else:
            antinode1[0] = i1 + idelta

        if j1smaller:
            antinode1[1] = j1 - jdelta
        else:
            antinode1[1] = j1 + jdelta

        if oob(antinode1):
            break
        
        
        antinodes.append(tuple(antinode1))

        i1 = antinodes[-1][0]
        j1 = antinodes[-1][1]

    while True:
        antinode2 = [0, 0]
        if i1smaller:
            antinode2[0] = i2 + idelta
        else:
            antinode2[0] = i2 - idelta

        if j1smaller:
            antinode2[1] = j2 + jdelta
        else:
            antinode2[1] = j2 - jdelta

        if oob(antinode2):
            break

        antinodes.append(tuple(antinode2))

        i2 = antinodes[-1][0]
        j2 = antinodes[-1][1]

    return antinodes


def oob(pair):
    i, j = pair

    if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]):
        return True

    return False 

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] != "." and a[i][j] != "#":
            node_map[a[i][j]].append((i, j))

antinodes_set = set()

for nodes in node_map.values():
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            antinodes = calc_antinodes(nodes[i], nodes[j])

            for n in antinodes:
                antinodes_set.add(n)


print(len(antinodes_set))

z = list(antinodes_set)

z.sort()

print(z)