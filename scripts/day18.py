from string import digits
from itertools import pairwise
from math import ceil, floor
import re

REGEX_PAIR = re.compile("\\[(\\d+),(\\d+)\\]")
REGEX_NUMBER = re.compile("(\\d+)")

def explode(snailfish_number):
    cnt_unclosed = 0
    for i, c in enumerate(snailfish_number):
        if c == '[': cnt_unclosed += 1
        if c == ']': cnt_unclosed -= 1

        if cnt_unclosed >= 5:
            if (m := REGEX_PAIR.match(snailfish_number[i:(i + 8)])) is not None:
                splitter, left_value, right_value = m.group(0), m.group(1), m.group(2)
                split_number = snailfish_number[i:].split(splitter)
                left_w_updated_value = snailfish_number[:i] + split_number[0]
                right_w_updated_value = splitter.join(split_number[1:])

                # [::-1] --> reverse string
                if (ml := REGEX_NUMBER.search(left_w_updated_value[::-1])) is not None:
                    l_start, l_end = ml.span()
                    l_updated_value = str(
                        int(ml.group(1)[::-1]) + int(left_value)
                    )
                    left_w_updated_value = (
                        left_w_updated_value[::-1][:l_start] +
                        l_updated_value[::-1] +
                        left_w_updated_value[::-1][l_end:]
                    )[::-1]

                if (mr := REGEX_NUMBER.search(right_w_updated_value)) is not None:
                    r_start, r_end = mr.span()
                    r_updated_value = int(mr.group(1)) + int(right_value)
                    right_w_updated_value = (
                        right_w_updated_value[:r_start] +
                        str(r_updated_value) +
                        right_w_updated_value[r_end:]
                    )

                updated_number = left_w_updated_value + '0' + right_w_updated_value

                return updated_number, True

    return snailfish_number, False

def split(snailfish_number):
    for a,b in pairwise(snailfish_number):
        if a in digits and b in digits:
            splitter = a + b
            split_number = snailfish_number.split(splitter)
            left = split_number[0]
            right = splitter.join(split_number[1:])

            updated_number = (
                left + "[" +
                str(floor(int(a + b) / 2)) + "," + str(ceil(int(a + b) / 2)) +
                "]" + right
            )

            return updated_number, True

    return snailfish_number, False

def add(snailfish_number_1, snailfish_number_2):
    return("[" + snailfish_number_1 + "," + snailfish_number_2 + "]")

def reduce(snailfish_number):
    updated = True
    while updated == True:
        snailfish_number, updated = explode(snailfish_number)
        if updated == False:
            snailfish_number, updated = split(snailfish_number)

    return snailfish_number

def finalSum(list_of_snailfish_numbers):
    final_sum = list_of_snailfish_numbers[0]
    for snailfish_number in list_of_snailfish_numbers[1:]:
        final_sum = add(final_sum, snailfish_number)
        final_sum = reduce(final_sum)

    return final_sum


def magnitude(final_sum):
    while True:
        if (m := REGEX_PAIR.search(final_sum)) is not None:
            magnitude_of_pair = 3 * int(m.group(1)) + 2 * int(m.group(2))
            splitter = m.group(0)
            split_number = final_sum.split(splitter)
            left = split_number[0]
            right = splitter.join(split_number[1:])
            final_sum = left + str(magnitude_of_pair) + right
        else:
            return int(final_sum)


with open("inputs/input18.txt", "r") as input:
    list_of_snailfish_numbers = input.read().rstrip().split("\n")

final_sum = finalSum(list_of_snailfish_numbers)

print("1 -------")
print(magnitude(final_sum))

magnitudes_for_all_combinations = []
for snailfish_number_1 in list_of_snailfish_numbers:
    for snailfish_number_2 in list_of_snailfish_numbers:
        if snailfish_number_1 != snailfish_number_2:
            magnitudes_for_all_combinations.append(
                magnitude(
                    finalSum([snailfish_number_1, snailfish_number_2])
                )
            )

print("2 -------")
print(max(magnitudes_for_all_combinations))
















## TESTING SUITE
# print(" <--- magnitude tests ---> ")
# print(magnitude("[[1,2],[[3,4],5]]") == 143)
# print(magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]") == 1384)
# print(magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]") == 445)
# print(magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]") == 791)
# print(magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]") == 1137)
# print(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]") == 3488)

# print(" <--- final sum tests --->")
# input = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"""
# list_of_snailfish_numbers = input.split("\n")
# print(
#     finalSum(list_of_snailfish_numbers) ==
#     "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
# )


# input = """[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]"""
# list_of_snailfish_numbers = input.split("\n")
# print(
#     finalSum(list_of_snailfish_numbers) ==
#     "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]"
# )

# input = "[1,1]\n[2,2]\n[3,3]\n[4,4]"
# list_of_snailfish_numbers = input.split("\n")
# print(
#     finalSum(list_of_snailfish_numbers) ==
#     "[[[[1,1],[2,2]],[3,3]],[4,4]]"
# )

# input = "[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]"
# list_of_snailfish_numbers = input.split("\n")
# print(
#     finalSum(list_of_snailfish_numbers) ==
#     "[[[[3,0],[5,3]],[4,4]],[5,5]]"
# )

# input = "[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]"
# list_of_snailfish_numbers = input.split("\n")
# print(
#     finalSum(list_of_snailfish_numbers) ==
#     "[[[[5,0],[7,4]],[5,5]],[6,6]]"
# )

# print(" <--- reduce tests --->")
# print(
#     reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]") ==
#     "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
# )

# print(" <--- add tests --->")
# print(
#     add("[1,2]","[[3,4],5]") ==
#     "[[1,2],[[3,4],5]]"
# )

# print(
#     add("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]") ==
#     "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# )

# print(" <--- split tests --->")
# input = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
# print(
#     split(input)[0] ==
#     "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
# )

# input = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
# print(
#     split(input)[0] ==
#     "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
# )

# print(" <--- explode tests --->")

# input = "[[[[[9,8],1],2],3],4]"
# print(
#     explode(input)[0] ==
#     "[[[[0,9],2],3],4]"
# )

# input = "[7,[6,[5,[4,[3,2]]]]]"
# print(
#     explode(input)[0] ==
#     "[7,[6,[5,[7,0]]]]"
# )

# input = "[[6,[5,[4,[3,2]]]],1]"
# print(
#     explode(input)[0] ==
#     "[[6,[5,[7,0]]],3]"
# )

# input = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# print(
#     explode(input)[0] ==
#     "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# )

# input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# print(
#     explode(input)[0] ==
#     "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
# )

