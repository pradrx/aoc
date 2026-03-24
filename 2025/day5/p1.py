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

fresh_count = 0
for id in ids:
    if search_intervals(id_ranges, id):
        fresh_count += 1
print(fresh_count)
