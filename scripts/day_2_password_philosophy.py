import re

with open("inputs/day_2_password_philosophy_input.txt", "r") as input:
    lines = list(input.read().split('\n')[:-1])

parsed_lines = []
for l in lines:
    pattern = '^(\\d+)-(\\d+) ([A-z]): ([A-z]+)$'
    matches = re.search(pattern, l)

    parsed_lines.append({
        "min_rep": int(matches.group(1)),
        "max_rep": int(matches.group(2)),
        "letter" : matches.group(3),
        "pw": matches.group(4)
    })

# part 1
num_pw_correct = 0
for x in parsed_lines:
    count_letter = x['pw'].count(x['letter'])
    if x['min_rep'] <= count_letter <= x['max_rep']:
        num_pw_correct = num_pw_correct + 1

print(num_pw_correct)
# 548

# part 2
num_pw_correct = 0
for x in parsed_lines:
    match = 0
    if x['pw'][x['min_rep']-1] == x['letter']:
        match = match + 1
    if x['pw'][x['max_rep']-1] == x['letter']:
        match = match + 1

    if match == 1:
        num_pw_correct = num_pw_correct + 1

print(num_pw_correct)
# 502
