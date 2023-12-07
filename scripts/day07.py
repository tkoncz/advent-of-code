from collections import Counter


with open("inputs/input07.txt", "r") as input:
    hands, bids = zip(*[x.split(" ") for x in input.read().rstrip().split("\n")])
    bids = [int(x) for x in bids]

# part 1 ----
CARD_VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

def calculateHandValue(hand: str) -> tuple:
    hand_values = {
        # max, diff
        (5, 1): 7, # 5 of a kind
        (4, 2): 6, # 4 of a kind
        (3, 2): 5, # full-house
        (3, 3): 4, # 3 of a kind
        (2, 3): 3, # 2 pairs
        (2, 4): 2, # 1 pair
        (1, 5): 1, # high card
    }
    
    card_values = [int(CARD_VALUES.get(x, x)) for x in hand]
    num_max, num_diff = (max(Counter(hand).values()), len(Counter(hand).values()))
    return (hand_values[(num_max, num_diff)], *card_values)


hands_sorted_w_bids = sorted(
    [(*calculateHandValue(hand), bid) for hand, bid in zip(hands, bids)]
)
print(sum([(r + 1) * x[-1] for r, x in enumerate(hands_sorted_w_bids)]))


# part 2 ----
CARD_VALUES["J"] = 1

def calculateHandValuePartTwo(hand: str) -> tuple:
    card_values = [int(CARD_VALUES.get(x, x)) for x in hand]
    
    cntr = Counter(hand)
    num_j = cntr.get("J", 0)
    if num_j not in [0, 5]:
        hand = hand.replace("J", [x[0] for x in cntr.most_common(2) if x[0] != "J"][0])
        
    return (calculateHandValue(hand)[0], *card_values)

hands_sorted_w_bids = sorted(
    [(*calculateHandValuePartTwo(h), b) for h, b in zip(hands, bids)]
)
print(sum([(r + 1) * x[-1] for r, x in enumerate(hands_sorted_w_bids)]))