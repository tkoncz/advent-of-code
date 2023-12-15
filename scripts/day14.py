from functools import cache


@cache
def tilt(dish, direction):
    dish = [list(x) for x in dish.split("\n")]
    
    num_rows = len(dish)
    num_cols = len(dish[0])
    
    if direction == "n":
        for r in range(1, num_rows, 1):
            for c in range(num_cols):
                if dish[r][c] == "O":
                    d = 1
                    while r - d >= 0 and dish[r-d][c] == ".":
                        dish[r-d][c] = "O"
                        dish[r-d+1][c] = "."
                        d += 1
    elif direction == "s":
        for r in range(num_rows-2, -1, -1):
            for c in range(num_cols):
                if dish[r][c] == "O":
                    d = 1
                    while r + d <= num_rows - 1 and dish[r+d][c] == ".":
                        dish[r+d][c] = "O"
                        dish[r+d-1][c] = "."
                        d += 1
    elif direction == "e":
        for r in range(num_rows):
            for c in range(num_cols-2, -1, -1):
                if dish[r][c] == "O":
                    d = 1
                    while c + d <= num_rows - 1 and dish[r][c+d] == ".":
                        dish[r][c+d] = "O"
                        dish[r][c+d-1] = "."
                        d += 1
    elif direction == "w":
        for r in range(num_rows):
            for c in range(1, num_cols, 1):
                if dish[r][c] == "O":
                    d = 1
                    while c - d >= 0 and dish[r][c-d] == ".":
                        dish[r][c-d] = "O"
                        dish[r][c-d+1] = "."
                        d += 1
                        
    return "\n".join(["".join(x) for x in dish])


with open("inputs/input14.txt", "r") as input:
    dish = input.read().rstrip()

dish = tilt(dish, "n")

dish = [list(x) for x in dish.split("\n")]
num_row = len(dish)

print(sum([(num_row - r) for r, row in enumerate(dish) for col in row if col == "O"]))

# part 2 ----
with open("inputs/input14.txt", "r") as input:
    dish = input.read().rstrip()
   

for i in range(1_000_000_000):
    for direction in ["n", "w", "s", "e"]:
        dish = tilt(dish, direction)

    if i % 1_000_000 == 0: 
        print(i / 1_000_000)

print(sum([
    (num_row - r) for r, row in 
    enumerate([list(x) for x in dish.split("\n")]) for col in row if col == "O"
]))
