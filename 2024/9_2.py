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
    init_c = disk_repr[i]
    size = 0
    while disk_repr[i] == init_c:
        size += 1
        i -= 1
    return size

def check_gap_size(i):
    size = 0
    while disk_repr[i] == ".":
        size += 1
        i += 1
    return size


# l = 0
# r = len(disk_repr) - 1

# try:
#     while True:
#         # find gapa
#         r = len(disk_repr) - 1
#         if disk_repr[l] != ".":
#             l += 1
#             continue

#         l_size = check_gap_size(l)
#         print(l_size, ''.join(disk_repr))

#         while r > (l + l_size):
#             if disk_repr[r] == ".":
#                 r -= 1
#                 continue
#             r_size = check_word_len(r)

#             if l_size >= r_size:
#                 r_str = disk_repr[r - r_size + 1: r + 1]
#                 print(r_str)
#                 for i in range(len(r_str)):
#                     disk_repr[l + i] = disk_repr[r - r_size + 1 + i]
#                     disk_repr[r - r_size + 1 + i] = "."
                
#                 l += r_size
#                 break
#             else:
#                 r -= r_size
#         else:
#             l += l_size

# except Exception as e:
#     print(''.join(disk_repr))
#     print(e)
#     print(l, r, len(disk_repr))


# try word in every GAP, then move on to next word for each GAP, continue this way.

l = 0
r = len(disk_repr) - 1


try:
    while True:
        l = 0

        if disk_repr[r] == ".":
            r -= 1
            continue

        r_size = check_word_len(r)

        while l < (r - r_size + 1):
            if disk_repr[l] != ".":
                l += 1
                continue

            l_size = check_gap_size(l)

            if l_size >= r_size:
                r_str = disk_repr[r - r_size + 1: r + 1]
                for i in range(len(r_str)):
                    disk_repr[l + i] = disk_repr[r - r_size + 1 + i]
                    disk_repr[r - r_size + 1 + i] = "."

                r -= r_size
                break
            else:
                
                l += l_size
        else:
            r -= r_size
except Exception as e:
    print(disk_repr)
    print(e)
    print(l, r, len(disk_repr))

    checksum = 0
    for i in range(len(disk_repr)):
        if disk_repr[i].isdigit():      
            checksum += i * int(disk_repr[i])

    print(checksum)