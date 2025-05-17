from cell import Cell
from tkinter import Tk, BOTH, Canvas
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()
    
    def create_cells(self):
        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                self.cells[i].append(Cell(self.win))
                self.draw_cell(i, j)
    
    def draw_cell(self, i, j):
        x = self.x1 + (i * self.cell_size_x)
        y = self.y1 + (j * self.cell_size_y)
        x2 = x + self.cell_size_x
        y2 = y + self.cell_size_y
        self.cells[i][j].draw(x, y, x2, y2)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)