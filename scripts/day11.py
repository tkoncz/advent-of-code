from itertools import combinations


with open("inputs/input11.txt", "r") as input:
    images = [list(x) for x in input.read().rstrip().split("\n")]


galaxies = [
    (r,c) for r, row in enumerate(images) for c, col in enumerate(row) 
    if col == "#"
]
galaxy_pairs = list(combinations(galaxies, 2))

row_weights = [2 if all([x == "." for x in row]) else 1 for row in images]
col_weights = [
    2 if all([row[c] == "." for row in images]) else 1 
    for c, _ in enumerate(images[0])
]

# part 1 ----
distances = [
    abs(sum(row_weights[min(g1[0], g2[0]):max(g1[0], g2[0])])) + 
    abs(sum(col_weights[min(g1[1], g2[1]):max(g1[1], g2[1])]))
    for g1, g2 in galaxy_pairs
]

print(sum(distances))

# part 2 ----
row_weights = [1_000_000 if w == 2 else 1 for w in row_weights]
col_weights = [1_000_000 if w == 2 else 1 for w in col_weights]

distances = [
    abs(sum(row_weights[min(g1[0], g2[0]):max(g1[0], g2[0])])) + 
    abs(sum(col_weights[min(g1[1], g2[1]):max(g1[1], g2[1])]))
    for g1, g2 in galaxy_pairs
]

print(sum(distances))
