with open("inputs/day_1_report_repair_input.txt", "r") as input:
    lines = list(map(int, input.read().split('\n')[:-1]))

num_lines = len(lines)

# part 1
for i in range(num_lines):
    for j in range(i, num_lines):
        if lines[i] + lines[j] == 2020:
            print(lines[i] * lines[j])
# 1016619

# part 2
for i in range(num_lines):
    for j in range(i, num_lines):
        for k in range(j, num_lines):
            if lines[i] + lines[j] + lines[k] == 2020:
                print(lines[i] * lines[j] * lines[k])
# 218767230
