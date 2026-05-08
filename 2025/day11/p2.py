from functools import lru_cache

with open("input.txt") as f:
    lines = f.read().splitlines()

adjacency_map = {}

for line in lines:
    device_mapping = line.split()
    device = device_mapping[0][:-1]
    outputs = device_mapping[1:]
    adjacency_map[device] = outputs

@lru_cache(None)
def dfs(device, visited_fft, visited_dac):
    if device == "out" and visited_fft and visited_dac:
        return 1
    if device == "fft":
        visited_fft = True
    if device == "dac":
        visited_dac = True
    if device not in adjacency_map:
        return 0
    total = 0
    for output in adjacency_map[device]:
        total += dfs(output, visited_fft, visited_dac)
    return total

print(dfs("svr", False, False))
