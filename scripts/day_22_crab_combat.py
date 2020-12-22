from hashlib import md5

with open("inputs/day_22_crab_combat_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n\n')

# part 1
def parseLinesToCards(lines):
    cards = {}
    for i in [1, 2]:
        cards[i] = list(
            map(int, lines[i - 1].replace(f'Player {i}:\n', '').split('\n'))
        )

    return(cards)

def playRound(player_1_cards, player_2_cards):
    if player_1_cards[0] > player_2_cards[0]:
        player_1_cards = player_1_cards[1:] + [player_1_cards[0], player_2_cards[0]]
        player_2_cards = player_2_cards[1:]
    else:
        player_2_cards = player_2_cards[1:] + [player_2_cards[0], player_1_cards[0]]
        player_1_cards = player_1_cards[1:]

    return((player_1_cards, player_2_cards))


def calculateScore(winner_cards):
    num_all_cards = len(winner_cards)

    return(
        sum([card * (num_all_cards - card_id)
             for card_id, card in enumerate(winner_cards)])
    )


cards = parseLinesToCards(lines)

num_all_cards = len(cards[1]) + len(cards[2])

i = 1
some_has_all_cards = False
while some_has_all_cards == False:
    # print(f'----- Round: {i} -----')

    cards[1], cards[2] = playRound(cards[1], cards[2])

    # print(cards[1])
    # print(cards[2])

    if len(cards[1]) == num_all_cards:
        print('Player 1 has won!')
        winner = 1
        some_has_all_cards = True
        break

    if len(cards[2]) == num_all_cards:
        print('Player 2 has won!')
        winner = 2
        some_has_all_cards = True
        break

    i += 1

print(calculateScore(cards[winner]))
# 33393


# part 2
def calculateWinnerFromCards(player_1_cards, player_2_cards):
    num_all_cards = len(player_1_cards) + len(player_2_cards)

    hashed_rounds = []

    i = 1
    some_has_all_cards = False
    while some_has_all_cards == False:
        # print(f'----- Round: {i} -----')

        round_hash = hashCurrentCards(player_1_cards, player_2_cards)
        if round_hash in hashed_rounds:
            # print('Player 1 has won! (infinite loop)')
            return((1, player_1_cards))
        else:
            hashed_rounds.append(round_hash)


        player_1_card = player_1_cards[0]
        player_2_card = player_2_cards[0]
        num_remaining_cards_player_1 = len(player_1_cards[1:])
        num_remaining_cards_player_2 = len(player_2_cards[1:])

        if (player_1_card <= num_remaining_cards_player_1 and
            player_2_card <= num_remaining_cards_player_2):
            # print('--- Recursive Combat ---')

            player_1_deck = player_1_cards[1:(player_1_card + 1)]
            player_2_deck = player_2_cards[1:(player_2_card + 1)]

            # print(player_1_deck)
            # print(player_2_deck)

            sub_game_winner, sub_game_winner_cards = calculateWinnerFromCards(
                player_1_deck, player_2_deck
            )
            if sub_game_winner == 1:
                player_1_cards = player_1_cards[1:] + [player_1_cards[0], player_2_cards[0]]
                player_2_cards = player_2_cards[1:]
            else:
                player_2_cards = player_2_cards[1:] + [player_2_cards[0], player_1_cards[0]]
                player_1_cards = player_1_cards[1:]
        else:
            player_1_cards, player_2_cards = playRound(
                player_1_cards, player_2_cards
            )

        # print(player_1_cards)
        # print(player_2_cards)

        if len(player_1_cards) == num_all_cards:
            # print('Player 1 has won!')
            return((1, player_1_cards))

        if len(player_2_cards) == num_all_cards:
            # print('Player 2 has won!')
            return((2, player_2_cards))

        i += 1


def hashCurrentCards(player_1_cards, player_2_cards):
    rounds_hash = (
        md5(str(player_1_cards).encode()).hexdigest() + '_' +
        md5(str(player_2_cards).encode()).hexdigest()
    )

    return(rounds_hash)


cards = parseLinesToCards(lines)
winner, winner_cards = calculateWinnerFromCards(cards[1], cards[2])

print(calculateScore(winner_cards))
# 31963
