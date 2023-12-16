with open("inputs/input16.txt", "r") as input:
    layout = [list(x) for x in input.read().rstrip().split("\n")]


DIRECTIONS = {
    (-1, 0): "up",
    (0, 1): "right",
    (1, 0): "down",
    (0, -1): "left",
}

NUM_ROW = len(layout)
NUM_COL = len(layout[0])


def calculateNumberOfVisitedLocations(
    starting_point: tuple,
    starting_direction: str,
) -> int:
    r, c = starting_point
    direction = [k for k, v in DIRECTIONS.items() if v == starting_direction][0]
    beams = [[r, c, direction]]

    visited_locations = []
    while beams:
        r, c, direction = beams.pop()
        if (r, c, direction) not in visited_locations:
            visited_locations += [(r, c, direction)]
            
            if (
                layout[r][c] == "."
                or (DIRECTIONS[direction] in ["left", "right"] and layout[r][c] == "-")
                or (DIRECTIONS[direction] in ["up", "down"] and layout[r][c] == "|")
            ):
                if (
                    0 <= r + direction[0] < NUM_ROW
                    and 0 <= c + direction[1] < NUM_COL
                ):
                    beams.append([r + direction[0], c + direction[1], direction])
            
            # splits
            elif DIRECTIONS[direction] in ["left", "right"] and layout[r][c] == "|":
                if 0 <= r - 1 < NUM_ROW: beams.append([r - 1, c, (-1, 0)])
                if 0 <= r + 1 < NUM_ROW: beams.append([r + 1, c, ( 1, 0)])
            elif DIRECTIONS[direction] in ["up", "down"] and layout[r][c] == "-":
                if 0 <= c - 1 < NUM_COL: beams.append([r, c - 1, (0, -1)])
                if 0 <= c + 1 < NUM_COL: beams.append([r, c + 1, (0,  1)])
            
            # mirrors: /
            elif DIRECTIONS[direction] == "up" and layout[r][c] == "/":
                if 0 <= c + 1 < NUM_COL: beams.append([r, c + 1, (0, 1)])
            elif DIRECTIONS[direction] == "down" and layout[r][c] == "/":
                if 0 <= c - 1 < NUM_COL: beams.append([r, c - 1, (0, -1)])
            elif DIRECTIONS[direction] == "left" and layout[r][c] == "/":
                if 0 <= r + 1 < NUM_COL: beams.append([r + 1, c, (1, 0)])
            elif DIRECTIONS[direction] == "right" and layout[r][c] == "/":
                if 0 <= r - 1 < NUM_COL: beams.append([r - 1, c, (-1, 0)])
            
            # mirrors: \
            elif DIRECTIONS[direction] == "up" and layout[r][c] == "\\":
                if 0 <= c - 1 < NUM_COL: beams.append([r, c - 1, (0, -1)])
            elif DIRECTIONS[direction] == "down" and layout[r][c] == "\\":
                if 0 <= c + 1 < NUM_COL: beams.append([r, c + 1, (0, 1)])
            elif DIRECTIONS[direction] == "left" and layout[r][c] == "\\":
                if 0 <= r - 1 < NUM_COL: beams.append([r - 1, c, (-1, 0)])
            elif DIRECTIONS[direction] == "right" and layout[r][c] == "\\":
                if 0 <= r + 1 < NUM_COL: beams.append([r + 1, c, (1, 0)])
            
    return len(set([(r,c) for r,c, _ in visited_locations]))


# part 1 ----
print(calculateNumberOfVisitedLocations((0, 0), "right"))


# part 2 ----
starts = []
starts += [(0, c, "down") for c in range(NUM_COL)]
starts += [(NUM_ROW - 1, c, "up") for c in range(NUM_COL)]
starts += [(r, 0, "right") for r in range(NUM_ROW)]
starts += [(r, NUM_COL - 1, "left") for r in range(NUM_COL)]

energized_tiles = [
    calculateNumberOfVisitedLocations((r, c), direction)
    for r, c, direction in starts
]

print(max(energized_tiles))