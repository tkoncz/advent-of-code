import re

def getTargetArea(input):
    regex = re.compile(
        "target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)"
    )
    m = regex.match(input)
    x_min, x_max = int(m.group(1)), int(m.group(2))
    y_min, y_max = int(m.group(3)), int(m.group(4))

    return x_min, x_max, y_min, y_max

# input = "target area: x=20..30, y=-10..-5"
input = "target area: x=139..187, y=-148..-89"

target_x_min, target_x_max, target_y_min, target_y_max = getTargetArea(input)

reached_max_highs = []
num_target_found = 0

for x_velo_start in range(0, target_x_max + 1):
    for y_velo_start in range(target_y_min, (-1 * target_y_min)):

        reached_y = []
        x_pos, y_pos = 0, 0
        target_found = False
        step = 0
        while (
            target_found == False and
            x_pos <= target_x_max and
            not (y_pos < target_y_min and (y_velo_start - step) <= 0)
        ):
            x_pos += max(0, x_velo_start - step)
            y_pos += y_velo_start - step
            reached_y.append(y_pos)

            if (
                x_pos in list(range(target_x_min, target_x_max + 1)) and
                y_pos in list(range(target_y_min, target_y_max + 1))
            ):
                target_found = True
                num_target_found += 1
                reached_max_highs.append(max(reached_y))

            step += 1



print("1 -------")
print(max(reached_max_highs))


print("2 -------")
print(num_target_found)
