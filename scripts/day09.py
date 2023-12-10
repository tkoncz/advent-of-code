with open("inputs/input09.txt", "r") as input:
    sequences = [
        [int(x) for x in l.split(" ")] 
        for l in input.read().rstrip().split("\n")
    ]


next_values, prev_values = [], []
for seq in sequences:
    seqs = [seq]
    while len(set(seq)) != 1:
        seq = [seq[i + 1] - seq[i] for i, _ in enumerate(seq) if i < len(seq) - 1]
        seqs.append(seq)

    seqs = seqs[::-1]

    for i, seq in enumerate(seqs):
        if i < len(seqs) - 1:
            diff = seq[-1]
            seqs[i + 1] = seqs[i + 1] + [seqs[i + 1][-1] + diff]
            
            diff = seq[0]
            seqs[i + 1] = [seqs[i + 1][0] - diff] + seqs[i + 1]
        else:
            next_values.append(seq[-1])
            prev_values.append(seq[0])

# part 1 ----
print(sum(next_values))
# part 2 ----
print(sum(prev_values))
