import numpy as np

with open("inputs/day_5_binary_boarding_input.txt", "r") as input:
    lines = list(input.read().rstrip().split('\n'))

# part 1
seating = [{'row': l[0:7], 'col':l[7:10]} for l in lines]

seat_ids = []

for s in seating:
    rows = np.array(range(0, 128))
    for r in s['row']:
        middle = np.median(rows)
        if r == 'B':
            rows = rows[rows > middle]
        if r == 'F':
            rows = rows[rows < middle]
    row = int(rows)

    cols = np.array(range(0, 8))
    for c in s['col']:
        middle = np.median(cols)
        if c == 'R':
            cols = cols[cols > middle]
        if c == 'L':
            cols = cols[cols < middle]
    col = int(cols)

    seat_id = row * 8 + col
    seat_ids.append(seat_id)

print(max(seat_ids))

# part 2
all_seat_ids = list(range(min(seat_ids), max(seat_ids) + 1))

print(set(all_seat_ids) - set(seat_ids))
