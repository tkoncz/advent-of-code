from itertools import compress
from collections import deque

input = '389125467'

# part 1
def moveCups(cups, current_cup_id, num_cups):
    # print(f'cups: {cups}')

    current_cup  = cups[current_cup_id]
    # print(f'current cup: {current_cup}')

    pick_up_cup_ids = list(map(
        lambda x: x % num_cups,
        range((current_cup_id + 1), (current_cup_id + 4))
    ))
    pick_up_cups = [cups[cup_id] for cup_id in pick_up_cup_ids]
    # print(f'pick up cups: {pick_up_cups}')

    mask = [1] * num_cups
    mask[pick_up_cup_ids[0]] = 0
    mask[pick_up_cup_ids[1]] = 0
    mask[pick_up_cup_ids[2]] = 0
    remaining_cups = list(compress(cups, mask))
    # print(f'remaining cup: {remaining_cups}')

    destination_cup_index = remaining_cups.index(
        getDestinationCup(current_cup, pick_up_cups, num_cups)
    )


    reordered_cups =  deque(
        remaining_cups[:(destination_cup_index + 1)] +
        pick_up_cups +
        remaining_cups[(destination_cup_index + 1):]
    )
    # print(f'pre reo: {reordered_cups}')

    reordered_current_cup_index = reordered_cups.index(current_cup)
    reordered_cups.rotate((current_cup_id - reordered_current_cup_index))
    reordered_cups = list(reordered_cups)
    # print(f'post reo: {reordered_cups}')

    return(reordered_cups)

def getDestinationCup(current_cup, pick_up_cups, num_cups):
    destination_cup = current_cup - 1
    if destination_cup < 1:
            destination_cup = num_cups

    while destination_cup in pick_up_cups:
        destination_cup = destination_cup - 1

        if destination_cup < 1:
            destination_cup = num_cups

    return(destination_cup)

#
cups = [int(d) for d in input]
num_cups = len(cups)
for move in range(0, 100):
    # print(f'-------- {move + 1} --------')
    current_cup_id = move % num_cups
    cups = moveCups(cups, current_cup_id, num_cups)

starting_index = cups.index(1)
final_cup_order = ''.join([
    str(cups[i % 9]) for i in range(starting_index + 1, starting_index + 9)
])

print(final_cup_order)
# 82934675
