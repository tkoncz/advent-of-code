class TwoDArray:
    def __init__(self, ll: list, default_value=None):
        self.data = ll
        self.default_value = default_value
        self.num_row = len(ll)
        self.num_col = len(ll[0])
        self.shape = (self.num_row, self.num_col)

    def __getitem__(self, index: tuple):
        if any([i < 0 for i in index]):
            return self.default_value
        
        try:
            return self.data[index[0]][index[1]]
        except:
            return self.default_value
    
    def __str__(self):
        return '\n'.join([''.join(row) for row in self.data])


with open("inputs/input03.txt", "r") as input:
    schematic = TwoDArray(
        [list(x) for x in input.read().rstrip().split("\n")],
        default_value="."
    )
    
    
DIGITS = [str(i) for i in range(10)]
NON_SYMBOLS = DIGITS + ["."]
ADJACENT_SHIFTS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,  -1),          (0,  1),
    (1,  -1), (1,  0), (1,  1),
]

num_row, num_col = schematic.shape

part_numbers = []
stars = {}
for r in range(num_row):
    number = ""
    is_part_number = False
    adjacent_stars = set()
    
    for c in range(num_col):
        if schematic[r, c] in DIGITS:
            number += schematic[r, c]
            
            adjacents = [
                schematic[r + shift[0], c + shift[1]] 
                for shift in ADJACENT_SHIFTS
            ]
        
            if any([x not in NON_SYMBOLS for x in adjacents]):
                is_part_number = True

            adjacent_stars |= set([
                (r + shift[0], c + shift[1])
                for shift in ADJACENT_SHIFTS
                if schematic[r + shift[0], c + shift[1]] == "*"
            ])
            
        if (
            # hits a non-digit or reaches the end of line
            (schematic[r, c] not in DIGITS or c == num_col - 1) and
            len(number) > 0 
        ):
            if is_part_number:
                part_numbers.append(int(number))
            
            if len(adjacent_stars) > 0:
                for star in adjacent_stars:
                    stars[star] = stars.get(star, []) + [int(number)]
                    
            number = ""
            is_part_number = False
            adjacent_stars = set()  
    

# part 1 ----
print(sum([x for x in part_numbers]))

# part 2 ----
print(sum([v[0] * v[1] for k, v in stars.items() if len(v) == 2] ))
