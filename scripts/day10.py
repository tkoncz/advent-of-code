with open("inputs/input10.txt", "r") as input:
    instructions = input.read().rstrip().split('\n')


# part 1
cycle = 0
value_x = 1
signal_strenghts = {}
for inst in instructions:
    cycle += 1
    signal_strenghts[cycle] = cycle * value_x

    if inst != 'noop':
        cycle += 1
        signal_strenghts[cycle] = cycle * value_x
        chg = int(inst[5:])
        value_x += chg

print(sum([signal_strenghts[x] for x in [20, 60, 100, 140, 180, 220]]))


# part 2
grid = [[' ' for i in range(40)] for j in range(6)]
cycle = 0
value_x = 1

for inst in instructions:
    if (cycle % 40) in list(range(value_x - 1, value_x + 2)):
        grid[cycle // 40][cycle % 40] = '|'

    cycle += 1

    if inst != 'noop':
        if (cycle % 40) in list(range(value_x - 1, value_x + 2)):
            grid[cycle // 40][cycle % 40] = '|'
        
        cycle += 1
    
        chg = int(inst[5:])
        value_x += chg

for row in grid:
    print(''.join(row))
