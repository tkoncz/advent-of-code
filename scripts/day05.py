def parse_moves(moves: str) -> list:
    parsed_moves = []

    for move in moves.split('\n'):
        from_index = move.find('from')
        to_index   = move.find('to')

        n = int(move[5:(from_index - 1)])
        f = int(move[(from_index + 5):(to_index - 1)])
        t = int(move[(to_index + 3):])

        parsed_moves.append({
            'from': f,
            'to': t,
            'n': n
        })

    return parsed_moves


def parse_stacks(stacks: str) -> list:
    tmp = stacks.rstrip().split('\n')
    stack_lines, stack_indecies = tmp[:-1], tmp[-1:][0]
    last_stack = int(stack_indecies[-1:])

    stacks = {}
    for i in range(last_stack):
        if i == 0:
            lookup_index = 1
        else:
            lookup_index = 1 + i * 4

        stack = []
        for stack_line in stack_lines:
            crate = stack_line[lookup_index]
            if crate != ' ':
                stack.append(stack_line[lookup_index])

        stacks[i + 1] = stack

    return stacks


with open("inputs/input05.txt", "r") as input:
    raw_stacks, raw_moves = input.read().rstrip().split("\n\n")


# part 1
moves = parse_moves(raw_moves)
stacks = parse_stacks(raw_stacks)

for move in moves:
    f = move['from']
    t = move['to']
    n = move['n']

    crates_to_move = stacks[f][:n]
    crates_to_move.reverse() # part 1 v part 2 diff -- too lazy to refactor
    stacks[f] = stacks[f][n:]

    stacks[t] = crates_to_move + stacks[t]


print(''.join([v[0] for v in stacks.values()]))


# part 2
moves = parse_moves(raw_moves)
stacks = parse_stacks(raw_stacks)

for move in moves:
    f = move['from']
    t = move['to']
    n = move['n']

    crates_to_move = stacks[f][:n]
    # crates_to_move.reverse() # part 1 v part 2 diff -- too lazy to refactor
    stacks[f] = stacks[f][n:]

    stacks[t] = crates_to_move + stacks[t]


print(''.join([v[0] for v in stacks.values()]))
