with open("inputs/input1.txt", "r") as input:
    elfs = [cals.split('\n') for cals in input.read().rstrip().split("\n\n")]
    elfs = [[int(cal) for cal in elf] for elf in elfs]

elf_calories = [sum(elf) for elf in elfs]
elf_calories.sort(reverse=True)

# part 1 ----
print(elf_calories[0])

# part 2 ----
print(sum(elf_calories[0:3]))

