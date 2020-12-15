from math import nan

# lines = [0, 3, 6]
lines = [16, 12, 1, 0, 15, 7, 11]

# part 1 & 2
numbers_last_spoken = {}

spoken_numbers = {}
for i in range(0, 30000000):
    # if i > 0 and i % 300000 == 0:
    #     print(i / 30000000)

    if i < len(lines):
        number = lines[i]
    else:
        if spoken_numbers[i - 1]['first_spoken'] == True:
            number = 0
        else:
            number = (i - 1) - spoken_numbers[i - 1]['last_spoken']

    if number not in numbers_last_spoken.keys():
        first_spoken = True
        numbers_last_spoken[number] = [i, nan]
    else:
        first_spoken = False
        numbers_last_spoken[number] = [i, max(numbers_last_spoken[number])]

    last_spoken = numbers_last_spoken[number][1]

    spoken_numbers[i] = {
        'number': number,
        'first_spoken': first_spoken,
        'last_spoken': last_spoken
    }

# part 1
print(spoken_numbers[2019]['number'])
# 2020: 403

# part 2
print(spoken_numbers[30000000 - 1]['number'])
# 30000000: 6823
