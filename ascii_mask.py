import sys

from mazes.mask import Mask
from mazes.masked_grid import MaskedGrid
from mazes.algo import RecursiveBacktracker


# get filename passed as arg
filename = sys.argv[1]
if not filename:
    print("Please provide a filename as an argument")
    sys.exit(1)

mask = Mask.from_png(filename)
grid = MaskedGrid(mask)
RecursiveBacktracker.on(grid)

filename = "masked.svg"
with open(filename, "w") as f:
    svg_content = grid.to_svg()
    f.write(svg_content)
print(grid)
