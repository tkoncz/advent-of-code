with open("inputs/day_13_shuttle_search_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

earliest_departure = int(lines[0])
buses = [int(bus) for bus in lines[1].split(',') if bus != "x"]

def getEarliestDepartureWithBus(earliest_departure, bus_id):
    earliest_departure_w_bus = 0
    while earliest_departure_w_bus < earliest_departure:
        earliest_departure_w_bus += bus_id

    return(earliest_departure_w_bus)

earliest_departures_by_bus = {
    bus_id: getEarliestDepartureWithBus(earliest_departure, bus_id)
    for bus_id in buses
}

earliest_departure_by_bus = min(
    earliest_departures_by_bus.items(), key = lambda x: x[1]
)

print(earliest_departure_by_bus[0] * (earliest_departure_by_bus[1] - earliest_departure))

# part 2
departure_rule = 0
for bus in lines[1].split(','):
    if bus != 'x':
        buses_w_departure_rules[int(bus)] = departure_rule
    departure_rule += 1


step_size = 1
start_time = 0
all_criteria_met = False
while all_criteria_met == False:
    start_time += step_size

    ok = True
    items_to_pop = []
    for bus, departure_rule in buses_w_departure_rules.items():
        if ((start_time + departure_rule) % bus == 0):
            step_size = step_size * bus
            items_to_pop.append(bus)
            # print("start_time: {}, step_size: {}".format(start_time, step_size))
        else:
            ok = False
            break

    for item in items_to_pop:
        buses_w_departure_rules.pop(item)

    if ok == True:
        all_criteria_met = True

print(start_time)
