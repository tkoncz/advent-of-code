import numpy as np

def convert_motion_to_steps(dir, size):
    steps = {
        'R': [0,  1],
        'D': [-1, 0],
        'L': [0, -1],
        'U': [1,  0],
    }

    return [steps[dir] for i in range(size)]

with open("inputs/input09.txt", "r") as input:
    steps_nested = [
        convert_motion_to_steps(line[0], int(line[2:]))
        for line in input.read().rstrip().split('\n')
    ]

steps = [np.array(x) for step in steps_nested for x in step]

# part 1
head_pos = np.array([0, 0])
tail_pos = np.array([0, 0])
tail_pos_visited = [(0, 0)]

for head_step in steps:
    head_pos += head_step
    pos_diff = head_pos - tail_pos
    
    if max(abs(pos_diff)) == 2:
        tail_step = np.clip(pos_diff, -1, 1)
        tail_pos += tail_step
        tail_pos_visited.append(tuple(tail_pos))


print(len(set(tail_pos_visited)))


# part 2
head_pos = np.array([0, 0])
tail_positions = [np.array([0, 0]) for i in range(9)]
tail_pos_visited = [(0, 0)]

for head_step in steps:
    head_pos += head_step

    for i in range(9):
        if i == 0:
            pos_diff = head_pos - tail_positions[0]
        else:
            pos_diff = tail_positions[i-1] - tail_positions[i]
    
        if max(abs(pos_diff)) == 2:
            tail_step = np.clip(pos_diff, -1, 1)
            tail_positions[i] += tail_step


    tail_pos_visited.append(tuple(tail_positions[8]))


print(len(set(tail_pos_visited)))
