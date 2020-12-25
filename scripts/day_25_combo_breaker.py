# card_public_key = 5764801
# door_public_key = 17807724

card_public_key = 9093927
door_public_key = 11001876

# part 1
def findLoopSize(public_key, subject_number):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= subject_number
        value = value % 20201227

        loop_size = loop_size + 1

    return(loop_size)


subject_number = 7

card_loop_size = findLoopSize(card_public_key, subject_number)
door_loop_size = findLoopSize(door_public_key, subject_number)

value_1 = 1
for i in range(0, card_loop_size):
    value_1 *= door_public_key
    value_1 = value_1 % 20201227

value_2 = 1
for i in range(0, door_loop_size):
    value_2 *= card_public_key
    value_2 = value_2 % 20201227

print(f'{value_1} --- {value_2}')
