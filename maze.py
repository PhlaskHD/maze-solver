from cell import Cell
from tkinter import Tk, BOTH, Canvas
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
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
        time.sleep(0.025)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[len(self.cells) - 1][len(self.cells[len(self.cells)-1]) - 1].has_bottom_wall = False
        self.draw_cell(len(self.cells) - 1, len(self.cells[len(self.cells)-1]) - 1)
    
    def break_walls_r(self, i=0, j=0):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and self.cells[i-1][j].visited == False:
                to_visit.append((i-1, j))
            if i < len(self.cells) - 1 and self.cells[i+1][j].visited == False:
                to_visit.append((i+1, j))
            if j > 0 and self.cells[i][j-1].visited == False:
                to_visit.append((i, j-1))
            if j < len(self.cells[i]) - 1 and self.cells[i][j+1].visited == False:
                to_visit.append((i, j+1))
            if to_visit == []:
                return
            else:
                chosen_x, chosen_y = to_visit[random.randint(0, len(to_visit)-1)]
                if chosen_x > i:
                    self.cells[i][j].has_right_wall = False
                    self.draw_cell(i, j)
                    self.cells[chosen_x][chosen_y].has_left_wall = False
                    self.draw_cell(chosen_x, chosen_y)
                if chosen_x < i:
                    self.cells[i][j].has_left_wall = False
                    self.draw_cell(i, j)
                    self.cells[chosen_x][chosen_y].has_right_wall = False
                    self.draw_cell(chosen_x, chosen_y)
                if chosen_y > j:
                    self.cells[i][j].has_bottom_wall = False
                    self.draw_cell(i, j)
                    self.cells[chosen_x][chosen_y].has_top_wall = False
                    self.draw_cell(chosen_x, chosen_y)
                if chosen_y < j:
                    self.cells[i][j].has_top_wall = False
                    self.draw_cell(i, j)
                    self.cells[chosen_x][chosen_y].has_bottom_wall = False
                    self.draw_cell(chosen_x, chosen_y)
                self.break_walls_r(chosen_x, chosen_y)


        