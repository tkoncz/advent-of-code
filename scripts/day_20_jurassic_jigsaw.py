from math import sqrt

with open("inputs/day_20_jurassic_jigsaw_input.txt", "r") as input:
    input = input.read().rstrip().split('\n\n')

tiles = {}
for tile in input:
    tile_rows = tile.split('\n')
    tile_id = tile_rows[0].replace('Tile ', '').replace(':', '')
    tiles[int(tile_id)] = tile_rows[1:]

# part 1
def getEdges(tile):
    num_rows = len(tile)
    num_cols = len(tile[0])

    edge_top = tile[0]
    edge_right = ''
    for row in range(0, num_rows):
        edge_right += tile[row][num_cols - 1]
    edge_bottom = tile[num_rows - 1]
    edge_left = ''
    for row in range(0, num_rows):
        edge_left += tile[row][0]

    return([edge_top, edge_right, edge_bottom, edge_left])

def reverseString(str):
    return(str[::-1])

tile_edges = {}
for tile_id, tile in tiles.items():
    tile_edges[tile_id] = getEdges(tile)

tile_edge_matches = {}
for tile_id, edges in tile_edges.items():
    reverse_edges = list(map(reverseString, edges)) # by rotating, the order of elements in a tile can be reversed

    num_neighbours = 0
    matching_edges = []
    for tile_id2, edges2 in tile_edges.items():

        if tile_id != tile_id2:
            shared_edges = list(set(edges + reverse_edges) & set(edges2))
            if len(shared_edges) == 1:
                matching_edges.append(shared_edges[0]) # only 1 edge can match between two tiles, hence the subset

    tile_edge_matches[tile_id] = {
        'num_matching_edges': len(matching_edges),
        'matching_edges': matching_edges
    }


# ----
answer = 1
for tile_id, matching_edges in tile_edge_matches.items():
    if matching_edges['num_matching_edges'] == 2:
        answer *= tile_id

print(answer)
# 14129524957217

# part 2
def rotateTileRight(tile):
    rows = list(range(0, len(tile)))
    cols = list(range(0, len(tile[0])))

    rotated_tile = []
    for row in rows:
        new_col = ''
        for col in cols:
            new_col += tile[max(cols) - col][row]
        rotated_tile.append(new_col)

    return(rotated_tile)


def flipTileHorizontally(tile):
    rows = list(range(0, len(tile)))
    cols = list(range(0, len(tile[0])))

    flipped_tile = []
    for row in rows:
        new_col = ''
        for col in cols:
            new_col += tile[row][max(cols) - col]
        flipped_tile.append(new_col)

    return(flipped_tile)


def getTileWithMatchingEdge(tile_id_to_skip, edge, tile_edge_matches):
    tile_found = False

    for tile_id, matching_edges in tile_edge_matches.items():
        # should we check for reverse as well? probably yes
        if (edge in matching_edges['matching_edges'] or
            reverseString(edge) in matching_edges['matching_edges']):
            if tile_id != tile_id_to_skip:
                tile_found = True
                return((tile_id, tiles[tile_id]))

    if tile_found == False:
        raise Exception("Couldn't find matching tile to 'edge' and 'tile_id_to_skip'")


# orienting the first tile!
first_tile_id = [
    tile_id for tile_id, matching_edges
    in tile_edge_matches.items() if matching_edges['num_matching_edges'] == 2
][0]

first_tile_found = False
first_tile = tiles[first_tile_id]
tile_matching_edges = tile_edge_matches[first_tile_id]['matching_edges']
for i in range(0, 4):
    edges = getEdges(first_tile)
    if ((edges[1] in tile_matching_edges or reverseString(edges[1]) in tile_matching_edges) and
        (edges[2] in tile_matching_edges or reverseString(edges[2]) in tile_matching_edges)):
        first_tile_found = True
        break
    else:
        first_tile = rotateTileRight(first_tile)

if first_tile_found == False:
    raise Exception("Problem with 'first_tile'")


