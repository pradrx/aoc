import math

f = open("input1", "r")

a = []

for i, line in enumerate(f):
    a = line.strip().split(" ")

for i in range(len(a)):
    a[i] = int(a[i])

def check_even(n):
    if (((int(log10(n)))))


count = 0
while count < 75:
    print(count)
    new_a = []

    for i in range(len(a)):
        e = a[i]

        if e == 0:
            new_a.append(1)
        elif (len(e) % 2) == 0:
            new_a.append(e[0:len(e)//2])
            next_num = e[len(e)//2:len(e)]
            new_a.append(str(int(next_num)))
        else:
            new_a.append(str(int(e) * 2024))

    a = list(new_a)
    count += 1

print(len(a))


@lru_cache(None)
def f(e, a):
    if e == "0":
        return "1"
    
    if len(e) % 2 == 1:
        return str(int(e) * 2024)

    a = e[0:len(e) / 2]
    b = str(int(e[len(e) / 2: len(e)]))

    

