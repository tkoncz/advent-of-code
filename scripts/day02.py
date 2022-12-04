with open("inputs/input02.txt", "r") as input:
    rounds = [x.split(" ") for x in input.read().rstrip().split("\n")]

# part 1 ----
def calc_score(first, second):
    if second == 'X':
        score = 1
        if first == 'A': score += 3
        if first == 'B': score += 0
        if first == 'C': score += 6
    if second == 'Y':
        score = 2
        if first == 'A': score += 6
        if first == 'B': score += 3
        if first == 'C': score += 0
    if second == 'Z':
        score = 3
        if first == 'A': score += 0
        if first == 'B': score += 6
        if first == 'C': score += 3

    return score

print(sum([calc_score(round[0], round[1]) for round in rounds]))

# part 2 ----
def calc_score2(first, second):
    # lose
    if second == 'X':
        score = 0
        if first == 'A': score += 3
        if first == 'B': score += 1
        if first == 'C': score += 2
    # draw
    if second == 'Y':
        score = 3
        if first == 'A': score += 1
        if first == 'B': score += 2
        if first == 'C': score += 3
    # win
    if second == 'Z':
        score = 6
        if first == 'A': score += 2
        if first == 'B': score += 3
        if first == 'C': score += 1

    return score

print(sum([calc_score2(round[0], round[1]) for round in rounds]))
