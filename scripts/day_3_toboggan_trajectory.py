import math

with open("inputs/day_3_toboggan_trajectory_input.txt", "r") as input:
    lines = list(input.read().split('\n')[:-1])

extended_lines = [l * 3 * math.ceil(len(lines) / len(lines[0])) for l in lines]

# part 1
num_trees = 0

row = 0
col = 0
while row < len(extended_lines):
    if extended_lines[row][col] == "#":
        num_trees += 1

    row = row + 1
    col = col + 3

print(num_trees)

# part 2
slopes = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}
]

num_trees_multiplied = 1
for s in slopes:
    num_trees = 0
    row = 0
    col = 0
    right = s["right"]
    down = s["down"]

    extended_lines = [
        l * math.ceil(right / down) * math.ceil(len(lines) / len(lines[0]))
        for l in lines
    ]

    while row < len(extended_lines):
        if extended_lines[row][col] == "#":
            num_trees += 1

        row += down
        col += right

    print(num_trees)
    num_trees_multiplied = num_trees_multiplied * num_trees

print(num_trees_multiplied)
