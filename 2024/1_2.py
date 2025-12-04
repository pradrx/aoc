f = open("input", "r")


a1 = []
a2 = []
for line in f:
    l = line.strip().split(" ")
    a1.append(int(l[0]))
    a2.append(int(l[3]))


sim = 0

for v1 in a1:
    count = 0
    for v2 in a2:
        if v1 == v2:
            count += 1
    sim += count * v1

print(sim)