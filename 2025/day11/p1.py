import pprint

with open("input.txt") as f:
    lines = f.read().splitlines()

adjacency_map = {}

for line in lines:
    device_mapping = line.split()
    device = device_mapping[0][:-1]
    outputs = device_mapping[1:]
    adjacency_map[device] = outputs

def dfs(device):
    if device == "out":
        return 1
    if device not in adjacency_map:
        return 0
    
    total = 0
    for output in adjacency_map[device]:
        total += dfs(output)
    return total        

print(dfs("you"))
