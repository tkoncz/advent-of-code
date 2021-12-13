from collections import Counter

def getConnectedCaves(cave):
    all_connections = (
        [x["from"] for x in DIRECTIONS if x["to"] == cave] +
        [x["to"] for x in DIRECTIONS if x["from"] == cave]
    )
    return([y for y in all_connections if y != 'end'])


def findAllPaths(connected_caves_map, is_part2):
    all_paths_known = False
    unfinished_paths = [['end']]
    finished_paths = []

    while all_paths_known == False:
        temp_unfinished_paths = []
        for path in unfinished_paths:
            current_cave = path[-1]
            connected_caves = connected_caves_map.get(current_cave)
            for prev_cave in connected_caves:
                if prev_cave == 'start':
                    finished_paths.append(path + [prev_cave])
                else:
                    if prev_cave.islower() == False:
                        temp_unfinished_paths.append(path + [prev_cave])
                    elif prev_cave not in path:
                        temp_unfinished_paths.append(path + [prev_cave])
                    elif is_part2 == True:
                        max_small_cave_occ = max([
                            v for k,v in dict(Counter(path)).items()
                            if k.islower() == True
                        ])
                        if max_small_cave_occ < 2:
                            temp_unfinished_paths.append(path + [prev_cave])


        unfinished_paths = temp_unfinished_paths

        all_paths_known = True
        if len(unfinished_paths) > 0:
            all_paths_known = False

    return finished_paths


with open("inputs/input12.txt", "r") as input:
    DIRECTIONS = [
        {"from": x.split("-")[0], "to": x.split("-")[1]}
        for x in input.read().rstrip().split("\n") if x.split("-")[1]
    ]

connected_caves_map = {
    cave: getConnectedCaves(cave) for cave
    in set([d["from"] for d in DIRECTIONS] + [d["to"] for d in DIRECTIONS])
}


print("1 -------")
print(len(findAllPaths(connected_caves_map, False)))

print("2 -------")
print(len(findAllPaths(connected_caves_map, True)))
