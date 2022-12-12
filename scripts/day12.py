from string import ascii_lowercase
import numpy as np

def is_coords_within_map(coords, nrows, ncols):
    if coords[0] >= nrows or coords[0] < 0:
        return False
    if coords[1] >= ncols or coords[1] < 0:
        return False

    return True


def find_loc_in_input(chr_to_find: str, input: [[str]]) -> [tuple]:
    return [
        (ln, cn) 
        for ln, line in enumerate(input) 
        for cn, x in enumerate(line) 
        if x == chr_to_find
    ]


with open("inputs/input12.txt", "r") as input:
    input = [[x for x in line] for line in input.read().rstrip().split('\n')]


end = find_loc_in_input('E', input)[0]

letter_mapping = {l: n for n, l in enumerate(ascii_lowercase)}
height_map = np.array([[letter_mapping.get(x, 0) for x in line] for line in input])
height_map[end] = ascii_lowercase.index('z')

nrows, ncols = height_map.shape

up_left_down_right = [
    np.array([-1, 0]),
    np.array([0, +1]),
    np.array([1,  0]),
    np.array([0, -1]),
]


# part 1
neighbour_coords = {}
for row in range(nrows):
    for col in range(ncols):
        coords = (row, col)
        possible_neighbour_coords = [
            tuple(coords + step)
            for step in up_left_down_right 
            if is_coords_within_map(coords + step, nrows, ncols) == True
        ]

        current_height = height_map[coords]

        neighbour_coords[coords] = [
            nc for nc in possible_neighbour_coords
            if height_map[nc] + 1 >= current_height
        ]

start = find_loc_in_input('S', input)[0]

dist_map = np.array([[np.Inf for col in range(ncols)] for row in range(nrows)])
dist_map[start] = 0

distances_updated = True
while distances_updated:
    distances_updated = False
    for row in range(nrows):
        for col in range(ncols):
            
            coords = (row, col)
            current_dist = dist_map[coords]
            
            if coords != start:
                distances = [
                    dist_map[nc] 
                    for nc in neighbour_coords[coords]
                ]
                dist = np.min(distances) + 1 if len(distances) > 0 else np.Inf

                if dist < current_dist:
                    distances_updated = True
                    dist_map[coords] = dist

print(int(dist_map[end]))


# part 2
neighbour_coords = {}
for row in range(nrows):
    for col in range(ncols):
        coords = (row, col)
        possible_neighbour_coords = [
            tuple(coords + step)
            for step in up_left_down_right 
            if is_coords_within_map(coords + step, nrows, ncols) == True
        ]

        current_height = height_map[coords]

        neighbour_coords[coords] = [
            nc for nc in possible_neighbour_coords
            if height_map[nc] <= current_height + 1
        ]

start = find_loc_in_input('E', input)[0]
ends = find_loc_in_input('a', input)

dist_map = np.array([[np.Inf for col in range(ncols)] for row in range(nrows)])
dist_map[end] = 0

distances_updated = True
while distances_updated:
    distances_updated = False
    for row in range(nrows):
        for col in range(ncols):
            
            coords = (row, col)
            current_dist = dist_map[coords]
            
            if coords != start:
                distances = [
                    dist_map[nc] 
                    for nc in neighbour_coords[coords]
                ]
                dist = np.min(distances) + 1 if len(distances) > 0 else np.Inf

                if dist < current_dist:
                    distances_updated = True
                    dist_map[coords] = dist

print(int(min(dist_map[end] for end in ends)))
