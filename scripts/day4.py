with open("inputs/input4.txt", "r") as input:
    bingo_numbers = [int(i) for i in input.readline().rstrip().split(',')]
    temp_boards = input.read().rstrip().split('\n')

board_num_rows = 0
boards = []
board = []
for line in temp_boards:
    if line != "":
        board.append([int(i) for i in line.split(' ') if i != ''])

        if len(board) == 5:
            boards.append(board)
            board = []

def calculateWinners(bingo_numbers, boards):
    marked_boards = [[[0, 0, 0, 0, 0] for i in range(5)] for board in boards]
    winner_boards = []
    draws_at_wins = []
    for draw in bingo_numbers:
        for board_id, board in enumerate(boards):
            for line_id, line in enumerate(board):
                for num_id, num in enumerate(line):
                    if board_id not in winner_boards:
                        if num == draw:
                            marked_boards[board_id][line_id][num_id] = 1

        for board_id, board in enumerate(marked_boards):
            # check rows
            for line_id, line in enumerate(board):
                total_marks_in_line = sum(line)
                if total_marks_in_line == 5:
                    if board_id not in winner_boards:
                        winner_boards.append(board_id)
                        draws_at_wins.append(draw)

            # check cols
            for col_id in range(5):
                total_marks_in_col = sum([line[col_id] for line in board])
                if total_marks_in_col == 5:
                    if board_id not in winner_boards:
                        winner_boards.append(board_id)
                        draws_at_wins.append(draw)

    return(winner_boards, draws_at_wins, marked_boards)


winner_boards, draws_at_wins, marked_boards = calculateWinners(
    bingo_numbers, boards
)

winner_board = winner_boards[0]
sum_unmarked_on_winner_board = sum([
    sum([
        val for col_id, val in enumerate(line)
        if marked_boards[winner_board][line_id][col_id] == 0
    ]) for line_id, line in enumerate(boards[winner_board])
])

print("1 -------")
print(sum_unmarked_on_winner_board * draws_at_wins[0])


last_winner_board = winner_boards[-1]
sum_unmarked_on_last_winner_board = sum([
    sum([
        val for col_id, val in enumerate(line)
        if marked_boards[last_winner_board][line_id][col_id] == 0
    ]) for line_id, line in enumerate(boards[last_winner_board])
])

print("2 -------")
print(sum_unmarked_on_last_winner_board * draws_at_wins[-1])
