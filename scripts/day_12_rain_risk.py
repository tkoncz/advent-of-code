with open("inputs/day_12_rain_risk_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

instructions = [{'action': l[0], 'value': int(l[1:])} for l in lines]

# part 1
def getNewDirectionId(current_direction_id, turn_direction, num_turns):
    if turn_direction == 'L':
        new_direction_id = (current_direction_id + num_turns) % 4
        if new_direction_id < 1:
            new_direction_id = 4 + new_direction_id
    elif turn_direction == 'R':
        new_direction_id = (current_direction_id + (4 - num_turns) % 4) % 4
        if new_direction_id == 0:
            new_direction_id = 4
    else:
        print("Incorrect value for 'turn_direction'")

    return(new_direction_id)


def getDirectionFromId(direction_id):
    directions = {1: [0, 1], 2: [1, 0], 3: [0, -1], 4: [-1, 0]}

    return(directions[direction_id])


direction_id = 1  # [0, 1]
position = [0, 0]

for inst in instructions:
    if inst['action'] == 'N':
        position[0] += inst['value']
    if inst['action'] == 'S':
        position[0] -= inst['value']
    if inst['action'] == 'E':
        position[1] += inst['value']
    if inst['action'] == 'W':
        position[1] -= inst['value']

    if inst['action'] in ['L', 'R']:
        num_turns = int(inst['value'] / 90)
        direction_id = getNewDirectionId(direction_id, inst['action'], num_turns)

    if inst['action'] == 'F':
        direction = getDirectionFromId(direction_id)
        position[0] += inst['value'] * direction[0]
        position[1] += inst['value'] * direction[1]

    print(position)

manhattan_distance = abs(position[0]) + abs(position[1])
print(manhattan_distance)
# 1601

# part 2
def getNewWaypoint(current_waypoint, turn_direction,  num_turns):
    if turn_direction == 'R':
        turn_id = num_turns % 4
    elif turn_direction == 'L':
        turn_id = (4 - num_turns % 4) % 4
    else:
        print("Incorrect value for 'rotation_direction'")

    if turn_id == 0:
        new_waypoint = current_waypoint
    elif turn_id == 1:
        new_waypoint = [-1 * current_waypoint[1], current_waypoint[0]]
    elif turn_id == 2:
        new_waypoint = [-1 * current_waypoint[0], -1 * current_waypoint[1]]
    elif turn_id == 3:
        new_waypoint = [current_waypoint[1], -1 * current_waypoint[0]]
    else:
        raise Exception("Incorrect 'turn_id'")

    return(new_waypoint)


waypoint = [1, 10]
position = [0, 0]

for inst in instructions:
    if inst['action'] == 'N':
        waypoint[0] += inst['value']
    if inst['action'] == 'S':
        waypoint[0] -= inst['value']
    if inst['action'] == 'E':
        waypoint[1] += inst['value']
    if inst['action'] == 'W':
        waypoint[1] -= inst['value']

    if inst['action'] in ['L', 'R']:
        num_turns = int(inst['value'] / 90)
        waypoint = getNewWaypoint(waypoint, inst['action'], num_turns)

    if inst['action'] == 'F':
        position[0] += inst['value'] * waypoint[0]
        position[1] += inst['value'] * waypoint[1]

    print("-----------------------------")
    print(waypoint)
    print(position)

manhattan_distance = abs(position[0]) + abs(position[1])
print(manhattan_distance)
# 13340
