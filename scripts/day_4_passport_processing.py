from itertools import compress
import re

with open("inputs/day_4_passport_processing_input.txt", "r") as input:
    lines = list(input.read().rstrip().split('\n\n'))

lines = [l.replace('\n', ' ') for l in lines]

parsed_lines = []
for l in lines:
    parsed_lines.append(dict(x.split(":") for x in l.split(" ")))

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# part 1
def checkThatAllFieldsExist(required_fields, passport_fields):
    not_all_fields_exist = False

    for item in required_fields:
        if item not in passport_fields:
            not_all_fields_exist = True
            break

    return(not not_all_fields_exist)

passport_complete = [
    checkThatAllFieldsExist(required_fields, list(l.keys())) for l in parsed_lines
]

print(sum(passport_complete))

# part 2
complete_passports = list(compress(parsed_lines, passport_complete))

correct_passports = complete_passports
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
correct_passports = [p for p in correct_passports if 1920 <= int(p['byr']) <= 2002]
print(len(correct_passports))
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
correct_passports = [p for p in correct_passports if 2010 <= int(p['iyr']) <= 2020]
print(len(correct_passports))
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
correct_passports = [p for p in correct_passports if 2020 <= int(p['eyr']) <= 2030]
print(len(correct_passports))
# hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
correct_passports = [
    p for p in correct_passports
    if (bool(re.match('\d{2}in', p['hgt'])) and 59  <= int(p['hgt'][0:2]) <= 76) or
       (bool(re.match('\d{3}cm', p['hgt'])) and 150 <= int(p['hgt'][0:3]) <= 193)
]
print(len(correct_passports))
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
correct_passports = [
    p for p in correct_passports if bool(re.match('^#[0-9a-f]{6}$', p['hcl']))
]
print(len(correct_passports))
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
correct_passports = [
    p for p in correct_passports
    if bool(re.match('^amb|blu|brn|gry|grn|hzl|oth$', p['ecl']))
]
print(len(correct_passports))
# pid (Passport ID) - a nine-digit number, including leading zeroes.
correct_passports = [
    p for p in correct_passports
    if bool(re.match('^\d{9}$', p['pid']))
]
print(len(correct_passports))

print(len(correct_passports))
