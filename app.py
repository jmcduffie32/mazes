import random
from flask import Flask, render_template, request
from mazes.grid import Grid
from mazes.distance_grid import DistanceGrid
from mazes.algo import BinaryTree, Sidewinder

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
    show_distances = request.args.get('showDistances', "true") == 'true'
    show_solution = request.args.get('showSolution', "true") == 'true'
    seed = request.args.get('seed', None)
    if seed and seed != 'random':
        random.seed(seed)

    grid = DistanceGrid(rows, columns)
    match algo:
        case 'binary_tree':
            BinaryTree.on(grid)
        case 'sidewinder':
            Sidewinder.on(grid)

    
    start = grid.get_cell(0, 0)
    distances = start.distances()

    if show_solution:
        grid.distances = distances.path_to(grid.get_cell(grid.rows - 1, 0))
    else:
        grid.distances = distances

    return grid.to_svg(scale=scale, show_distances=show_distances, show_solution=show_solution)
