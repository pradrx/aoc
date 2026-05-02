with open("input.txt", "r") as f:
    depth = 0
    length = 0
    aim = 0
    for line in f.read().splitlines():
        move, distance = line.split(" ")
        distance = int(distance)
        if move == "forward":
            length += distance
            depth += aim * distance
        elif move == "up":
            aim -= distance
        elif move == "down":
            aim += distance
            
print(depth * length)
