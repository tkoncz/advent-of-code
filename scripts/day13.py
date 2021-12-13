def uniqueDots(dots_to_unique):
    unique_dots = []
    for dot in dots_to_unique:
        if dot not in unique_dots:
            unique_dots.append(dot)

    return(unique_dots)


def printCurrentState(dots):
    x_max = max([dot.get("x") for dot in dots])
    y_max = max([dot.get("y") for dot in dots])

    numbers = ''
    for y in range(y_max + 1):
        line = ''
        for x in range(x_max + 1):
            if {"x": x, "y": y} in dots:
                line += "#"
            else:
                line += "."

        numbers += line + "\n"

    print(numbers)


with open("inputs/input13.txt", "r") as input:
    input = input.read().rstrip().split("\n")

dots = []
folds = []
for x in input:
    if x[0:12] == "fold along y":
        folds.append({"y": int(x.replace("fold along y=", ""))})
    elif x[0:12] == "fold along x":
        folds.append({"x": int(x.replace("fold along x=", ""))})
    elif x != "":
        dots.append({
            "x": int(x.split(",")[0]),
            "y": int(x.split(",")[1])
        })


for fold_num, fold in enumerate(folds):
    fold_axis = list(fold.keys())[0]
    fold_value = list(fold.values())[0]

    new_dots = []
    for dot in dots:
        if dot.get(fold_axis) < fold_value:
            new_dots.append(dot)
        elif dot.get(fold_axis) != fold_value and fold_axis == "y":
            new_dot = {"x": dot.get("x"), "y": (2 * fold_value - dot.get("y"))}
            new_dots.append(new_dot)
        elif dot.get(fold_axis) != fold_value and fold_axis == "x":
            new_dot = {"x": (2 * fold_value - dot.get("x")), "y": dot.get("y")}
            new_dots.append(new_dot)

    dots = uniqueDots(new_dots)

    if fold_num == 0:
        print("1 -------")
        print(len(dots))

print("2 -------")
printCurrentState(dots)


###..#....###...##....##..##..#....#..#
#..#.#....#..#.#..#....#.#..#.#....#..#
#..#.#....###..#.......#.#....#....#..#
###..#....#..#.#.......#.#.##.#....#..#
#.#..#....#..#.#..#.#..#.#..#.#....#..#
#..#.####.###...##...##...###.####..##.
