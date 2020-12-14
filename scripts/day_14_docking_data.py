import re
from itertools import product

with open("inputs/day_14_docking_data_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

# part 1
def convertDecimalToBinary(decimal):
    binary = bin(decimal).replace('0b', '')
    return(binary)


def overrideBinaryWithMask(binary, mask):
    if len(binary) != len(mask):
        raise Exception("'binary' and 'mask' should be the same length!")

    masked_binary = ''
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            masked_binary += binary[i]
        else:
            masked_binary += mask[i]

    return(masked_binary)

instructions = []
for l in lines:
    if l[0:4] == 'mask':
        instructions.append({'mask': l[7:]})
    elif l[0:3] == "mem":
        decimal = int(re.match('^mem\\[\\d+\\] = (\\d+)$', l).group(1))
        instructions.append({
            'memory': {
                'address': re.match('^mem\\[(\\d+)\\] = \\d+$', l).group(1),
                'decimal': decimal,
                'binary': convertDecimalToBinary(decimal).rjust(36, '0')
            }
        })
    else:
        raise Exception(f"Couldn't parse input: {l}")


memory_contents = {}
for inst in instructions:
    if 'mask' in inst.keys():
        mask = inst['mask']
    elif 'memory' in inst.keys():
        binary = overrideBinaryWithMask(inst['memory']['binary'], mask)
        memory_contents[inst['memory']['address']] = binary
    else:
        raise Exception(f'Incorrect instruction: {inst}')

decimal_values_in_memory = [
    int(binary, 2)
    for binary in memory_contents.values()
]

print(sum(decimal_values_in_memory))
# 3059488894985


# part 2
def applyMaskToBinary(binary, mask):
    if len(binary) != len(mask):
        raise Exception("'binary' and 'mask' should be the same length!")

    masked_binary = ''
    for i in range(0, len(mask)):
        if mask[i] == '0':
            masked_binary += binary[i]
        elif mask[i] == '1':
            masked_binary += '1'
        else:
            masked_binary += 'X'

    return(masked_binary)

memory_contents = {}
for inst in instructions:
    if 'mask' in inst.keys():
        mask = inst['mask']
    elif 'memory' in inst.keys():
        binary_of_address = convertDecimalToBinary(
            int(inst['memory']['address'])
        ).rjust(36, '0')
        binary = applyMaskToBinary(binary_of_address, mask)
        # print("----------------------")
        # print(binary_of_address)
        # print(mask)
        # print(binary)
        memory_contents[binary] = inst['memory']['decimal']
    else:
        raise Exception(f'Incorrect instruction: {inst}')

memory_contents_unmasked = {}
for masked_address, decimal in memory_contents.items():
    x_positions = [i for i in range(0, len(masked_address)) if masked_address[i] == 'X']
    num_x = len(x_positions)
    x_product = list(product(['0', '1'], repeat = num_x))

    for comb in x_product:
        address = masked_address
        for i, j in zip(x_positions, range(0, num_x)):
            tmp_address = address[:i] + comb[j]
            if i < len(masked_address):
                tmp_address += address[i + 1:]
            address = tmp_address

        memory_contents_unmasked[address] = decimal


print(sum([decimal for decimal in memory_contents_unmasked.values()]))
# 2900994392308
