from collections import defaultdict

f = open("input1", "r")

COLS = 101
ROWS = 103

SECONDS = 100

a = []
for line in f:
    l = line.strip().split(" ")
    
    s1 = l[0].split(",")

    px = int(s1[0].split("=")[1])
    py = int(s1[1])

    s2 = l[1].split(",")
    vx = int(s2[0].split("=")[1])
    vy = int(s2[1])

    a.append((px, py, vx, vy))

# res = defaultdict(int)

def tree_line_check(pos_set):

    for x, y in pos_set:
        for i in range(1, 7):
            if (x + i, y) not in pos_set:
                break
        else:
            return True
    return False
    # for i in range(COLS):
    #     for j in range(ROWS - 5):
    #         if (i, j) not in pos_set:
    #             break

    #     else:
    #         return True

    # return False


for sec in range(1, 100000000000):
    pos_set = set()
    for i, (px, py, vx, vy) in enumerate(a):
        # print(i, px, py, vx, vy)
        new_px = (px + vx) % COLS
        new_py = (py + vy) % ROWS

        a[i] = ((new_px, new_py, vx, vy))

        pos_set.add((new_px, new_py))

    # print(pos_set)
    if tree_line_check(pos_set):
        print(sec)


def safety_count():
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    mid_x = COLS // 2
    mid_y = ROWS // 2

    for p, count in res.items():
        px = p[0]
        py = p[1]

        if px == mid_x or py == mid_y:
            continue
        if px >= 0 and px < mid_x:
            if py >= 0 and py < mid_y:
                q1 += count
            else:
                q2 += count
        else:
            if py >= 0 and py < mid_y:
                q3 += count
            else:
                q4 += count


    return (q1 * q2 * q3 * q4)


# print(safety_count())
        
