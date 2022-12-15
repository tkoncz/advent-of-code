import re


def parse_report(report_line: str) -> [tuple, tuple]:
    p = re.compile('Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)')
    m = p.match(line)

    # row, col format (so reverse of x, y)
    S = (int(m.group(2)), int(m.group(1)))
    B = (int(m.group(4)), int(m.group(3)))

    return [S, B]


def calc_manhattan_dist(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open("inputs/input15.txt", "r") as input:
    input = input.read().rstrip().split('\n')


sensors = {}
beacons = []

for ln, line in enumerate(input):
    sensor_pos, beacon_pos = parse_report(line)
    sensor_radius = calc_manhattan_dist(sensor_pos, beacon_pos)
    
    sensors[sensor_pos] = sensor_radius
    beacons += [beacon_pos]


sensors = dict(sorted(sensors.items(), key=lambda x: x[0]))

beacons = list(set(beacons))
beacons.sort()


# part 1
# row = 10 
row = 2_000_000

covered_positions = []
for S, R in sensors.items(): # sensor, radius
    SR, SC = S[0], S[1] # sensor row, sensor col
    VD = abs(row - SR) # vertical distance
    if VD <= R:
        covered_positions += [(row, c) for c in range(SC - (R - VD), SC + (R - VD) + 1)]

covered_positions = list(set(covered_positions))

print(sum([1 for pos in covered_positions if not (pos in sensors or pos in beacons)]))


# part 2
r_min, c_min = 0, 0
# r_max, c_max = 20, 20
r_max, c_max = 4_000_000, 4_000_000


def solve_part2():
    for row in range(r_min, r_max + 1):
        covered_positions = []
        for S, R in sensors.items(): # sensor, radius
            SR, SC = S[0], S[1] # sensor row, sensor col
            VD = abs(row - SR) # vertical distance
            if VD <= R:
                first_col = max(SC - (R - VD), c_min)
                last_col  = min(SC + (R - VD), c_max)
                covered_positions.append((first_col, last_col))

        covered_positions.sort()
        covmax = 1
        for cp in covered_positions:
            if covmax < cp[0] - 1:
                return((row, covmax + 1))
            covmax = max(cp[1], covmax)

        if covmax != c_max:
            return((row, covmax + 1))


y, x = solve_part2()
print(x * 4_000_000 + y)
