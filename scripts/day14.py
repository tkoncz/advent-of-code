from collections import Counter

def letterPairs(num_steps, pair_counter):
    for step in range(num_steps):
        temp_pair_counter = {}
        for k, v in pair_counter.items():
            letter_pairs_to_add = transition_rules.get(k)
            letter_1, letter_2 = letter_pairs_to_add[0], letter_pairs_to_add[1]
            temp_pair_counter[letter_1] = temp_pair_counter.get(letter_1, 0) + v
            temp_pair_counter[letter_2] = temp_pair_counter.get(letter_2, 0) + v

        pair_counter = temp_pair_counter

    return pair_counter


def letterCounts(pair_counter, edge_letters):
    letter_counter = {}
    for k,v in pair_counter.items():
        letter_1, letter_2 = k[0], k[1]
        letter_counter[letter_1] = letter_counter.get(letter_1, 0) + v
        letter_counter[letter_2] = letter_counter.get(letter_2, 0) + v

    letter_counter = (
        {k: int((v - 1) / 2 + 1) for k,v in letter_counter.items() if k in edge_letters} |
        {k: int(v / 2) for k,v in letter_counter.items() if k not in edge_letters}
    )

    return letter_counter


def letterCountRange(letter_counter):
    letter_counts = sorted(list(letter_counter.values()))
    return(letter_counts[-1] - letter_counts[0])


with open("inputs/input14.txt", "r") as input:
    raw_input = input.read().rstrip().split("\n")

polymer_template = raw_input[0]

rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in raw_input[2:]}
transition_rules = {k: [k[0] + v, v + k[1]] for k,v in rules.items()}

pair_counter = dict(Counter([r for r in rules.keys() if r in polymer_template]))

pair_counter = letterPairs(10, pair_counter)
edge_letters = [polymer_template[0], polymer_template[-1]]
letter_counter = letterCounts(pair_counter, edge_letters)

print("1 -------")
print(letterCountRange(letter_counter))

pair_counter = letterPairs(30, pair_counter)
letter_counter = letterCounts(pair_counter, edge_letters)

print("2 -------")
print(letterCountRange(letter_counter))
