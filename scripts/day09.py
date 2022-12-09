import numpy as np


def convert_motion_to_steps(dir: str, size: int) -> list:
    steps = {
        'R': [0,  1],
        'D': [-1, 0],
        'L': [0, -1],
        'U': [1,  0],
    }

    return [steps[dir] for i in range(size)]


def simulate_tail_path(tail_length: int) -> list:
    head_pos = np.array([0, 0])
    tail_positions = [np.array([0, 0]) for i in range(tail_length)]
    tail_pos_visited = [(0, 0)]

    for head_step in steps:
        head_pos += head_step

        for i in range(tail_length):
            if i == 0:
                pos_diff = head_pos - tail_positions[0]
            else:
                pos_diff = tail_positions[i-1] - tail_positions[i]
        
            if max(abs(pos_diff)) == 2:
                tail_step = np.clip(pos_diff, -1, 1)
                tail_positions[i] += tail_step

        tail_pos_visited.append(tuple(tail_positions[tail_length - 1]))

    return tail_pos_visited


with open("inputs/input09.txt", "r") as input:
    steps_nested = [
        convert_motion_to_steps(line[0], int(line[2:])) 
        for line in input.read().rstrip().split('\n')
    ]

steps = [np.array(x) for step in steps_nested for x in step]

# part 1
print(len(set(simulate_tail_path(tail_length=1))))

# part 2
print(len(set(simulate_tail_path(tail_length=9))))
