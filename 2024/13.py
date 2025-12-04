f = open("input1", "r")

a = []
for line in f:
    l = line.strip()

    if l:
        a.append(l)

dat = []

i = 0
while i < len(a):
    x = a[i]
    s = x.split(" ")
    btn_a_x = s[2]
    btn_a_y = s[3]

    btn_a_x_val = btn_a_x.split("+")[1].replace(",", "")
    btn_a_y_val = btn_a_y.split("+")[1]

    x = a[i + 1]
    s = x.split(" ")
    btn_b_x = s[2]
    btn_b_y = s[3]

    btn_b_x_val = btn_b_x.split("+")[1].replace(",", "")
    btn_b_y_val = btn_b_y.split("+")[1]

    p_split = a[i + 2].split(" ")

    x_prize = p_split[1].split("=")[1].replace(",", "")
    y_prize = p_split[2].split("=")[1]

    i += 3

    dat.append((int(btn_a_x_val), int(btn_a_y_val), int(btn_b_x_val), int(btn_b_y_val), int(x_prize), int(y_prize)))

tokens_spent = 0

def solve_system(A, B, C, D, N, M):
    x = ((N * D) - (M * B)) / ((D * A) - (C * B))

    y = (N - (A * x)) / B

    if not x.is_integer() or not y.is_integer():
        return False

    return x, y


for a_x, a_y, b_x, b_y, prize_x, prize_y in dat:
    # print(a_x, a_y, b_x, b_y, prize_x, prize_y)

    # for i in range(101):
    #     for j in range(101):
    #         total_x = a_x * i + b_x * j
    #         total_y = a_y * i + b_y * j

    #         if total_x == prize_x and total_y == prize_y:
    #             min_tokens = min(min_tokens, i * 3 + j * 1)

    # if min_tokens != 99999999999:
    #     tokens_spent += min_tokens

    A = a_x
    B = b_x
    C = a_y
    D = b_y

    n = prize_x + 10000000000000
    m = prize_y + 10000000000000


    x = solve_system(A, B, C, D, n, m)

    if x:
        btn_a_presses = x[0]
        btn_b_presses = x[1]

        tokens_spent += btn_a_presses * 3 + btn_b_presses * 1

    


print(tokens_spent)
            
