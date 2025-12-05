f = open("input", "r")

dial = 50
zero_count = 0

for line in f:
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    
    factor = 1 if direction == "R" else -1
    
    loops = distance // 100
    effective_distance = distance % 100
    
    zero_count += loops
    
    new_dial = dial + (factor * effective_distance)
    
    if new_dial >= 100 or new_dial <= 0:
        new_dial = new_dial % 100
        
        # If our existing dial is at 0, going into the negatives doesn't mean we
        # crossed over zero so we shouldn't increment here.
        if dial != 0:
            zero_count += 1
            
    dial = new_dial

print(zero_count)
