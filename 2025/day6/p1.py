import math

def split_vals(s):
    return list(filter(None, s.split(" ")))

def perform_math(vals, operation):
    if operation == "+":
        return sum(vals)
    elif operation == "*":
        return math.prod(vals)
    raise Exception()
    

num_columns = []
operations = []

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    num_columns = [[] for _ in range(len(split_vals(lines[0])))]
    i = 0
    while lines[i][0] not in ["*", "+"]:
        vals = split_vals(lines[i])
        
        for j in range(len(vals)):
            num_columns[j].append(int(vals[j]))
        i += 1
    operations = split_vals(lines[i])

total = 0
for i in range(len(operations)):
    total += perform_math(num_columns[i], operations[i])
print(total)
