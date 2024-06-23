import random
from flask import Flask, render_template, request
from mazes.grid import Grid
from mazes.colored_grid import ColoredGrid
from mazes.distance_grid import DistanceGrid
from mazes.algo import BinaryTree, Sidewinder, AldousBroder, Wilsons

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/maze')
def maze():
    scale = int(request.args.get('scale', '10'))
    rows = int(request.args.get('rows', '10'))
    columns = int(request.args.get('columns', '10'))
    algo = request.args.get('algo', 'binary_tree')
    starting_cell = request.args.get('startingCell', '0,0')
    show_distances = request.args.get('showDistances', "true") == 'true'
    show_solution = request.args.get('showSolution', "true") == 'true'
    show_colors = request.args.get('showColors', "true") == 'true'
    seed = request.args.get('seed', None)
    if seed and seed != 'random':
        random.seed(seed)

    if show_colors:
        grid = ColoredGrid(rows, columns)
    else:
        grid = DistanceGrid(rows, columns)

    starting_cell = [int(coord) for coord in starting_cell.split(',')]
    start = grid.get_cell(starting_cell[0], starting_cell[1])

    match algo:
        case 'binary_tree':
            BinaryTree.on(grid)
        case 'sidewinder':
            Sidewinder.on(grid)
        case 'aldous-broder':
            AldousBroder.on(grid)
        case 'wilsons':
            Wilsons.on(grid)
        case 'aldous-broder-wilsons':
            AldousBroder.on(grid, steps=(grid.size() // 2))
            Wilsons.on(grid)
    
    distances = start.distances()

    if show_solution:
        grid.distances = distances.path_to(grid.get_cell(grid.rows - 1, 0))
    else:
        grid.distances = distances


    return grid.to_svg(scale=scale, show_distances=show_distances, show_solution=show_solution)
