from mazes.grid import Grid
from mazes.distances import Distances

class DistanceGrid(Grid):
    def __init__(self, rows, columns) -> None:
        super().__init__(rows, columns)
        self.distances: Distances

    def contents_of(self, cell):
        if not self.distances:
            return super().contents_of(cell)

        if (distance := self.distances[cell]) is not None:
            return distance
        
        return super().contents_of(cell)
