with open("input.txt") as f:
    fish = f.read().splitlines()

count = [0 for _ in range(10)]
fish = [int(x) for x in fish[0].split(",")]

for f in fish:
    count[f] += 1
    
for i in range(256):
    new_count = [0 for _ in range(10)]
    for j in range(1, 10):
        new_count[j - 1] = count[j]
    new_count[6] += count[0]
    new_count[8] += count[0]
    count = new_count
print(sum(count))
