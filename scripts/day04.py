import re

with open("inputs/input04.txt", "r") as input:
    cards = [
        re.sub(r"\s+", " ", x).split(": ")[1].split(" | ") 
        for x in input.read().rstrip().split("\n")
    ]

cards = [
    {
        "winning_numbers": set([int(x) for x in card[0].split(" ")]),
        "your_numbers": set([int(x) for x in card[1].split(" ")]),
    }
    for card in cards
]

matches = [
    len(card["winning_numbers"] & card["your_numbers"])
    for card in cards
]

# part 1 ----
points = 0
for match in matches:
    if match == 0:
        pass
    else:
        points += 2**(match - 1)
        
print(points)


# part 2 ----
card_counts = {i+1: 1 for i, card in enumerate(cards)}
for i, match in enumerate(matches):
    card_id = i + 1
    card_count = card_counts[card_id]
    for x in range(match):
        card_counts[card_id + x + 1] += card_count
        
print(sum([card_count for card_count in card_counts.values()]))
