class RiskLevels:
    def __init__(self, risk_map):
        self.risk_levels = risk_map

    def get_dimensions(self):
        y = len(self.risk_levels) - 1
        x = len(self.risk_levels[0]) - 1
        return x, y

    def get_value(self, coords):
        x, y = coords["x"], coords["y"]
        # TODO: handle values that are outside?
        return self.risk_levels[y][x]

    def get_connected_caves(self, coords):
        x, y = coords["x"], coords["y"]
        max_x, max_y = self.get_dimensions()
        connected_caves = []
        if x < max_x: connected_caves.append({"x": x + 1, "y": y})
        if y < max_y: connected_caves.append({"x": x, "y": y + 1})
        if x > 0: connected_caves.append({"x": x - 1, "y": y})
        if y > 0: connected_caves.append({"x": x, "y": y - 1})

        return(connected_caves)

    def get_last_cave(self):
        max_x, max_y = self.get_dimensions()
        return {"x": max_x, "y": max_y}

    def calc_lowest_risk_paths_to_cave(self):
        last_cave = self.get_last_cave()

        lowest_risk_paths = []
        for y in range(last_cave["y"] + 1):
            line = []
            for x in range(last_cave["x"] + 1):
                if x == 0 and y == 0:
                    line.append(0)
                else:
                    line.append(float('inf'))

            lowest_risk_paths.append(line)

        any_risk_updated = True
        while any_risk_updated == True:
            any_risk_updated = False
            for y in range(last_cave["y"] + 1):
                for x in range(last_cave["x"] + 1):
                    if not(x == 0 and y == 0):
                        current_risk = lowest_risk_paths[y][x]
                        cave_risk = self.get_value({"x": x, "y": y})
                        connected_caves = self.get_connected_caves({"x": x, "y": y})
                        lowest_risk_path_to_current_cave = min([
                            lowest_risk_paths[coord["y"]][coord["x"]]
                            for coord in connected_caves
                        ])

                        if current_risk > (lowest_risk_path_to_current_cave + cave_risk):
                            lowest_risk_paths[y][x] = lowest_risk_path_to_current_cave + cave_risk
                            any_risk_updated = True

        self.lowest_risk_paths = lowest_risk_paths

    def get_lowest_risk_path(self):
        last_cave = self.get_last_cave()
        x, y = last_cave["x"], last_cave["y"]
        return self.lowest_risk_paths[y][x]

    def extend_map(self):
        last_cave = self.get_last_cave()
        full_risk_map = []
        for row in range(5):
            for y in range(last_cave["y"] + 1):
                line = []
                for col in range(5):
                    for x in range(last_cave["x"] + 1):
                        risk = (self.get_value({"x": x, "y": y}) + col + row) % 9
                        if risk == 0: risk = 9
                        line.append(risk)

                full_risk_map.append(line)

        self.risk_levels = full_risk_map


with open("inputs/input15.txt", "r") as input:
    risk_map = [[int(x) for x in y] for y in input.read().rstrip().split("\n")]

risk_levels = RiskLevels(risk_map)
risk_levels.calc_lowest_risk_paths_to_cave()

print("1 -------")
print(risk_levels.get_lowest_risk_path())

risk_levels.extend_map()
risk_levels.calc_lowest_risk_paths_to_cave()

print("2 -------")
print(risk_levels.get_lowest_risk_path())
