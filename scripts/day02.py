import re


with open("inputs/input02.txt", "r") as input:
    games = [g.split(": ")[1] for g in input.read().rstrip().split("\n")]
    games = [g.split("; ") for g in games]

PATTERN = r"(\d+) blue|(\d+) red|(\d+) green"


# part 1 ----
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

valid_games = []
for game_id, game  in enumerate(games):
    is_valid = True
    for s in game:
        matches = re.findall(PATTERN, s)
        num_blue  = int(next((m[0] for m in matches if m[0] != ""), "0"))
        num_red   = int(next((m[1] for m in matches if m[1] != ""), "0"))
        num_green = int(next((m[2] for m in matches if m[2] != ""), "0"))
        
        if (
            num_blue > LIMITS["blue"] or 
            num_green > LIMITS["green"] or
            num_red > LIMITS["red"]
        ):
            is_valid = False
            break
    if is_valid:
        valid_games.append(game_id + 1)
        
print(sum(valid_games))


# part 2 ----
powers = []
for game_id, game  in enumerate(games):
    min_blue, min_red, min_green = (0, 0, 0)
    for s in game:
        matches = re.findall(PATTERN, s)
        num_blue  = int(next((m[0] for m in matches if m[0] != ""), "0"))
        num_red   = int(next((m[1] for m in matches if m[1] != ""), "0"))
        num_green = int(next((m[2] for m in matches if m[2] != ""), "0"))
        
        min_blue = max([min_blue, num_blue])
        min_red = max([min_red, num_red])
        min_green = max([min_green, num_green])
        
    power = min_blue * min_red * min_green
    powers.append(power)

print(sum(powers))