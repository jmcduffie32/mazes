import random
class AldousBroder:

    @staticmethod
    def on(grid, steps=None):
        if steps is None:
            steps = grid.size()

        cell = grid.random_cell()
        grid.unvisited.remove(cell)

        while len(grid.unvisited) > grid.size() - steps:
            neighbor = random.choice(cell.neighbors())
            if not neighbor.links:
                cell.link(neighbor)
                grid.unvisited.remove(neighbor)
            cell = neighbor

        return grid
