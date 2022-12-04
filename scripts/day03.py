with open("inputs/input03.txt", "r") as input:
    rucksacks = [x for x in input.read().rstrip().split("\n")]

from string import ascii_lowercase, ascii_uppercase

letters = ascii_lowercase + ascii_uppercase

# part 1 ----
priorities = []
for rucksack in rucksacks:
    half = int(len(rucksack) / 2)
    first_half  = rucksack[:half]
    second_half = rucksack[half:]

    overlap = list(set(first_half) & set(second_half))[0]
    priority = prio.index(overlap) + 1
    priorities.append(priority)

print(sum(priorities))


# part 2 ----
priorities = []
for i in range(0, len(rucksacks), 3):
    overlap = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))[0]
    priority = prio.index(overlap) + 1
    priorities.append(priority)

print(sum(priorities))
