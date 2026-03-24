def read_str_grid(input="input.txt"):
    grid = []
    with open(input, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
