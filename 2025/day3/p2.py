with open("input.txt", "r") as f:
    battery_lines = f.read().splitlines()

line_len = len(battery_lines[0])
size = 12

res = 0
for batteries in battery_lines:
    good_batteries = ""
    last_idx = -1
    while len(good_batteries) != size:
        max_val = -1
        for i in range(last_idx + 1, line_len - size + 1 + len(good_batteries)):
            if int(batteries[i]) > max_val:
                max_val = int(batteries[i])
                last_idx = i
        good_batteries += str(max_val)
    res += int(good_batteries)
print(res)
        
    
    
