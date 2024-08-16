from mazes.grid import Grid
from mazes.mask import Mask
from mazes.cell import Cell


class MaskedGrid(Grid):
    def __init__(self, mask: Mask) -> None:
        self.mask = mask
        super().__init__(mask.rows, mask.columns)

    def prepare_grid(self):
        return [
            [
                Cell(row, column) if self.mask.get_bit(row, column) else None
                for column in range(self.columns)
            ]
            for row in range(self.rows)
        ]

    def random_cell(self):
        row, col = self.mask.random_location()
        return self.get_cell(row, col)

    def size(self):
        return self.mask.count()
