with open("input.txt") as f:
    lines = f.read().splitlines()
 
def sum_values(n):
    return (n * (n + 1)) // 2

crabs = [int(x) for x in lines[0].split(",")]

min_fuel = float('inf')
for i in range(len(crabs)):
    fuel = 0
    for j in range(len(crabs)):
        fuel += sum_values(abs(crabs[i] - crabs[j]))
    min_fuel = min(min_fuel, fuel)

print(min_fuel)
