def getMostAndLeastFrequentDigits(digits):
    most_frequent = mostFrequent(digits)
    least_frequent = leastFrequent(digits)
    if most_frequent == least_frequent:
        most_frequent = '1'
        least_frequent = '0'

    return(most_frequent, least_frequent)


def mostFrequent(List):
    return max(set(List), key = List.count)


def leastFrequent(List):
    return min(set(List), key = List.count)


# ----
with open("inputs/input3.txt", "r") as input:
    input = [x for x in input.read().rstrip().split("\n")]

num_digits = len(input[0])

gamma, epsilon = '', ''
for digit in range(num_digits):
    most_frequent, least_frequent = getMostAndLeastFrequentDigits(
        digits=[i[digit] for i in input]
    )
    gamma += most_frequent
    epsilon += least_frequent

print("1 -------")
print(int(gamma, 2) * int(epsilon, 2))


oxygen_generator_rating = input.copy()
co2_scrubber_rating = input.copy()

for digit in range(num_digits):
    if len(oxygen_generator_rating) > 1:
        most_frequent, least_frequent = getMostAndLeastFrequentDigits(
            digits=[i[digit] for i in oxygen_generator_rating]
        )

        oxygen_generator_rating_to_keep = [
            line for line in oxygen_generator_rating
            if most_frequent == line[digit]
        ]
        oxygen_generator_rating = oxygen_generator_rating_to_keep.copy()

    if len(co2_scrubber_rating) > 1:
        most_frequent, least_frequent = getMostAndLeastFrequentDigits(
            digits=[i[digit] for i in co2_scrubber_rating]
        )

        co2_scrubber_rating_to_keep = [
            line for line in co2_scrubber_rating
            if least_frequent == line[digit]
        ]
        co2_scrubber_rating = co2_scrubber_rating_to_keep.copy()

    if len(oxygen_generator_rating) == 1 & len(co2_scrubber_rating) == 1:
        break


print("2 -------")
print(int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2))
