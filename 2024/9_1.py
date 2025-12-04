f = open("input1", "r")

l = ""
for line in f:
    l = line.strip()

def create_str_repr(disk):
    i = 0

    d = []
    while i < len(disk) - 1:
        file_size = disk[i]
        free_space = disk[i + 1]

        for j in range(int(file_size)):
            d.append(str(i // 2))

        a2 = "." * int(free_space)

        d += list(a2)

        i += 2


    for j in range(int(disk[-1])):
        d.append(str(i // 2))
    return d


disk_repr = list(create_str_repr(l))

def check_word_len(i):
    size = 0
    while disk_repr[i] != ".":
        size += 1
        i -= 1
    for i in range(i, i + size - 1):
        print(disk_repr[i])
    return size

def check_gap_size(i):
    size = 0
    while disk_repr[i] == ".":
        size += 1
        i += 1
    return size

l = 0
r = len(disk_repr) - 1

while True:
    # find gap
    if disk_repr[l] != ".":
        l += 1
        continue

    l_size = check_gap_size(l)

    # try all r_words until we find a size:
    r = len(disk_repr) - 1
    while r > (l + l_size):
        if disk_repr[r] == ".":
            r -= 1
            continue
        r_size = check_word_len(r)
        
        # check if can swap
        if l_size >= r_size:
            # perform swap
            x = 0
            for i in range(r - r_size, r + 1):
                disk_repr[l + x] = disk_repr[i]
                x += 1
                disk_repr[i] = "."
        r = r - r_size


total = 0


for i in range(len(disk_repr)):
    c = disk_repr[i]
    if not c.isdigit():
        continue

    total += i * int(c)

print(total)