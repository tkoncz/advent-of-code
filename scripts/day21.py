with open("inputs/input21.txt", "r") as input:
    input = input.read().rstrip().split('\n')

player_1_pos = int(input[0][-1])
player_2_pos = int(input[1][-1])

class Dice:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = list(range(1, num_sides + 1))

    def get_value(self, index):
        index = index % self.num_sides
        return(self.sides[index - 1])

dice = Dice(100)

dice_index = 1
player_1_score, player_2_score = 0, 0

while True:
    player_1_pos = (player_1_pos + sum(range(dice_index, dice_index + 3, 1))) % 10
    if player_1_pos == 0: player_1_pos = 10
    player_1_score += player_1_pos
    dice_index += 3
    if player_1_score >= 1000: break

    player_2_pos = (player_2_pos + sum(range(dice_index, dice_index + 3, 1))) % 10
    if player_2_pos == 0: player_2_pos = 10
    player_2_score += player_2_pos
    dice_index += 3
    if player_2_score >= 1000: break


lower_score = min(player_1_score, player_2_score)
num_rolls = dice_index - 1

print("1 -------")
print(lower_score * num_rolls)


###
from collections import Counter

roll_combinations = [
    [1,1,1], [1,1,2], [1,1,3],
    [1,2,1], [1,2,2], [1,2,3],
    [1,3,1], [1,3,2], [1,3,3],
    [2,1,1], [2,1,2], [2,1,3],
    [2,2,1], [2,2,2], [2,2,3],
    [2,3,1], [2,3,2], [2,3,3],
    [3,1,1], [3,1,2], [3,1,3],
    [3,2,1], [3,2,2], [3,2,3],
    [3,3,1], [3,3,2], [3,3,3]
]

step_size_num_times = dict(Counter([sum(i) for i in roll_combinations]))

unfinished_worlds = [{
    "p1_pos": int(input[0][-1]),
    "p2_pos": int(input[1][-1]),
    "p1_score": 0,
    "p2_score": 0,
    "num_copies": 1
}]

wins = {"p1": 0, "p2": 0}

while len(unfinished_worlds) > 0:
    # print("unfinished worlds: ", len(unfinished_worlds))
    # print("wins: ", wins)
    new_unfinished_worlds = []
    for world_state in unfinished_worlds:
        for p1_step_size, p1_num_times in step_size_num_times.items():
            num_copies = world_state["num_copies"] * p1_num_times

            p1_pos = (world_state["p1_pos"] + p1_step_size) % 10
            if p1_pos == 0: p1_pos = 10
            p1_score = world_state["p1_score"] + p1_pos

            if p1_score >= 21:
                wins["p1"] += num_copies
            else:
                for p2_step_size, p2_num_times in step_size_num_times.items():
                        p2_num_copies = num_copies * p2_num_times

                        p2_pos = (world_state["p2_pos"] + p2_step_size) % 10
                        if p2_pos == 0: p2_pos = 10
                        p2_score = world_state["p2_score"] + p2_pos

                        if p2_score >= 21:
                            wins["p2"] += p2_num_copies
                        else:
                            new_unfinished_worlds.append({
                                "p1_pos": p1_pos,
                                "p2_pos": p2_pos,
                                "p1_score": p1_score,
                                "p2_score": p2_score,
                                "num_copies": p2_num_copies
                            })

    unfinished_worlds = new_unfinished_worlds

print("2 -------")
print(max(wins.values()))
