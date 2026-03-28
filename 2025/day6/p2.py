import math

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
ops_idx = set()

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    for i, c in enumerate(lines[-1]):
        if c != " ":
            operations.append(c)
            ops_idx.add(i - 1)
    
    for i in range(len(lines) - 1):
        s = ""
        nums = []
        for j in range(len(lines[0])):
            if j in ops_idx:  # TODO:verify logic
                nums.append(s)
                s = ""
                continue
                
            if lines[i][j] == " ":
                s += "#"
            else:
                s += lines[i][j]
        nums.append(s)
        num_columns.append(nums)

res = 0

for i in range(len(num_columns[0])):
    vals = ["" for i in range(len(num_columns[0][i]))]
    for j in range(len(num_columns)):
        for k in range(len(num_columns[j][i])):
            if num_columns[j][i][k] == "#":
                continue
            vals[k] += num_columns[j][i][k]

    for k in range(len(vals)):
        if vals[k] == "":
            vals[k] = 0
        vals[k] = int(vals[k])
    res += perform_math(vals, operations[i])
print(res)
