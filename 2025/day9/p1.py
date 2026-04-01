points = []
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        col, row = line.split(",")
        points.append((int(row), int(col)))

# naive approach
max_size = 0
for i in range(len(points)):
    for j in range(i, len(points)):
        length = abs(points[i][0] - points[j][0] + 1)
        width = abs(points[i][1] - points[j][1] + 1)
        max_size = max(max_size, length * width)
print(max_size)
