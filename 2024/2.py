f = open("input2", "r")

safe = 0
for line in f:
    a = []
    l = line.strip().split(" ")

    for x in l:
        a.append(int(x))

    for j in range(len(a)):
        a_copy = a.copy()
        del a_copy[j]
        print(a_copy)

        decreasing = False

        if a_copy[0] > a_copy[1]:
            decreasing = True

        unsafe = False

        for i in range(len(a_copy) - 1):
            if decreasing:
                if a_copy[i] - a_copy[i + 1] < 1 or a_copy[i] - a_copy[i + 1] > 3:
                    unsafe = True
                    break
            else:
                if a_copy[i] - a_copy[i + 1] < -3 or a_copy[i] - a_copy[i + 1] > -1: 
                        unsafe = True
                        break

        if not unsafe:
            safe += 1
            break


print(safe)