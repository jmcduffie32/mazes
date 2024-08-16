from mazes.polar_grid import PolarGrid

grid = PolarGrid(8)

filename = "polar.png"
grid.to_png().save(filename)
