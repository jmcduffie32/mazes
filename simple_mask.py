from mazes.masked_grid import MaskedGrid
from mazes.mask import Mask
from mazes.algo import RecursiveBacktracker

mask = Mask(5,5)

mask.set_bit(0, 0, False)
mask.set_bit(2, 2, False)
mask.set_bit(4, 4, False)

grid = MaskedGrid(mask)

RecursiveBacktracker.on(grid)

print(grid)
