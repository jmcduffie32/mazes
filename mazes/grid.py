import random
import svgwrite as sw
from mazes.cell import Cell


class Grid:
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        return [
            [Cell(row, column) for column in range(self.columns)]
            for row in range(self.rows)
        ]

    def configure_cells(self):
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            cell.north = self.get_cell(row - 1, column)
            cell.south = self.get_cell(row + 1, column)
            cell.east = self.get_cell(row, column + 1)
            cell.west = self.get_cell(row, column - 1)

    def get_cell(self, row, column):
        if row >= self.rows or row < 0:
            return None
        if column >= self.columns or column < 0:
            return None
        return self.grid[row][column]

    def random_cell(self):
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return self.get_cell(row, column)

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in self.grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def __str__(self) -> str:
        output = "+" + "---+" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                cell = cell or Cell(-1, -1)
                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        return output
    
    def to_svg(self, scale=1):
        dwg = sw.Drawing(
            filename="assets/maze.svg",
            size=(self.columns * 10 * scale, self.rows * 10 * scale),
        )

        for cell in self.each_cell():
            x1 = cell.column * 10 * scale
            y1 = cell.row * 10 * scale
            x2 = (cell.column + 1) * 10 * scale
            y2 = (cell.row + 1) * 10 * scale

            if not cell.north:
                dwg.add(dwg.line((x1, y1), (x2, y1), stroke=sw.rgb(0, 0, 0)))

            if not cell.west:
                dwg.add(dwg.line((x1, y1), (x1, y2), stroke=sw.rgb(0, 0, 0)))

            if not cell.is_linked(cell.east):
                dwg.add(dwg.line((x2, y1), (x2, y2), stroke=sw.rgb(0, 0, 0)))

            if not cell.is_linked(cell.south):
                dwg.add(dwg.line((x1, y2), (x2, y2), stroke=sw.rgb(0, 0, 0)))
            
        return dwg.tostring()
        

