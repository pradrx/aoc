f = open("input", "r")

total = 0

for line in f:
    line = line.strip()
    
    id_ranges = line.split(",")
    id_pairs = [x.split("-") for x in id_ranges]
    
    for first, last in id_pairs:
        for i in range(int(first), int(last) + 1):
            snum = str(i)
            if len(snum) % 2 == 1:
                continue
            
            mid = len(snum) // 2
            if snum[0:mid] == snum[mid:len(snum)]:
                total += i

print(total)
