f = open("input2", "r")

flag = False

init_values = {}

gates = []


for line in f:
    if not flag:
        l = line.strip().replace(":", "").split()

        if not l:
            flag = True
            continue

        init_values[l[0]] = int(l[1])

    else:
        l = line.strip().split()
        gates.append(l)

while True:
    new_gates = []
    for v1, op, v2, _, v3 in gates:
        if v1 in init_values and v2 in init_values:
            if op == "AND":
                init_values[v3] = init_values[v1] & init_values[v2]
            elif op == "OR":
                init_values[v3] = init_values[v1] | init_values[v2]
            elif op == "XOR":
                init_values[v3] = init_values[v1] ^ init_values[v2]
        else:
            new_gates.append([v1, op, v2, _, v3])

    if not new_gates:
        break

    gates = new_gates    

z_vals = [x for x in list(init_values.keys()) if x[0] == "z"]

z_vals.sort(reverse=True)

print(z_vals)

binary_str = []

for v in z_vals:
    binary_str.append(str(init_values[v]))

print(int("".join(binary_str), 2))
