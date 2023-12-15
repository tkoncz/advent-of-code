with open("inputs/input15.txt", "r") as input:
    strings = input.read().rstrip().split(",")
    

# part 1 ----
values = []
for string in strings:
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    
    values.append(current_value)

print(sum(values))


# part 2 ----
def getBox(s):
    box = 0
    for c in s:
        box += ord(c)
        box *= 17
        box = box % 256
    
    return box

boxes = [[] for i in range(256)]
for string in strings:
    if string.endswith("-"):
        s = string[:-1]
        box = getBox(s)
        
        for i, s_fl in enumerate(boxes[box]):
            if s_fl[0] == s:
                boxes[box].pop(i)
        
    else:
        s, focal_length = string.split("=")
        box = getBox(s)
        
        s_found_in_box = False
        for i, s_fl in enumerate(boxes[box]):
            if s_fl[0] == s:
                boxes[box][i] = (s, focal_length)
                s_found_in_box = True
        
        if not s_found_in_box:
            boxes[box] += [(s, focal_length)]

print(sum([
    (i+1) * (slot+1) * int(s_fl[1])
    for i, box in enumerate(boxes) for slot, s_fl in enumerate(box)
    if len(box) > 0
]))