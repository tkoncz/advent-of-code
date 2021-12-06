def roundOfNextSplit(timer_start: int, current_round: int):
    return(current_round + timer_start + 1)


def countSplitsInRounds(timers: [int], last_rounds: int):
    splits = [0 for x in range(last_rounds+1)]
    for t in timers:
        splits[roundOfNextSplit(t, 0)] += 1

    for i in range(last_rounds + 1):
        num_splits = splits[i]
        if num_splits > 0:
            next_split_1 = roundOfNextSplit(6, i)
            next_split_2 = roundOfNextSplit(8, i)
            if next_split_1 <= last_rounds: splits[next_split_1] += num_splits
            if next_split_2 <= last_rounds: splits[next_split_2] += num_splits

    return(splits)


with open("inputs/input6.txt", "r") as input:
    timers = [int(x) for x in input.read().rstrip().split(",")]


print("1 -------")
print(sum(countSplitsInRounds(timers, 80)) + len(timers))


print("2 -------")
print(sum(countSplitsInRounds(timers, 256)) + len(timers))
