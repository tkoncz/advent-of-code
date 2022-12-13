def check_if_correct_order(left, right) -> bool:

    # both ints
    if isinstance(left, int) & isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right

    is_correct_order = None
    while is_correct_order is None:
        
        # both lists
        if isinstance(left, list) & isinstance(right, list):

            if len(left) == 0 and len(right) == 0:
                return None
            if len(left) == 0:
                return True
            elif len(right) == 0:
                return False

            left_, right_ = left[0], right[0]
            is_correct_order = check_if_correct_order(left_, right_)

            if is_correct_order is None:
                left, right = left[1:], right[1:]

        # mixed types
        elif isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]

    return is_correct_order


with open("inputs/input13.txt", "r") as input:
    input = input.read().rstrip().split('\n\n')


packet_pairs = [[eval(x) for x in i.split('\n')] for i in input]


# part 1
cnt = 0
for i, packet_pair in enumerate(packet_pairs):
    
    left, right = packet_pair[0], packet_pair[1]
    if check_if_correct_order(left, right) == True:
        cnt += (i + 1)

print(cnt)


# part 2
packets = [
    [[2]],
    [[6]]
]

for packet_pair in packet_pairs:
    packets.append(packet_pair[0])
    packets.append(packet_pair[1])

changed_order = True
while changed_order:
    changed_order = False
    for i in range(len(packets) - 1):
        left = packets[i]
        right = packets[i + 1]

        if not check_if_correct_order(left, right):
            packets = packets[:i] + [right] + [left] + packets[i+2:]
            changed_order = True

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
