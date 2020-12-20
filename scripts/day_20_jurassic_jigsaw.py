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

    edge_1 = tile[0]
    edge_2 = ''
    for row in range(0, num_rows):
        edge_2 += tile[row][num_cols - 1]
    edge_3 = tile[num_rows - 1]
    edge_4 = ''
    for row in range(0, num_rows):
        edge_4 += tile[row][0]

    return([edge_1, edge_2, edge_3, edge_4])

def reverseString(str):
    return(str[::-1])

tile_edges = {}
for tile_id, tile in tiles.items():
    tile_edges[tile_id] = getEdges(tile)

tile_edge_matches = {}
for tile_id, edges in tile_edges.items():
    reverse_edges = list(map(reverseString, edges))

    num_neighbours = 0
    for tile_id2, edges2 in tile_edges.items():

        if tile_id != tile_id2:
            num_matching_edges = max(
                len(set(edges) & set(edges2)),
                len(set(reverse_edges) & set(edges2))
            )
            if num_matching_edges == 1:
                num_neighbours += 1

    tile_edge_matches[tile_id] = num_neighbours

# ----
answer = 1
for tile_id, num_matching_edges in tile_edge_matches.items():
    if num_matching_edges == 2:
        answer *= tile_id

print(answer)
# 14129524957217
