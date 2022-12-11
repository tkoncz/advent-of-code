with open("inputs/input08.txt", "r") as input:
    input = input.read().rstrip().split('\n')

num_cols = len(input[0])
num_rows = len(input)

trees = [[int(col) for col in row] for row in input]

# part 1
num_visible_trees = 0
for row in list(range(num_rows))[1:-1]:
    for col in list(range(num_cols))[1:-1]:
        tree = trees[row][col]

        left  = tree > max(trees[row][:col])
        right = tree > max(trees[row][(col+1):])
        up    = tree > max([row[col] for row in trees[:row]])
        down  = tree > max([row[col] for row in trees[(row+1):]])

        visible = max([left, right, up, down])
        if visible:
            num_visible_trees += 1

num_trees_edges = (2 * num_rows) + (2 * (num_cols - 2))
print(num_visible_trees + num_trees_edges)


# part 2
def get_first_bigger_tree_dist(trees: [], tree: int) -> int:
    distances = [dist for dist, size in enumerate(trees) if size >= tree]
    if len(distances) == 0:
        return(len(trees))
    else:
        return distances[0] + 1

scores = []
for row in list(range(num_rows))[1:-1]:
    for col in list(range(num_cols))[1:-1]:
        tree = trees[row][col]

        left  = get_first_bigger_tree_dist(list(reversed(trees[row][:col])),                  tree)
        right = get_first_bigger_tree_dist(trees[row][(col+1):],                              tree)
        up    = get_first_bigger_tree_dist(list(reversed([row[col] for row in trees[:row]])), tree)
        down  = get_first_bigger_tree_dist([row[col] for row in trees[(row+1):]],             tree)

        score = left * right * up * down
        scores.append(score)


print(max(scores))
