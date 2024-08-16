import random
from PIL import Image, ImageColor

WHITE = (255, 255, 255)

class Mask:
    @classmethod
    def from_png(cls, filename):
        img = Image.open(filename)
        mask = Mask(img.height, img.width)
        for row in range(img.height):
            for col in range(img.width):
                result = img.getpixel((col, row))
                if len(result) == 4:
                    r, g, b, _a = result
                elif len(result) == 3:
                    r, g, b = result
                elif len(result) == 1:
                    r = result[0]
                    g = result[0]
                    b = result[0]
                mask.set_bit(row, col, (r, g, b) == WHITE)
        return mask


    @classmethod
    def from_txt(cls, filename):
        with open(filename, encoding="utf8") as f:
            lines = [line for line in f.readlines() if line.strip()]
            rows = len(lines)
            columns = len(lines[0])
            mask = Mask(rows, columns)
            for row, line in enumerate(lines):
                for col, c in enumerate(line):
                    if c == 'X':
                        mask.set_bit(row, col, False)
        return mask

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.bits = [[True for _ in range(columns)] for _ in range(rows)]

    def get_bit(self, row, column):
        if row < 0 or row >= self.rows:
            return None
        if column < 0 or column >= self.columns:
            return None
        return self.bits[row][column]

    def set_bit(self, row, column, value):
        if row < 0 or row >= self.rows:
            return
        if column < 0 or column >= self.columns:
            return
        self.bits[row][column] = value

    def count(self):
        count = 0
        for row in self.bits:
            for bit in row:
                if bit:
                    count += 1
        return count

    def random_location(self):
        while True:
            row = random.randint(0, self.rows - 1)
            column = random.randint(0, self.columns - 1)
            if self.get_bit(row, column):
                return row, column
