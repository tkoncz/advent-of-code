with open("inputs/input7.txt", "r") as input:
    positions = [int(x) for x in input.read().rstrip().split(",")]

print("1 -------")
min([
    sum([abs(pos1 - pos2) for pos2 in positions])
    for pos1 in range(1, max(positions) + 1)
])

print("2 -------")
min([
    sum([sum(range(abs(pos1 - pos2) + 1)) for pos2 in positions])
    for pos1 in range(1, max(positions) + 1)
])
