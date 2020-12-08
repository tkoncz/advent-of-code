import re

with open("inputs/day_8_input.txt", "r") as input:
    lines = input.read().split('\n')[:-1]

pattern = '^(nop|acc|jmp) ([+-]\\d+)$'

instructions = []
for l in lines:
    matches = re.match(pattern, l)
    instructions.append({
        'instruction': matches.group(1),
        'value':       int(matches.group(2)),
        'executed':    False
    })


# part 1
executed_instructions = [] # for part 2

acc = 0

i = 0
inf_loop_reached = False
while inf_loop_reached == False and i <= len(instructions):
    if instructions[i]['executed'] == True:
        print("vaa")
        inf_loop_reached = True
        break

    instructions[i]['executed'] = True

    executed_instructions.append(i)

    instruction = instructions[i]['instruction']
    if instruction == 'nop':
        i += 1
    elif instruction == 'acc':
        acc += instructions[i]['value']
        i += 1
    elif instruction == 'jmp':
        i += instructions[i]['value']
    else:
        print('Baj van - copyrigth fonok869')


print(acc)
# 1200

# part 2
fix_found = False
inst = 0
while fix_found == False and inst <= len(executed_instructions):

    # reset instructions
    for i in instructions: i['executed'] = False

    print('Trying to fix instruction {}'.format(inst))

    acc = 0
    i = 0
    inf_loop_reached = False
    last_line = len(instructions)

    while inf_loop_reached == False and i <= last_line:
        if instructions[i]['executed'] == True:
            print("Infinite loop for instruction {}".format(inst))
            inf_loop_reached = True
            break

        instructions[i]['executed'] = True

        instruction = instructions[i]['instruction']
        if i == executed_instructions[inst]:
            if instruction == 'jmp':
                print('Overriding "jmp" to "nop" instruction ({})'.format(inst))
                instruction = 'nop'
            elif instruction == 'nop':
                print('Overriding "nop" to "jmp" instruction ({})'.format(inst))
                instruction = 'jmp'

        if instruction == 'nop':
            i += 1
        elif instruction == 'acc':
            acc += instructions[i]['value']
            i += 1
        elif instruction == 'jmp':
            i += instructions[i]['value']
        else:
            print('Baj van - copyrigth fonok869')

        if i >= last_line:
            fix_found = True
            break

    inst += 1

print(acc)
