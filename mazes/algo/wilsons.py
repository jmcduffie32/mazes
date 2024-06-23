import random

class Wilsons:
    @staticmethod
    def on(grid):
        if len(grid.unvisited) == grid.size():
            first = random.choice(grid.unvisited)
            grid.unvisited.remove(first)

        while grid.unvisited:
            cell = random.choice(grid.unvisited)
            path = [cell]

            while cell in grid.unvisited:
                cell = random.choice(cell.neighbors())
                try:
                    position = path.index(cell)
                    path = path[:position + 1]
                except ValueError:
                    path.append(cell)
        
            for i in range(len(path) - 1):
                path[i].link(path[i + 1])
                grid.unvisited.remove(path[i])

        return grid
