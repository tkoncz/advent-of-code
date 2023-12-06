import re
from functools import reduce


def solveQuadratic(a, b, c) -> float:
    # (-b +/- sqrt(b**2 - 4ac)) / 2a
    sol_1 = int((-b - (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a))
    sol_2 = int((-b + (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a))
    return (sol_1, sol_2)


with open("inputs/input06.txt", "r") as input:
    times, distances =[
        [int(y) for y in re.findall("\d+", x)] 
        for x in input.read().rstrip().split("\n")
    ]
    

# part 1 ----
ways_to_beat = []
for time, distance in zip(times, distances):
    wins = 0
    for hold in range(time)[1:]:
        speed = hold
        distance_travelled = speed * (time - hold)
        if distance_travelled > distance:
            wins += 1
    
    ways_to_beat.append(wins)
        
print(reduce(lambda x, y: x * y, ways_to_beat))


# part 2 ----
time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))

hold_min, hold_max = solveQuadratic(a=1, b=-time, c=distance)

print(int(hold_max - hold_min))
