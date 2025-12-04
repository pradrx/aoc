f = open("input", "r")


a1 = []
a2 = []
for line in f:
    l = line.strip().split(" ")
    a1.append(int(l[0]))
    a2.append(int(l[3]))

a1.sort()
a2.sort()

dist = 0

for i in range(len(a1)):
    dist += abs(a1[i] - a2[i])

print(dist)
