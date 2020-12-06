with open("inputs/day_6_custom_customs_input.txt", "r") as input:
    lines = list(input.read().rstrip().split('\n\n'))

groups = [l.split('\n') for l in lines]

# part 1
sum_unique_letters = 0

for group in groups:
    if len(group) == 1:
        unique_letters = [letter for letter in group[0]]
    else:
        unique_letters = []
        for person in group:
            person_letters = [letter for letter in person]
            new_letters = list(set(person_letters) - set(unique_letters))
            unique_letters.extend(new_letters)

    sum_unique_letters += len(unique_letters)

print(sum_unique_letters)

# part 2
sum_common_letters = 0

for group in groups:
    if len(group) == 1:
        common_letters = [letter for letter in group[0]]
    else:
        common_letters = [letter for letter in group[0]]
        for person in group[1:]:
            person_letters = [letter for letter in person]
            common_letters = list(set(person_letters) & set(common_letters))

    sum_common_letters += len(common_letters)

print(sum_common_letters)
