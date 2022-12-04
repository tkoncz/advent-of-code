def input_parser(line: str) -> list:
    return ([
        [int(x) for x in assignment.split('-')]
        for assignment in line.split(',')
    ])


with open("inputs/input04.txt", "r") as input:
    assignments = [
        input_parser(line) for line in input.read().strip().split('\n')
    ]

part1_counter = 0
part2_counter = 0
for assignment in assignments:
    sections_1 = set(range(assignment[0][0], assignment[0][1] + 1))
    sections_2 = set(range(assignment[1][0], assignment[1][1] + 1))

    if sections_1.issubset(sections_2) or sections_2.issubset(sections_1):
        part1_counter += 1
    
    if sections_1 & sections_2:
        part2_counter += 1


# part1 ----
print(part1_counter)

# part2 ----
print(part2_counter)
