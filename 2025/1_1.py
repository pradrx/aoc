f = open("input", "r")

dial = 50
zero_count = 0

for line in f:
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    
    factor = 1 if direction == "R" else -1

    dial += (factor * distance)
    if dial >= 100 or dial < 0:
        dial = dial % 100
    
    if dial == 0:
        zero_count += 1
        
print(zero_count)
    