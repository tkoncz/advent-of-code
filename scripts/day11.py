import copy

with open("inputs/input11.txt", "r") as input:
    input = input.read().rstrip().split('Monkey ')

rounds = 20

parsed_monkies = {}
for unparsed_monkey in input[1:]:
    m_unstructured = unparsed_monkey.split('\n')

    monkey_index = int(m_unstructured[0][0])
    items = [int(x) for x in m_unstructured[1][18:].split(', ')]
    operation = m_unstructured[2][23:]
    if operation == '* old': operation = '** 2'
    test = int(m_unstructured[3][21:])
    if_true = int(m_unstructured[4][29:])
    if_false = int(m_unstructured[5][30:])

    monkey = {
        'items': items,
        'operation': operation,
        'test': test,
        'throw_rule': {True: if_true, False: if_false},
        'num_inspection': 0
    }
    parsed_monkies[monkey_index] = monkey


# part 1
monkies = copy.deepcopy(parsed_monkies)
for round in list(range(rounds)):
    for monkey_index in list(monkies.keys()):
        monkey = monkies[monkey_index]
        items = monkey['items']
        operation, throw_rule, test = monkey['operation'], monkey['throw_rule'], monkey['test']

        for item in items:
            worry_level = eval(f'{item}{operation}') // 3
            monkey_to_throw = throw_rule[worry_level % test == 0]            
            monkies[monkey_to_throw]['items'].append(worry_level)

        monkies[monkey_index]['items'] = []
        monkies[monkey_index]['num_inspection'] += len(items)


num_inspections = [monkey['num_inspection'] for monkey_index, monkey in monkies.items()]
num_inspections.sort(reverse=True)

print(num_inspections[0] * num_inspections[1])


# part 2
rounds = 10_000

monkies = copy.deepcopy(parsed_monkies)

# idea: don't store actual items, but the remainder by all the possible divisors
throw_tests = [monkey['test'] for monkey in monkies.values()]
for monkey_id, monkey in monkies.items():
    actual_items = monkies[monkey_id]['items']
    replaced_items = [{test: item % test for test in throw_tests} for item in actual_items]
    monkies[monkey_id]['items'] = replaced_items


for round in list(range(rounds)):
    for monkey_index in list(monkies.keys()):
        monkey = monkies[monkey_index]
        items = monkey['items']
        operation, throw_rule, test = monkey['operation'], monkey['throw_rule'], monkey['test']

        for item in items:
            worry_level = {
                test: eval(f'{x}{operation}') % test
                for test, x in item.items()
            }

            throw_monkey_id = throw_rule[worry_level[test] == 0]
            throw_monkey_test = monkies[throw_monkey_id]['test']            
            monkies[throw_monkey_id]['items'].append(worry_level)

        monkies[monkey_index]['items'] = []
        monkies[monkey_index]['num_inspection'] += len(items)

num_inspections = [monkey['num_inspection'] for monkey_index, monkey in monkies.items()]
num_inspections.sort(reverse=True)

print(num_inspections[0] * num_inspections[1])
