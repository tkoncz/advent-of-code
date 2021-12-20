class Image:
    def __init__(self, image, enhancement_algo, infinite_pixel = '.'):
        self.image = image
        self.max_y = len(image) - 1
        self.max_x = len(image[0]) - 1
        self.algo = enhancement_algo
        self.infinite_pixel = infinite_pixel

    def pad_image(self):
        extra_row = [self.infinite_pixel * (self.max_x + 7)]
        padded_rows = [
            3 * self.infinite_pixel + row + 3 * self.infinite_pixel
            for row in self.image
        ]

        self.padded_image = (extra_row + padded_rows + extra_row)
        self.padded_max_y = len(self.padded_image) - 1
        self.padded_max_x = len(self.padded_image[0]) - 1

    def get_pixel(self, x, y):
        if (x > self.padded_max_x or x < 0) or (y > self.padded_max_y or y < 0):
            return(self.infinite_pixel)

        return self.padded_image[y][x]

    def get_output_pixel(self, x, y):
        pixels = "".join([
            self.get_pixel(x - 1, y - 1),
            self.get_pixel(x,     y - 1),
            self.get_pixel(x + 1, y - 1),
            self.get_pixel(x - 1, y),
            self.get_pixel(x,     y),
            self.get_pixel(x + 1, y),
            self.get_pixel(x - 1, y + 1),
            self.get_pixel(x,     y + 1),
            self.get_pixel(x + 1, y + 1)
        ])

        binary = pixels.replace('.', '0').replace('#', '1')
        pos = int(binary, 2)

        return self.algo[pos]

    def enhance_image(self):
        enhanced_image = []
        for y in range(self.padded_max_y + 1):
            line = ''
            for x in range(self.padded_max_x + 1):
                line += self.get_output_pixel(x, y)
            enhanced_image += [line]

        self.enhanced_image = enhanced_image

    def count_lit_pixels(self):
        return len("".join(self.enhanced_image).replace('.', ''))


with open("inputs/input19.txt", "r") as input:
    input = input.read().rstrip().split('\n')

input_image = input[2:]
enhancement_algo = input[0]
infinite_pixel = '.'

for i in range(2):
    image = Image(input_image, enhancement_algo, infinite_pixel)
    image.pad_image()
    image.enhance_image()

    input_image = image.enhanced_image
    infinite_pixel = (
        enhancement_algo[0] if infinite_pixel == '.' else enhancement_algo[511]
    )

print("1 -------")
print(image.count_lit_pixels())


for i in range(48):
    image = Image(input_image, enhancement_algo, infinite_pixel)
    image.pad_image()
    image.enhance_image()

    input_image = image.enhanced_image
    infinite_pixel = (
        enhancement_algo[0] if infinite_pixel == '.' else enhancement_algo[511]
    )


print("2 -------")
print(image.count_lit_pixels())
