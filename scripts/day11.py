def adjacentSteps():
    steps = [
        {"row": -1, "col": -1},
        {"row": -1, "col":  0},
        {"row": -1, "col":  1},
        {"row":  0, "col": -1},
        {"row":  0, "col":  1},
        {"row":  1, "col": -1},
        {"row":  1, "col":  0},
        {"row":  1, "col":  1},
    ]

    return steps


with open("inputs/input11.txt", "r") as input:
    octopuses = [[int(x) for x in y] for y in input.read().rstrip().split("\n")]

n_rows = len(octopuses)
n_cols = len(octopuses[0])

last_step = 100

flashing_octopuses = []
full_flash_steps = []
step = 0

while not(step >= last_step and len(full_flash_steps) > 0):
    flashing_octopuses_to_process = []
    # iterate over each octopus
    for row in range(n_rows):
        for col in range(n_cols):
            if octopuses[row][col] != -1: octopuses[row][col] += 1

            if octopuses[row][col] > 9:
                flashing_octopuses_to_process.append({"row": row, "col": col})
                flashing_octopuses.append({"step": step, "row": row, "col": col})
                octopuses[row][col] = -1

    # handle adj flashes
    while len(flashing_octopuses_to_process) > 0:
        octopus = flashing_octopuses_to_process.pop(0)
        for adj_step in adjacentSteps():
            adj_row = octopus["row"] + adj_step["row"]
            adj_col = octopus["col"] + adj_step["col"]

            if (adj_row >= 0 and adj_row < n_rows) and (adj_col >= 0 and adj_col < n_cols):
                if octopuses[adj_row][adj_col] != -1:
                    octopuses[adj_row][adj_col] += 1

                if octopuses[adj_row][adj_col] > 9:
                    flashing_octopuses_to_process.append(
                        {"row": adj_row, "col": adj_col}
                    )
                    flashing_octopuses.append(
                        {"step": step, "row": row, "col": col}
                    )
                    octopuses[adj_row][adj_col] = -1

    # cleanup
    num_flashes_in_step = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if octopuses[row][col] == -1:
                octopuses[row][col] = 0
                num_flashes_in_step += 1

    if num_flashes_in_step == 100:
        full_flash_steps.append(step)

    step += 1


print("1 -------")
print(sum([1 for flash in flashing_octopuses if flash["step"] < last_step]))

print("2 -------")
print(full_flash_steps[0] + 1)
