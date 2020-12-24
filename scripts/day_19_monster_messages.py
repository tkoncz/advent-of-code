from itertools import product

with open("inputs/day_19_monster_messages_input.txt", "r") as input:
    raw_input = input.read().rstrip()

raw_rules = raw_input.split('\n\n')[0].split('\n')
messages = raw_input.split('\n\n')[1].split('\n')

rules = {}
for raw_rule in raw_rules:
    tmp = raw_rule.split(': ')
    rule = tmp[1].replace('"', '')
    rules[int(tmp[0])] = rule

# part 1
def checkIfRuleIsALetter(rule):
    return(len(rule) == 1 and not rule.isdigit() == True)


def addRules(rule_1, rule_2):
    rule = list(map(lambda x: ''.join(x),
        list(product(rule_1.split(' | '), rule_2.split(' | ')))
    ))

    rule = list(set(rule))

    return(' | '.join(rule))


def expandRule(id, rules):
    if id in rules_dict.keys():
        return(rules_dict[id])

    rule = rules[id]
    if checkIfRuleIsALetter(rule) == True:
        return(rule)
    else:
        sub_rules = ''
        for i, sub_rule in enumerate(rule.split(' | ')):
            rules_in_sub_rule = ''
            for rule_in_sub_rule in sub_rule.split(' '):
                if checkIfRuleIsALetter(rule_in_sub_rule) == True:
                    rules_in_sub_rule += rule_in_sub_rule
                else:
                    tmp_rule = expandRule(int(rule_in_sub_rule), rules)
                    rules_in_sub_rule = addRules(rules_in_sub_rule, tmp_rule)

            if i == 0:
                sub_rules = rules_in_sub_rule
            else:
                sub_rules += ' | ' + rules_in_sub_rule

        rules_dict[id] = sub_rules
        return(sub_rules)

rules_dict = {}

rule_0 = expandRule(0, rules).split(' | ')
num_matching_messages = sum([1 for message in messages if message in rule_0])

print(num_matching_messages)
# 111

# part 2
import re

rule_31 = expandRule(31, rules).split(' | ')
rule_42 = expandRule(42, rules).split(' | ')

rule_42_regex = '|'.join(rule_42)
rule_31_regex = '|'.join(rule_31)

matching_messages = []
for message in messages:
    pattern = ('^' + f'({rule_42_regex})+' + f'({rule_31_regex})+' + '$')
    matches = re.match(pattern, message)
    if matches is not None:
        matching_messages.append(message)


# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# there needs to be more matches to rule 42 than 31!

num_equal_or_more_rule_31_matches = 0
for msg in matching_messages:
    foo = re.search('^' + f'(({rule_42_regex})+)' + f'(({rule_31_regex})+)', msg)
    if len(foo.group(1)) <= len(foo.group(3)):
        num_equal_or_more_rule_31_matches += 1

print(len(matching_messages) - num_equal_or_more_rule_31_matches)
# 343
