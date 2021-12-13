def getHeightFromCoords(x, y, heights):
    if y >= len(heights) or y < 0: return 10
    if x >= len(heights[y]) or x < 0: return 10
    return int(heights[y][x])


def findNeighbours(temp_coords, non_9s_coords):
    return([
        coords for coords in non_9s_coords
        if checkIfNeighbours(temp_coords, coords) == True
    ])


def checkIfNeighbours(coords1, coords2):
    x1, y1 = coords1[0], coords1[1]
    x2, y2 = coords2[0], coords2[1]

    if x1 == x2 and (y1 == y2 + 1 or y1 == y2 - 1): return True
    if y1 == y2 and (x1 == x2 + 1 or x1 == x2 - 1): return True

    return False


with open("inputs/input9.txt", "r") as input:
    heights = [x for x in input.read().rstrip().split("\n")]

low_points = []
for y, line in enumerate(heights):
    for x, height in enumerate(line):
        adjacent_heights = [
            getHeightFromCoords(x + 1, y, heights),
            getHeightFromCoords(x - 1, y, heights),
            getHeightFromCoords(x, y + 1, heights),
            getHeightFromCoords(x, y - 1, heights)
        ]

        if int(height) < min(adjacent_heights):
            low_points.append(int(height))

print("1 -------")
print(sum(low_points) + len(low_points))


# basins
non_9s_coords = [
    [x, y] for y, line in enumerate(heights)
    for x, height in enumerate(line)
    if int(height) != 9
]

basins = []
while len(non_9s_coords) > 0:
    temp_coords = non_9s_coords[0]
    non_9s_coords.pop(0)
    temp_basin = [temp_coords]
    pos_in_temp_basin = 0
    look_for_next = True
    while look_for_next == True:
        adjacent_coords = findNeighbours(
            temp_basin[pos_in_temp_basin], non_9s_coords
        )
        if len(adjacent_coords) > 0:
            for adj_coords in adjacent_coords:
                temp_basin.append(adj_coords)
                non_9s_coords.remove(adj_coords)
        else:
            pos_in_temp_basin += 1
            if pos_in_temp_basin >= len(temp_basin):
                basins.append(temp_basin)
                look_for_next = False

largets_three_basins = sorted([len(b) for b in basins])[-3:]

print("2 -------")
print(largets_three_basins[0] * largets_three_basins[1] * largets_three_basins[2])
