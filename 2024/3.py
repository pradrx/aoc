import re
f = open("input2", "r")

sum = 0

do = True

for l in f:
    
    x = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", l)

    for match in x:
        if match == "do()":
            do = True
            continue
        if match == "don't()":
            do = False
            continue
        
        if not do:
            continue
        parsed = match[match.index("(") + 1:len(match) - 1]
        vals = parsed.split(",")
        v1 = int(vals[0])
        v2 = int(vals[1])

        sum += v1 * v2

print(sum)

