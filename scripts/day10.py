from itertools import pairwise
from re import sub

def checkIfLineHasClosingChar(line):
    for x in [')', ']', '}', '>']:
        if x in line: return True

    return False


def replaceClosedChunks(line):
    return sub('\\(\\)|\\[\\]|\\{\\}|<>', '', line)


def findFirstMisMatch(line):
    for a, b in pairwise(line):
        if a == '(' and b in [']', '}', '>']: return b
        if a == '[' and b in [')', '}', '>']: return b
        if a == '{' and b in [']', ')', '>']: return b
        if a == '<' and b in [']', '}', ')']: return b


def findValuePart1(char):
    char_to_value = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return char_to_value.get(char)


def findValuePart2(char):
    char_to_value = {")": 1, "]": 2, "}": 3, ">": 4}
    return char_to_value.get(char)


def findClosingChar(char):
    char_to_closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    return char_to_closing.get(char)


def CalculateScore(chars):
    score = 0
    for char in chars:
        score *= 5
        score += findValuePart2(char)

    return score


def calcCharsToAdd(line):
    chars_to_add = ''
    for char in reversed(line):
        if char == "(": chars_to_add += ")"
        if char == "[": chars_to_add += "]"
        if char == "{": chars_to_add += "}"
        if char == "<": chars_to_add += ">"

    return chars_to_add


with open("inputs/input10.txt", "r") as input:
    lines = [x for x in input.read().rstrip().split("\n")]

mismatch_closings = []
incomplete_lines = []

for line in lines:
    line_length = 0
    line_length_tmp = len(line)

    while line_length != line_length_tmp:
        line_length = line_length_tmp
        line = replaceClosedChunks(line)
        line_length_tmp = len(line)

    if checkIfLineHasClosingChar(line) == True:
        mismatch_closings.append(findFirstMisMatch(line))
    else:
        incomplete_lines.append(line)


print("1 -------")
print(sum([findValuePart1(x) for x in mismatch_closings]))

incomplete_line_scores = [
    CalculateScore(calcCharsToAdd(line)) for line in incomplete_lines
]

print("2 -------")
print(sorted(incomplete_line_scores)[int(len(incomplete_line_scores)/2)])
