with open("inputs/input5.txt", "r") as input:
    input = [x.split(" -> ") for x in input.read().rstrip().split("\n")]

lines = [[[int(x) for x in j.split(",")] for j in i] for i in input]

x_max = max([coords[0] for line in lines for coords in line])
y_max = max([coords[1] for line in lines for coords in line])

grid = [[0 for x in range(x_max + 1)] for y in range(y_max + 1)]

# ----
lines_to_keep = [
    line for line in lines
    if (line[0][0] == line[1][0] or line[0][1] == line[1][1])
]

for line in lines_to_keep:
    x0, x1 = min(line[0][0], line[1][0]), max(line[0][0], line[1][0])
    y0, y1 = min(line[0][1], line[1][1]), max(line[0][1], line[1][1])

    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            grid[y][x] += 1

print("1 -------")
print(sum([1 for line in grid for coord in line if coord > 1]))

# ----
lines_not_to_keep = [
    line for line in lines
    if not (line[0][0] == line[1][0] or line[0][1] == line[1][1])
]

for line in lines_not_to_keep:
    x0, x1 = line[0][0], line[1][0]
    y0, y1 = line[0][1], line[1][1]

    x_step = -1 if x0 >= x1 else 1
    y_step = -1 if y0 >= y1 else 1

    for x, y in zip(range(x0, x1 + x_step, x_step), range(y0, y1 + y_step, y_step)):
        grid[y][x] += 1

print("2 -------")
print(sum([1 for line in grid for coord in line if coord > 1]))
