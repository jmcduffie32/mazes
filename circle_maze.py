from mazes.polar_grid import PolarGrid
from mazes.algo import RecursiveBacktracker

grid = PolarGrid(8)
RecursiveBacktracker.on(grid)

filename = "polar.png"
grid.to_png().save(filename)
