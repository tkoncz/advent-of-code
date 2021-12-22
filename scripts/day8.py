import string

def getFirstDigitWithLength(length, digit_lengths):
    return list(digit_lengths.keys())[list(digit_lengths.values()).index(length)]


with open("inputs/input8.txt", "r") as input:
    signals = [x.split(" | ") for x in input.read().rstrip().split("\n")]

entries = [
    {"input": s[0].split(" "), "output": s[1].split(" ")} for s in signals
]

digit_lengths = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

digits_w_unique_len = [1, 4, 7, 8]

outputs = [signal for e in entries for signal in e["output"]]

print("1 -------")
print(
    len([
        f for f in outputs
        if len(f) in [digit_lengths[digit] for digit in digits_w_unique_len]
    ])
)

#### part 2
sum_output_values = 0

for entry in entries:
    mapping_digit_to_number = {}
    mapping_number_to_digit = {}

    all_digits = entry["input"] + entry["output"]
    all_digits = list(set(["".join(sorted(digit)) for digit in all_digits]))

    for digit in all_digits:
        if len(digit) == 2:
            mapping_digit_to_number[digit] = 1
            mapping_number_to_digit[1] = digit
        elif len(digit) == 4:
            mapping_digit_to_number[digit] = 4
            mapping_number_to_digit[4] = digit
        elif len(digit) == 3:
            mapping_digit_to_number[digit] = 7
            mapping_number_to_digit[7] = digit
        elif len(digit) == 7:
            mapping_digit_to_number[digit] = 8
            mapping_number_to_digit[8] = digit

    for digit in mapping_digit_to_number.keys():
        all_digits.remove(digit)

    for digit in all_digits:
        if (
            len(digit) == 6
            # contains b, c, d, f
            and mapping_number_to_digit.get(4, ['x'])[0] in digit
            and mapping_number_to_digit.get(4, ['x'])[1] in digit
            and mapping_number_to_digit.get(4, ['x'])[2] in digit
            and mapping_number_to_digit.get(4, ['x'])[3] in digit
        ):
            mapping_digit_to_number[digit] = 9
            mapping_number_to_digit[9] = digit
            all_digits.remove(digit)
            break


    for letter in set(sorted("".join(all_digits))):
        if letter not in mapping_number_to_digit[9]:
            letter_e = letter

    for digit in all_digits:
        if (
            len(digit) == 5
            and letter_e in digit
        ):
            mapping_digit_to_number[digit] = 2
            mapping_number_to_digit[2] = digit
            all_digits.remove(digit)
            break

    for digit in all_digits:
        if (
            len(digit) == 6
            # c, f
            and mapping_number_to_digit.get(1, ['x'])[0] in digit
            and mapping_number_to_digit.get(1, ['x'])[1] in digit
        ):
            mapping_digit_to_number[digit] = 0
            mapping_number_to_digit[0] = digit
            all_digits.remove(digit)
            break

    for digit in all_digits:
        if len(digit) == 6:
            mapping_digit_to_number[digit] = 6
            mapping_number_to_digit[6] = digit
            all_digits.remove(digit)
            break

    for digit in all_digits:
        if (
            len(digit) == 5
            # c, f
            and mapping_number_to_digit.get(1, ['x'])[0] in digit
            and mapping_number_to_digit.get(1, ['x'])[1] in digit
        ):
            mapping_digit_to_number[digit] = 3
            mapping_number_to_digit[3] = digit
            all_digits.remove(digit)
            break

    mapping_digit_to_number[all_digits[0]] = 5
    mapping_number_to_digit[5] = all_digits[0]

    output_value = ''
    for digit in entry["output"]:
        output_value += str(mapping_digit_to_number["".join(sorted(digit))])

    output_value = int(output_value)
    # print(entry["output"], ": ", output_value)
    sum_output_values += output_value

print("2 -------")
print(sum_output_values)


