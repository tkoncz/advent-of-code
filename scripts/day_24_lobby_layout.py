with open("inputs/day_24_lobby_layout_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

# part 1
def parseTileDirections(line):
    directions = ['ne', 'se', 'sw', 'nw', 'e', 'w']
    tmp = line
    tile_directions = []
    while len(tmp) > 0:
        for dir in directions:
            num_char = len(dir)
            if tmp[0:num_char] == dir:
                tile_directions.append(dir)
                tmp = tmp[num_char:]
                break

    return(tile_directions)


def translateTileDirection(tile_direction):
    tile_directions = {
        'ne': [1, 1],
        'se': [-1, 1],
        'sw': [-1, -1],
        'nw': [1, -1],
        'e':  [0, 2],
        'w':  [0, -2]
    }

    return(tile_directions[tile_direction])


def stepInDirection(current_location, direction):
    new_location = [
        current_location[0] + direction[0], current_location[1] + direction[1]
    ]

    return(new_location)


def isTileBlack(loc, black_tiles):
    try:
        tile_is_black = black_tiles[str(loc)]
    except KeyError as e:
        tile_is_black = False

    return(tile_is_black)


def countBlackTiles(black_tiles):
    return(sum([1 for is_black in black_tiles.values() if is_black == True]))


all_tile_directions = [parseTileDirections(line) for line in lines]

turned_tiles = []
for tile_directions in all_tile_directions:
    location = [0, 0]
    for step in tile_directions:
        location = stepInDirection(location, translateTileDirection(step))

    turned_tiles.append(location)

black_tiles = {}
for tile in turned_tiles:
    tile_is_black = isTileBlack(tile, black_tiles)

    if tile_is_black == True:
        black_tiles[str(tile)] = False
    else:
        black_tiles[str(tile)] = True

print(countBlackTiles(black_tiles))
# 424

# part 2
def convertStrLocToList(str_loc):
    return(list(map(int, str_loc.replace('[', '').replace(']','').split(','))))


neighbour_shifts = [
    translateTileDirection(dir) for dir in ['ne', 'se', 'sw', 'nw', 'e', 'w']
]


for i in range(0, 100):
    # print(f'---- Day: {i+1} ----')
    x_coordinates = [convertStrLocToList(loc)[0] for loc in black_tiles.keys()]
    min_x, max_x = (min(x_coordinates), max(x_coordinates))
    y_coordinates = [convertStrLocToList(loc)[1] for loc in black_tiles.keys()]
    min_y, max_y = (min(y_coordinates), max(y_coordinates))

    new_black_tiles = {}
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            loc = [x, y]
            tile_is_black = isTileBlack(loc, black_tiles)

            num_black_neighbours = 0
            for shift in neighbour_shifts:
                neighbour_loc = stepInDirection(loc, shift)
                if isTileBlack(neighbour_loc, black_tiles) == True:
                    num_black_neighbours += 1

            if (tile_is_black == True
                and (num_black_neighbours == 0 or num_black_neighbours > 2)):
                tile_is_black = False
            elif tile_is_black == False and num_black_neighbours == 2:
                tile_is_black = True

            new_black_tiles[str(loc)] = tile_is_black

    black_tiles = new_black_tiles
    # print(countBlackTiles(black_tiles))

print(countBlackTiles(black_tiles))
