from itertools import product

with open("inputs/day_17_conway_cubes_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')


def getValueForCoordinates(coordinates, state):
    try:
        value = state[coordinates]
    except KeyError as e:
        value = '.'

    return(value)


def convertStrCoordinatesToList(str_coordinates):
    return(list(map(
        int, str_coordinates.replace('[', '').replace(']','').split(',')
    )))


def addTwoLists(list_a, list_b):
    return([a + b for a, b in zip(list_a, list_b)])

## part 1

len_x = len(lines[0]) # col
len_y = len(lines)    # row
len_z = 3

initial_state = {}
for x in range(0, len_x):
    for y in range(0, len_y):
        coordinates = str([x, y, 0])
        initial_state[coordinates] = lines[y][x]

# initialize all neighbours shifts (3D)
all_neighbour_shifts = list(map(list, product([-1, 0, 1], repeat = 3)))
all_neighbour_shifts.remove([0, 0, 0])

# -----------------
old_state = initial_state

for i in range(0, 6):
    new_state = {}

    # calculate coordinates to cover in a given round (expanding the grid in each round)
    all_coordinates = [
        convertStrCoordinatesToList(str_coordinates)
        for str_coordinates in old_state.keys()
    ]
    x_coordinates = [coordinates[0] for coordinates in all_coordinates]
    min_x, max_x = (min(x_coordinates), max(x_coordinates))
    y_coordinates = [coordinates[1] for coordinates in all_coordinates]
    min_y, max_y = (min(y_coordinates), max(y_coordinates))
    z_coordinates = [coordinates[2] for coordinates in all_coordinates]
    min_z, max_z = (min(z_coordinates), max(z_coordinates))

    coordinates_to_cover = list(map(list, product(
        range(min_x - 1, max_x + 1 + 1),
        range(min_y - 1, max_y + 1 + 1),
        range(min_z - 1, max_z + 1 + 1)
    )))

    # count number of active neighbours for each coordinate
    for coordinates in coordinates_to_cover:
        # print("-------------------------")
        # print(coordinates)

        active_neighbours = 0
        for coordinate_shift in all_neighbour_shifts:
            # print(coordinate_shift)
            neighbour_coordinates = str(addTwoLists(coordinates, coordinate_shift))
            # print(neighbour_coordinates)
            old_value = getValueForCoordinates(neighbour_coordinates, old_state)
            # print(old_value)
            if old_value == "#":
                active_neighbours += 1

        old_value = getValueForCoordinates(str(coordinates), old_state)
        if old_value == "#" and active_neighbours in [2, 3]:
            new_state[str(coordinates)] = "#"
        elif old_value == "." and active_neighbours == 3:
            new_state[str(coordinates)] = "#"
        else:
            new_state[str(coordinates)] = "."

    old_state = new_state


print(sum([1 for value in old_state.values() if value == '#']))
# 207


## part 2

initial_state = {}
for x in range(0, len_x):
    for y in range(0, len_y):
        coordinates = str([x, y, 0, 0])
        initial_state[coordinates] = lines[y][x]

# initialize all neighbours shifts (4D)
all_neighbour_shifts = list(map(list, product([-1, 0, 1], repeat = 4)))
all_neighbour_shifts.remove([0, 0, 0, 0])

# -----------------
old_state = initial_state

for i in range(0, 6):
    new_state = {}

    # calculate coordinates to cover in a given round (expanding the grid in each round)
    all_coordinates = [
        convertStrCoordinatesToList(str_coordinates)
        for str_coordinates in old_state.keys()
    ]
    x_coordinates = [coordinates[0] for coordinates in all_coordinates]
    min_x, max_x = (min(x_coordinates), max(x_coordinates))
    y_coordinates = [coordinates[1] for coordinates in all_coordinates]
    min_y, max_y = (min(y_coordinates), max(y_coordinates))
    z_coordinates = [coordinates[2] for coordinates in all_coordinates]
    min_z, max_z = (min(z_coordinates), max(z_coordinates))
    f_coordinates = [coordinates[3] for coordinates in all_coordinates]
    min_f, max_f = (min(f_coordinates), max(f_coordinates))

    coordinates_to_cover = list(map(list, product(
        range(min_x - 1, max_x + 1 + 1),
        range(min_y - 1, max_y + 1 + 1),
        range(min_z - 1, max_z + 1 + 1),
        range(min_f - 1, max_f + 1 + 1)
    )))

    # count number of active neighbours for each coordinate
    for coordinates in coordinates_to_cover:
        # print("-------------------------")
        # print(coordinates)

        active_neighbours = 0
        for coordinate_shift in all_neighbour_shifts:
            # print(coordinate_shift)
            neighbour_coordinates = str(addTwoLists(coordinates, coordinate_shift))
            # print(neighbour_coordinates)
            old_value = getValueForCoordinates(neighbour_coordinates, old_state)
            # print(old_value)
            if old_value == "#":
                active_neighbours += 1

        old_value = getValueForCoordinates(str(coordinates), old_state)
        if old_value == "#" and active_neighbours in [2, 3]:
            new_state[str(coordinates)] = "#"
        elif old_value == "." and active_neighbours == 3:
            new_state[str(coordinates)] = "#"
        else:
            new_state[str(coordinates)] = "."

    old_state = new_state


print(sum([1 for value in old_state.values() if value == '#']))
# 2308
