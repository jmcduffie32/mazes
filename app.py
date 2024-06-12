from flask import Flask, render_template, request
from mazes.grid import Grid
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

    grid = Grid(rows, columns)
    match algo:
        case 'binary_tree':
            BinaryTree.on(grid)
        case 'sidewinder':
            Sidewinder.on(grid)
    return grid.to_svg(scale=scale)
