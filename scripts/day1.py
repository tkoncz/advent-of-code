with open("inputs/input1.txt", "r") as input:
    input = [int(x) for x in input]


cnt = 0
for i, val in enumerate(input):
    if i >= 1:
        if val > input[i-1]:
            cnt += 1

print("1 -------")
print(cnt)


cnt = 0
for i, val in enumerate(input):
    if i >= 3:
        curr = sum(input[i-2:i+1])
        prev = sum(input[i-3:i])
        if curr > prev:
            cnt += 1

print("2 -------")
print(cnt)
