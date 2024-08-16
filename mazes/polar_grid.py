import math
import random

from PIL import Image, ImageDraw
from mazes.grid import Grid
from mazes.polar_cell import PolarCell

class PolarGrid(Grid):
    def __init__(self, rows):
        super().__init__(rows, 1)

    def prepare_grid(self):
        rows = []
        row_height = 1.0 / self.rows

        rows.append([PolarCell(0, 0)])

        for row in range(1, self.rows):
            radius = row / self.rows
            circumference = 2 * math.pi * radius

            previous_count = len(rows[row - 1])
            estimated_cell_witdh = circumference / previous_count
            ratio = round(estimated_cell_witdh / row_height)

            cells = previous_count * ratio
            rows.append([PolarCell(row, col) for col in range(cells)])
        
        return rows

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            if row > 0:
                cell.cw = self.get_cell(row, col + 1)
                cell.ccw = self.get_cell(row, col - 1)
                ratio = len(self.grid[row]) / len(self.grid[row - 1])
                parent_row = row - 1
                parent_col = int(col // ratio)
                parent = self.get_cell(parent_row, parent_col)
                parent.outward.append(cell)
                cell.inward = parent

    def get_cell(self, row, column):
        if row >= self.rows or row < 0:
            return None
        return self.grid[row][column % len(self.grid[row])]
    
    def random_cell(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, len(self.grid[row]) - 1)
        return self.grid[row][col]


    def to_png(self, cell_size=10):
        img_size = 2 * self.rows * cell_size

        background = (255, 255, 255)
        wall = (0, 0, 0)

        img = Image.new("RGB", (img_size + 1, img_size + 1), background)

        center = img_size // 2

        for cell in self.each_cell():
            if cell.row == 0:
                continue
            theta = 2 * math.pi / len(self.grid[cell.row])
            inner_radius = cell.row * cell_size
            outer_radius = (cell.row + 1) * cell_size
            theta_ccw = cell.column * theta
            theta_cw = (cell.column + 1) * theta

            ax = center + int(inner_radius * math.cos(theta_ccw))
            ay = center + int(inner_radius * math.sin(theta_ccw))
            bx = center + int(outer_radius * math.cos(theta_ccw))
            by = center + int(outer_radius * math.sin(theta_ccw))
            cx = center + int(inner_radius * math.cos(theta_cw))
            cy = center + int(inner_radius * math.sin(theta_cw))
            # dx = center + int(outer_radius * math.cos(theta_cw))
            # dy = center + int(outer_radius * math.sin(theta_cw))

            if not cell.is_linked(cell.inward):
                img_draw = ImageDraw.Draw(img)
                img_draw.line([(ax, ay), (cx, cy)], fill=wall)
            if not cell.is_linked(cell.cw):
                img_draw = ImageDraw.Draw(img)
                img_draw.line([(ax, ay), (bx, by)], fill=wall)

        img_draw = ImageDraw.Draw(img)
        img_draw.circle((center, center), self.rows * cell_size, outline=wall)
        return img
