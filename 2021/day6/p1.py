with open("input.txt") as f:
    fish = f.read().splitlines()

fish = [int(x) for x in fish[0].split(",")]
for _ in range(80):
    length = len(fish)
    for i in range(length):
        fish[i] -= 1
        if fish[i] == -1:
           fish[i] = 6
           fish.append(8)

print(len(fish))
