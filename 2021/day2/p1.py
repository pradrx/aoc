with open("input.txt", "r") as f:
    depth = 0
    length = 0
    for line in f.read().splitlines():
        move, distance = line.split(" ")
        distance = int(distance)
        if move == "forward":
            length += distance
        elif move == "up":
            depth -= distance
        elif move == "down":
            depth += distance
            
print(depth * length)
