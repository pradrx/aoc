import copy
f = open("input2", "r")

ops = []

for line in f:
    l = line.strip().split(" ")
    l[0] = l[0].replace(":", "")
    ops.append(l)

def gen_combos(combos, cur_combo, max):
    if len(cur_combo) == max:
        return combos.append(cur_combo)

    gen_combos(combos, cur_combo + "*", max)
    gen_combos(combos, cur_combo + "+", max)
    gen_combos(combos, cur_combo + "|", max)

    return combos

res = 0

for op in ops:
    total = int(op[0])
    nums = op[1:]
    og_nums = list(nums)


    combos = gen_combos([], "", len(nums) - 1)

    for combo in combos:
        for i in range(len(combo)):
            symbol = combo[i]

            if symbol == "+":
                og_nums[i + 1] = int(og_nums[i]) + int(og_nums[i + 1])
            elif symbol == "*":
                og_nums[i + 1] = int(og_nums[i]) * int(og_nums[i + 1])
            elif symbol == "|":
                og_nums[i + 1] = int(str(og_nums[i]) + str(og_nums[i + 1]))
        
        if og_nums[-1] == total:
            res += total
            break

        og_nums = list(nums)

            


print(res)