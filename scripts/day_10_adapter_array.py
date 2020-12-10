import re
from itertools import groupby

with open("inputs/day_10_adapter_array_input.txt", "r") as input:
    lines = list(map(int, input.read().rstrip().split('\n')))

lines.sort()

extended_lines = [0]
extended_lines.extend(lines)
device = max(lines) + 3
extended_lines.append(device)

jolt_diffs = [
    extended_lines[i] - extended_lines[i-1]
    for i in range(1, len(extended_lines))
]

three_jolt_diffs = sum([i == 3 for i in jolt_diffs])
one_jolt_diffs = sum([i == 1 for i in jolt_diffs])

print(one_jolt_diffs * three_jolt_diffs)
# 2484

# part 2 - recursive method
def getNumberOfWays(position, ordered_jolts):
    if position == len(ordered_jolts) - 1:
        return(1)

    if position in already_processed:
        return(already_processed[position])

    number_of_ways = 0
    for i in range(position + 1, len(ordered_jolts)):
        if ordered_jolts[i] - ordered_jolts[position] <= 3:
            number_of_ways += getNumberOfWays(i, ordered_jolts)

    already_processed[position] = number_of_ways
    return(number_of_ways)

already_processed = {}
print(getNumberOfWays(0, extended_lines))
# 15790581481472

# part 2 - Feri's solution - props!
# seq_ones = [
#     len(x) for x in re.sub('3+', '3', str(jolt_diffs)[1:-1].replace(', ', '')).split('3')
# ]

# seq_ones.sort()

# num_seq_ones = {key: len(list(group)) for key, group in groupby(seq_ones)}
# del num_seq_ones[0]

# print(pow(2, num_seq_ones[2]) * pow(4, num_seq_ones[3]) * pow(7, num_seq_ones[4]))
