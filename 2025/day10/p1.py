from functools import lru_cache
import sys
sys.setrecursionlimit(1500)


lights = []
buttons = []
joltages = []
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        arr = line.split(" ")
        lights.append(arr[0].strip("[]"))
        button_strs = arr[1:len(arr)-1]
        button_tuples = []
        for button in button_strs:
            button_tuples.append(tuple(int(i) for i in button.strip("()").split(",")))
        buttons.append(tuple(button_tuples))
        joltages.append(arr[-1])
"""
subproblems can be based on state of light diagram. easiest way would be to
start from the end state. consider the example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

we start at [.##.], then we iterate over all possible button choices and
try to figure out the sequence that will get us to all empty the fastest.

main concern: infinite looping. we need to maintain a visited set during our
traversal so that we don't fall back into some previously visited state. exit
early in these cases.
"""

def is_lights_all_off(light):
    for c in light:
        if c != ".":
            return False
    return True

def apply_button(light, button):
    s = list(light)
    for step in button:
        s[step] = "." if s[step] == "#" else "#"
    return "".join(s)
        
visited = set()
@lru_cache(None)
def traverse(light, buttons):
    if light in visited:
        return -1
    if is_lights_all_off(light):
        return 0
    
    visited.add(light)
    min_presses = 100000000
    for button in buttons:
        new_state = apply_button(light, button)
        num_presses = traverse(new_state, buttons)
        if num_presses != -1:
            min_presses = min(min_presses, num_presses + 1)
    visited.remove(light)
    if min_presses == 100000000:
        return -1
    return min_presses

res = 0
for i in range(len(lights)):
    res += traverse(lights[i], buttons[i])
print(res)
