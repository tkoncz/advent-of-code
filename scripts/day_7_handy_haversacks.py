import re

with open("inputs/day_7_handy_haversacks_input.txt", "r") as input:
    lines = list(input.read().split('.\n'))[:-1]

text_to_remove = ' bags?'

rules = []
for l in lines:
    tmp = l.split(' contain ')

    rules.append({
        "container_bag": re.sub(text_to_remove, '', tmp[0]),
        "allowed_contents": tmp[1]
    })

## check if everything is OK
unique_bags = list(set([r['container_bag'] for r in rules]))
if len(unique_bags) != len(lines):
    print("baj van")
else:
    print('found {} unique bags'.format(len(unique_bags)))

can_contain_shiny_bag = [
    r['container_bag'] for r in rules if 'shiny gold' in r['allowed_contents']
]

founding_new_bags = True
while founding_new_bags is True:
    possible_new_bags = []
    for rule in rules:
        for bag in can_contain_shiny_bag:
            if bag in rule['allowed_contents']:
                possible_new_bags.append(rule['container_bag'])

    possible_new_bags = list(set(possible_new_bags)) # unique
    if len(list(set(possible_new_bags) - set(can_contain_shiny_bag))) > 0:
        print('new bags found')
        can_contain_shiny_bag.extend(possible_new_bags)
        can_contain_shiny_bag = list(set(can_contain_shiny_bag))
    else:
        print('No new bags found - stopping!')
        founding_new_bags = False

print(len(can_contain_shiny_bag))

# part 2
# bag - contents dict
parsed_rules = {}
for r in rules:
    parsed_rules[r['container_bag']] = []
    if r['allowed_contents'] != 'no other bags':
        tmp = r['allowed_contents'].split(', ')
        for x in tmp:
            pattern = '(\\d+) ([a-z]+ [a-z]+) bags?'
            matches = re.search(pattern, x)

            parsed_rules[r['container_bag']].append({
                matches.group(2): int(matches.group(1))
            })
    else:
        parsed_rules[r['container_bag']].append(None)

contents = [{'shiny gold': 1}]
num_bags_list = []
while len(contents) > 0:
    new_contents = []

    print("-------------------------------------------------")
    print(contents)
    for bag in contents:
        bag_name = list(bag.keys())[0]
        num_bags = list(bag.values())[0]
        if parsed_rules[bag_name] != [None]:
            print(parsed_rules[bag_name])

            new_contents.extend([
                {list(bag_rule.keys())[0]: num_bags * list(bag_rule.values())[0]}
                for bag_rule in parsed_rules[bag_name]
            ])
        else:
            print("Empty bag found")

    new_num_bags = [list(i.values())[0] for i in new_contents]
    num_bags_list.extend(new_num_bags)
    contents = new_contents

print(sum(num_bags_list))
