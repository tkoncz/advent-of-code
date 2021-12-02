with open("inputs/input2.txt", "r") as input:
    input = [x.split(" ") for x in input.read().rstrip().split("\n")]


coord = [0, 0]
for x in input:
    if x[0] == "forward":
        coord[0] += int(x[1])
    if x[0] == "down":
        coord[1] += int(x[1])
    if x[0] == "up":
        coord [1] -= int(x[1])

print("1 -------")
print(coord[0] * coord[1])


coord = [0, 0, 0]
for x in input:
    if x[0] == "forward":
        coord[0] += int(x[1])
        coord[1] += coord[2] * int(x[1])
    if x[0] == "down":
        coord[2] += int(x[1])
    if x[0] == "up":
        coord[2] -= int(x[1])

print("2 -------")
print(coord[0] * coord[1])
