def check_marker(input, n):
    for i in range(len(input) - (n-1)):
        chars_to_check = input[i:(i + n)]
        if len(set(chars_to_check)) == n:
            return(i + n)


with open("inputs/input06.txt", "r") as input:
    input = input.read().rstrip()


# part 1
print(check_marker(input, 4))


# part 2
print(check_marker(input, 14))
