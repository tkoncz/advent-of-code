import re

# part 1 ----
with open("inputs/input01.txt", "r") as input:
    calibration_values = [
        "".join(re.findall(r"\d", x)) 
        for x in input.read().rstrip().split("\n")
    ]
    
print(sum([int(x[0] + x[-1]) for x in calibration_values]))


# part 2 ----
NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_numbers(x: str) -> str:
    for word, number in NUMBER_MAPPING.items():
        x = x.replace(word, word + number + word)
    
    return x


with open("inputs/input01.txt", "r") as input:
    calibration_values = [
        "".join(re.findall(r"\d", replace_numbers(x))) 
        for x in input.read().rstrip().split("\n")
    ]
    
print(sum([int(x[0] + x[-1]) for x in calibration_values]))
