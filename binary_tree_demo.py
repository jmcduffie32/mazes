from mazes.grid import Grid
from mazes.algo.sidewinder import Sidewinder

grid = Grid(4, 4)
Sidewinder.on(grid)
print(grid)