# find everything else
edge_length = int(sqrt(len(tile_edge_matches)))
row = 0
col = 1
image_rows_tile_ids = [[first_tile_id]]
image_rows_tiles = [[first_tile]]
while row <= edge_length - 1 and col <= edge_length - 1:
    if col > 0:
        right_edge_to_match = getEdges(image_rows_tiles[row][col - 1])[1]
        tile_id_w_matching_edge, tile_w_matching_edge = getTileWithMatchingEdge(
            tile_id_to_skip = image_rows_tile_ids[row][col - 1],
            edge = right_edge_to_match,
            tile_edge_matches = tile_edge_matches
        )

        # rotate tile to correct position
        tile_correctly_aligned = False
        for i in range(0, 4):
            left_edge = getEdges(tile_w_matching_edge)[3]
            if left_edge == right_edge_to_match:
                tile_correctly_aligned = True
                break

            flipped_tile_w_matching_edge = flipTileHorizontally(tile_w_matching_edge)
            left_edge = getEdges(flipped_tile_w_matching_edge)[3]
            if left_edge == right_edge_to_match:
                tile_correctly_aligned = True
                tile_w_matching_edge = flipped_tile_w_matching_edge
                break

            tile_w_matching_edge = rotateTileRight(tile_w_matching_edge)

        if tile_correctly_aligned == False:
            raise Exception("Can't find correct tile alignment")

        # add to image
        image_rows_tile_ids[row].append(tile_id_w_matching_edge)
        image_rows_tiles[row].append(tile_w_matching_edge)
    else:
        bottom_edge_to_match = getEdges(image_rows_tiles[row - 1][col])[2]
        tile_id_w_matching_edge, tile_w_matching_edge = getTileWithMatchingEdge(
            tile_id_to_skip = image_rows_tile_ids[row - 1][col],
            edge = bottom_edge_to_match,
            tile_edge_matches = tile_edge_matches
        )

        # rotate tile to correct position
        tile_correctly_aligned = False
        for i in range(0, 4):
            top_edge = getEdges(tile_w_matching_edge)[0]
            if top_edge == bottom_edge_to_match:
                tile_correctly_aligned = True
                break

            flipped_tile_w_matching_edge = flipTileHorizontally(tile_w_matching_edge)
            top_edge = getEdges(flipped_tile_w_matching_edge)[0]
            if top_edge == bottom_edge_to_match:
                tile_correctly_aligned = True
                tile_w_matching_edge = flipped_tile_w_matching_edge
                break

            tile_w_matching_edge = rotateTileRight(tile_w_matching_edge)

        if tile_correctly_aligned == False:
            raise Exception("Can't find correct tile rotation")

        # add to image
        image_rows_tile_ids[row].append(tile_id_w_matching_edge)
        image_rows_tiles[row].append(tile_w_matching_edge)

    # if the last column is reached, jump to the beginning of next row
    if col == edge_length - 1 and row < edge_length - 1:
        row += 1
        col = 0
        image_rows_tile_ids.append([])
        image_rows_tiles.append([])

    # otherwise just jump to the next col
    else:
        col += 1

# remove edges and combine tiles into 1 image
def removeEdgesFromTile(tile):
    rows = list(range(1, len(tile) - 1))
    cols = list(range(1, len(tile[0]) - 1))

    tile_wo_edges = []
    for row in rows:
        new_col = ''
        for col in cols:
            new_col += tile[row][col]

        tile_wo_edges.append(new_col)

    return(tile_wo_edges)


num_image_rows = len(image_rows_tiles)
num_image_cols = len(image_rows_tiles[0])
num_tile_rows = len(removeEdgesFromTile(image_rows_tiles[0][0]))
num_tile_cols = len(removeEdgesFromTile(image_rows_tiles[0][0][0]))

image = ['' for i in range(0, num_image_rows * num_tile_rows)]
# iterating over tiles in the image
for img_row in range(0, num_image_rows):
    for img_col in range(0, num_image_cols):
        tile = removeEdgesFromTile(image_rows_tiles[img_row][img_col])

        # iterating over a tile
        for tile_row in range(0, num_tile_rows):
            current_image_row = (img_row * num_tile_rows) + tile_row
            image[current_image_row] += tile[tile_row]

# let's find them sea monsters shall we!
sea_monster_pattern = [
    '__________________#_',
    '#____##____##____###',
    '_#__#__#__#__#__#___'
]

sm_hashtag_locations = []
for sm_row in range(0, 3):
    for sm_col in range(0, 20):
        if sea_monster_pattern[sm_row][sm_col] == '#':
            sm_hashtag_locations.append({'sm_row': sm_row, 'sm_col': sm_col})


last_image_row = len(image) - len(sea_monster_pattern)
last_image_col = len(image[0]) - len(sea_monster_pattern[0])

num_sea_monsters = 0
for row in range(0, last_image_row):
    for col in range(0, last_image_col):
        slice_to_check = [
            image[row][col:(col + 20)],
            image[row + 1][col:(col + 20)],
            image[row + 2][col:(col + 20)]
        ]

        # check slice for seamonster
        sea_monster_found = True
        for loc in sm_hashtag_locations:
            if slice_to_check[loc['sm_row']][loc['sm_col']] != '#':
                sea_monster_found = False
                break

        if sea_monster_found == True:
            num_sea_monsters += 1

# and finally calculate the answer...
num_hashtags = 0
image_rows = range(0, len(image))
image_cols = range(0, len(image[0]))
for row in image_rows:
    for col in image_cols:
        if image[row][col] == '#':
            num_hashtags += 1

print(num_hashtags - num_sea_monsters * 15)
