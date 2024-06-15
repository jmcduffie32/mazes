from mazes.distance_grid import DistanceGrid
from mazes.algo.binary_tree import BinaryTree


grid = DistanceGrid(5, 5)
BinaryTree.on(grid)
start = grid.get_cell(0, 0)

distances = start.distances()
new_start, distance = distances.max

new_distances = new_start.distances()
goal, distance = new_distances.max

grid.distances = new_distances.path_to(goal)
print(grid)
