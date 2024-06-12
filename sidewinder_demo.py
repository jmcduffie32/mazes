from mazes.grid import Grid
from mazes.algo.binary_tree import BinaryTree

grid = Grid(4, 4)
BinaryTree.on(grid)
grid.to_svg()
print(grid)
