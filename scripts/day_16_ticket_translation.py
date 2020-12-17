import re
from itertools import compress

with open("inputs/day_16_ticket_translation_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n\n')

def convertStrToIntList(str_list):
    return(list(map(int, str_list)))

def convertTextRangeToListOfNumbers(text_range):
    range_borders = convertStrToIntList(text_range.split('-'))
    return(list(range(range_borders[0], range_borders[1] + 1)))

for l in lines:
    if 'your ticket' in l:
        your_ticket = convertStrToIntList(l[13:].split(','))
    elif 'nearby tickets' in l:
        nearby_tickets = l[16:].split('\n')
        nearby_tickets = [
            convertStrToIntList(ticket.split(','))
            for ticket in nearby_tickets
        ]
    else:
        rules = {}
        for rule in l.split('\n'):
            matches = re.match(
                '([a-z]+( [a-z]+)?): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)',
                rule
            )
            range_1 = convertTextRangeToListOfNumbers(matches.group(3))
            range_2 = convertTextRangeToListOfNumbers(matches.group(4))
            possible_numbers = list(set(range_1 + range_2))
            rules[matches.group(1)] = possible_numbers

# part 1
all_possible_numbers = []
for rule in rules.values():
    all_possible_numbers += rule
    all_possible_numbers = list(set(all_possible_numbers))


incorrect_numbers = []
ticket_validities = []
for ticket in nearby_tickets:
    ticket_is_valid = True
    for num in ticket:
        if num not in all_possible_numbers:
            incorrect_numbers.append(num)
            ticket_is_valid = False
    ticket_validities.append(ticket_is_valid)

# part 1
print(sum(incorrect_numbers))

# part 2
valid_tickets = list(compress(nearby_tickets, ticket_validities))
valid_tickets.append(your_ticket)

all_fields = list(range(0, len(valid_tickets[0])))

valid_cols_for_rules = {}
for rule_name, possible_numbers in rules.items():
    valid_cols = []
    for col in all_fields:
        col_valid = True

        for ticket in valid_tickets:
            if not ticket[col] in possible_numbers:
                col_valid = False

        if col_valid == True:
            valid_cols.append(col)

    valid_cols_for_rules[rule_name] = valid_cols


sorted_valid_cols_for_rules = {}
sorted_rule_names = sorted(
    valid_cols_for_rules,
    key = lambda rule_name: len(valid_cols_for_rules[rule_name])
)

rules_w_possible_cols = {}
allocated_cols = []
for rule_name in sorted_rule_names:
    # print("------------------------------")
    # print(set(valid_cols_for_rules[rule_name]))
    # print(set(allocated_cols))

    available_cols = list(set(valid_cols_for_rules[rule_name]) - set(allocated_cols))
    rules_w_possible_cols[rule_name] = available_cols
    if len(available_cols) == 1:
        allocated_cols += available_cols

print(len(allocated_cols) == len(all_fields))
# True --> each rule has one column assigned! No need to search further

part_2_answer = 1
for key, value in rules_w_possible_cols.items():
    if 'departure' in key:
        part_2_answer = part_2_answer * your_ticket[value[0]]

print(part_2_answer)
