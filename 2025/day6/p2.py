import math

def split_vals(s):
    return list(filter(None, s.split(" ")))

def form_numbers(vals):
    # vals is [123, 45, 6]
    max_len = 0
    for v in vals:
        max_len = max(max_len, len(v))
        
    for i, v in enumerate(vals):
        vals[i] = "#" * (max_len - len(v)) + vals[i]
        
    res = ["" for _ in range(len(vals))]
    idx = 0
    for i in range(max_len - 1, -1, -1):
        for v in vals:
            if v[i] == "#":
                continue
            res[idx] += v[i]
        idx += 1
    for i in range(len(res)):
        res[i] = int(res[i])
    print(res)
    return res

def perform_math(vals, operation):
    if operation == "+":
        idx = 0
        idx = 0
        return sum(vals)
    elif operation == "*":
        return math.prod(vals)
    raise Exception()
    

num_columns = []
operations = []


space = 0
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            if lines[j][i] != " ":
                break
        else:
            space = i
            break

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if j % 4 == 3:
                continue
    
print(space_idxs)

# with open("input.txt", "r") as file:
#     lines = file.read().splitlines()
#     num_columns = [[] for _ in range(len(split_vals(lines[0])))]
#     i = 0
#     while lines[i][0] not in ["*", "+"]:
#         vals = split_vals(lines[i])
        
#         for j in range(len(vals)):
#             num_columns[j].append(vals[j])
#         i += 1
#     operations = split_vals(lines[i])

# total = 0
# for i in range(len(operations)):
#     total += perform_math(form_numbers(num_columns[i]), operations[i])
# print(total)
