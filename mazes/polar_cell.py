from mazes.cell import Cell

class PolarCell(Cell):
    def __init__(self, row, column) -> None:
        super().__init__(row, column)
        self.cw = None
        self.ccw = None
        self.inward = None
        self.outward = []
    
    def neighbors(self):
        l = [self.cw, self.ccw, self.inward] + self.outward
        return [cell for cell in l if cell is not None]
