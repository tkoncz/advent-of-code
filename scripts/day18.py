import numpy as np


def calc_surface(cubes: set) -> int:
    surface = 0
    for cube in cubes:
        sides = get_sides(cube)
        cube_uncovered_sides = len(set(sides) - cubes)
        surface += cube_uncovered_sides

    return(surface)


def get_sides(cube: tuple) -> [tuple]:
    sides = [
        np.array((0, 0,  1)),
        np.array((0, 0, -1)),
        np.array((0, 1,  0)),
        np.array((0, -1, 0)),
        np.array((1,  0, 0)),
        np.array((-1, 0, 0)),
    ]

    cube = np.array(cube)
    side_cubes = [
        tuple(cube + side)
        for side in sides
    ]

    return side_cubes


def safe_max(a: np.array) -> int:
    if len(a) > 0:
        return int(max(a))
    else:
        return 0


with open("inputs/input18.txt", "r") as input:
    cubes = set([eval(f'({x})') for x in input.read().rstrip().split('\n')])


# part 1
print(calc_surface(cubes))

# part 2
# first create an x * y * z grid, where 1 marks if there's a cube in that grid point
x, y, z = set(), set(), set()
for cube in cubes:
    x.add(cube[0])
    y.add(cube[1])
    z.add(cube[2])

    grid = np.zeros((max(x), max(y), max(z)))
    for x_ in x:
        for y_ in y:
            for z_ in z:
                grid[(x_ - 1, y_ - 1, z_ - 1)] = int((x_, y_, z_) in cubes)


# then check for inner cubes by exploring each cubes outer x, y, z axes
inner_cubes = set()
for x__ in x:
    for y__ in y:
        for z__ in z:

            x_ = x__ - 1
            y_ = y__ - 1
            z_ = z__ - 1

            if min(
                # x axis
                safe_max(grid[:x_, y_, z_]),
                safe_max(grid[(x_ + 1):, y_, z_]),
                # y axis
                safe_max(grid[x_, :y_, z_]),
                safe_max(grid[x_, (y_ + 1):, z_]),
                # z axis
                safe_max(grid[x_, y_, :z_]),
                safe_max(grid[x_, y_, (z_ + 1):]),
            ) == 1:
                inner_cube_to_add = tuple([x__, y__, z__])
                inner_cubes.add(inner_cube_to_add)


# add inner cubes to the object ("fill inside")
filled_cubes = cubes | inner_cubes


print(calc_surface(filled_cubes))
