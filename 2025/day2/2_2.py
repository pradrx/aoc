f = open("input", "r")

# Not interested in learning regex this year either!

factorMap = {
    1: [1],
    2: [1],
    3: [1],
    4: [1, 2],
    5: [1],
    6: [1, 2, 3],
    7: [1],
    8: [1, 2, 4],
    9: [1, 3],
    10: [1, 2, 5],
}

total = 0

for line in f:
    line = line.strip()
    id_ranges = line.split(",")
    
    id_pairs = []
    for r in id_ranges:
        id_pairs.append(r.split("-"))
    
    for first, last in id_pairs:
        for i in range(int(first), int(last) + 1):
            snum = str(i)
            if len(snum) == 1:
                continue
            factors = factorMap[len(snum)]
            
            for factor in factors:
                snippet = snum[:factor]
                l, r = factor, factor * 2
                while (r <= len(snum)):
                    if snippet != snum[l:r]:
                        break
                    l += factor
                    r += factor
                    
                else:
                    total += i
                    break
            
print(total)
