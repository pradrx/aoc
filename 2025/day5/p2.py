def search_intervals(intervals, val):
    for start, end in intervals:
        if val >= start and val <= end:
            return True
    return False


id_ranges = []
ids = []

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    i = 0
    while lines[i] != "":
        start, end = lines[i].split("-")
        id_ranges.append([int(start), int(end)])
        i += 1
    i += 1
    while i < len(lines):
        ids.append(int(lines[i]))
        i += 1

id_ranges.sort()

merged = [id_ranges[0]]
for start, end in id_ranges[1:]:
    prev_start, prev_end = merged[-1]
    if prev_end >= start:
        merged[-1][1] = max(prev_end, end)
        continue
    merged.append([start, end])

total = 0
for start, end in merged:
    total += end - start + 1
print(total)
