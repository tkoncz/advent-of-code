with open("inputs/day_11_seating_system_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

# part 1
def recalcSeating(old_seating):
    num_rows = len(old_seating)
    num_cols = len(old_seating[0])
    new_seating = [[] for row in old_seating]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            new_seating[row].append(calcNewSeatStatus(row, col, old_seating))

    return(new_seating)


def calcNewSeatStatus(row, col, old_seating):
    if old_seating[row][col] == '.':
        return('.')

    num_rows = len(old_seating)
    num_cols = len(old_seating[0])

    num_occupied_seats = 0
    for r in [row - 1, row, row + 1]:
        for c in [col - 1, col, col + 1]:
            if (0 <= r <= num_rows - 1) and (0 <= c <= num_cols - 1):
                if old_seating[r][c] == '#':
                    num_occupied_seats += 1

    if old_seating[row][col] == 'L' and num_occupied_seats == 0:
        return('#')
    elif old_seating[row][col] == '#' and num_occupied_seats >= 5:
        # num_occupied_seats >= 5 --> in this solution, we'll add old_seating[row][col] (= "#") to the total, hence using 5 not 4
        return('L')
    else:
        return(old_seating[row][col])

def calcNumberOfOccupiedSeats(seating):
    num_occupied_seats = 0
    for row in seating:
        num_occupied_seats += sum([1 for seat in row if seat == '#'])

    return(num_occupied_seats)


seating = lines
num_occupied_seats_changes = True
old_num_occupied_seats = 0

while num_occupied_seats_changes == True:
    seating = recalcSeating(seating)
    new_num_occupied_seats = calcNumberOfOccupiedSeats(seating)

    print("-----------------------")
    print("old: {} --> new: {}".format(
        old_num_occupied_seats, new_num_occupied_seats
    ))

    if new_num_occupied_seats == old_num_occupied_seats:
        print("!!! seating stabilized at {} seats".format(new_num_occupied_seats))
        num_occupied_seats_changes = False

    old_num_occupied_seats = new_num_occupied_seats

# answer: 2468

# part 2
def recalcSeating(old_seating):
    num_rows = len(old_seating)
    num_cols = len(old_seating[0])
    new_seating = [[] for row in old_seating]

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            new_seating[row].append(calcNewSeatStatus(row, col, old_seating))

    return(new_seating)


def calcNewSeatStatus(row, col, old_seating):
    if old_seating[row][col] == '.':
        return('.')

    num_rows = len(old_seating)
    num_cols = len(old_seating[0])

    num_occupied_seats = 0
    row_directions = [-1, 0, 1]
    col_directions = [-1, 0, 1]

    for row_dir in row_directions:
        for col_dir in col_directions:
            # print("----------------")
            # print("row dir: {}, col dir: {}".format(row_dir, col_dir))
            if row_dir == 0 and col_dir == 0:
                # print("skipping")
                num_occupied_seats += 0
            else:
                r = row + row_dir
                c = col + col_dir
                seat_found = False
                while not seat_found and (0 <= r <= num_rows - 1) and (0 <= c <= num_cols - 1):
                    if old_seating[r][c] == '#':
                        # print("# found: row: {}, col: {}".format(r, c))
                        num_occupied_seats += 1
                        seat_found = True
                    elif old_seating[r][c] == 'L':
                        # print("L found: row: {}, col: {}".format(r, c))
                        seat_found = True
                    else:
                        # print("seat not found: row: {}, col: {}".format(r, c))
                        r += row_dir
                        c += col_dir

    if old_seating[row][col] == 'L' and num_occupied_seats == 0:
        return('#')
    elif old_seating[row][col] == '#' and num_occupied_seats >= 5:
        return('L')
    else:
        return(old_seating[row][col])


seating = lines
num_occupied_seats_changes = True
old_num_occupied_seats = 0

while num_occupied_seats_changes == True:
    seating = recalcSeating(seating)
    new_num_occupied_seats = calcNumberOfOccupiedSeats(seating)

    print("-----------------------")
    print("old: {} --> new: {}".format(
        old_num_occupied_seats, new_num_occupied_seats
    ))

    if new_num_occupied_seats == old_num_occupied_seats:
        print("!!! seating stabilized at {} seats".format(new_num_occupied_seats))
        num_occupied_seats_changes = False

    old_num_occupied_seats = new_num_occupied_seats

# answer: 2214
