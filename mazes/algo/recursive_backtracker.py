import random
from mazes.grid import Grid

class RecursiveBacktracker():
    @staticmethod
    def on(grid: Grid, start_at=None):
        stack = []
        start_at = start_at or grid.random_cell()
        stack.append(start_at)

        while stack:
            current = stack[-1]
            neighbors = [n for n in current.neighbors() if not n.links]
            if not neighbors:
                stack.pop()
            else:
                neighbor = random.choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
        return grid
