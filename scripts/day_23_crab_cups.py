from itertools import compress
from collections import deque

input = '327465189'

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


# part 2
cups = [int(d) for d in input]
total_cups =  1_000_000
additional_cups = [cup for cup in range(max(cups) + 1, (total_cups + 1))]
cups = cups + additional_cups
num_cups = len(cups)

cups_dict = {cups[i]: cups[(i + 1) % num_cups] for i in range(0, num_cups)}
current_cup = cups[0]
for i in range(0, 10_000_000):
    # print(' ------------------------------------ ')
    # print(f'current cup: {current_cup}')

    pickup_cup_1 = cups_dict[current_cup]
    pickup_cup_2 = cups_dict[pickup_cup_1]
    pickup_cup_3 = cups_dict[pickup_cup_2]
    # print(f'pickups: {[pickup_cup_1, pickup_cup_2, pickup_cup_3]}')

    cup_after_pickups = cups_dict[pickup_cup_3]
    cups_dict[current_cup] = cup_after_pickups
    # print(f'cup after pickups: {cup_after_pickups}')

    destination_cup = getDestinationCup(
        current_cup, [pickup_cup_1, pickup_cup_2, pickup_cup_3], num_cups
    )
    # print(f'destination cup: {destination_cup}')

    cups_dict[pickup_cup_3] = cups_dict[destination_cup]
    cups_dict[destination_cup] = pickup_cup_1

    current_cup = cup_after_pickups

print(cups_dict[1] * cups_dict[cups_dict[1]])
# 474600314018
