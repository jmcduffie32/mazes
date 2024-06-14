from mazes.distance_grid import DistanceGrid
from mazes.algo import BinaryTree

grid = DistanceGrid(4, 4)
BinaryTree.on(grid)

start = grid.get_cell(0, 0)
distances = start.distances()

grid.distances = distances
print(grid)

grid.distances = distances.path_to(grid.get_cell(grid.rows - 1, 0))
print(grid)
