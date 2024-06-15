from mazes.grid import Grid
from mazes.distances import Distances

class DistanceGrid(Grid):
    def __init__(self, rows, columns) -> None:
        super().__init__(rows, columns)
        self._distances: Distances
        self.max: int
    
    @property
    def distances(self):
        return self._distances
    
    @distances.setter
    def distances(self, distances):
        self._distances = distances
        _farthest, self.max = distances.max

    def contents_of(self, cell):
        if not self.distances:
            return super().contents_of(cell)

        if (distance := self._distances[cell]) is not None:
            return distance
        
        return super().contents_of(cell)
