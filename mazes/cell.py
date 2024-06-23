from mazes.distances import Distances

class Cell:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self._links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self) -> str:
        return f"Cell at ({self.row}, {self.column})"

    def link(self, cell, bidirectional=True):
        self._links[cell] = True
        if bidirectional:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidirectional=True):
        del self._links[cell]
        if bidirectional:
            cell.unlink(self, False)
        return self

    @property
    def links(self):
        return self._links.keys()

    def is_linked(self, cell):
        return cell in self._links

    def neighbors(self):
        potential_neighbors = [self.north, self.south, self.east, self.west]
        return [cell for cell in potential_neighbors if cell is not None]

    def distances(self):
        distances = Distances(self)
        frontier = [self]

        while len(frontier) != 0:
            new_frontier = []
            for cell in frontier:
                for linked in cell.links:
                    if distances[linked] is None:
                        distances[linked] = distances[cell] + 1
                        new_frontier.append(linked)
            frontier = new_frontier

        return distances
