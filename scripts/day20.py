def step_through(start_key: int, steps: int, llist: dict) -> int:
    end_key = start_key
    for ii in range(steps):
        end_key = llist[end_key]['next_key']

    return end_key


def llist_to_str(llist):
    next_key = list(llist.keys())[0]
    to_print = []
    i = 0
    while i < LEN_INPUT:
        data = llist[next_key]['data']
        next_key = llist[next_key]['next_key']
        to_print.append(str(data))
        i += 1

    return(', '.join(to_print))


with open("inputs/input20.txt", "r") as input:
    input = [int(x) for x in input.read().rstrip().split('\n')]


LEN_INPUT = len(input)

# key-data pairs will remain fixed --> only the next_key will change
llist = {}
for key, data in enumerate(input):
    next_key = (key + 1) % (LEN_INPUT)
    llist[key] = {'data': data, 'next_key': next_key}


# print(llist_to_str(llist))

for key, data in enumerate(input):
    # key #input[move]
    next_key = llist[key]['next_key']
    if data != 0:
        if data > 0:
            steps = data - 1
        else:
            steps = LEN_INPUT + data - 2
    
        # step through to find the place where i will move
        key_to_move_after = step_through(next_key, steps, llist)
        # print(f'{key=}, {data=}, {next_key=}')

        prev_key = [k for k, v in llist.items() if v['next_key'] == key][0] # grab the key which was previusly pointing to the current key

        llist[key]['next_key'] = llist[key_to_move_after]['next_key']
        llist[key_to_move_after]['next_key'] = key
        llist[prev_key]['next_key'] = next_key

    # print(f'{data} --->', llist_to_str(llist))


zero_key = [k for k, v in llist.items() if v['data'] == 0][0]

print(
    llist[step_through(zero_key, 1_000, llist)]['data'] + 
    llist[step_through(zero_key, 2_000, llist)]['data'] + 
    llist[step_through(zero_key, 3_000, llist)]['data']
)
