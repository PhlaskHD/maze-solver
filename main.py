from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import *
from maze import Maze
import time
import sys

def main():
    sys.setrecursionlimit(10000)
    win = Window(1920, 1080)

    maze = Maze(50, 50, win)
    maze.break_entrance_and_exit()
    maze.break_walls_r()
    maze.reset_cells_visited()
    maze.solve()


    win.wait_for_close()















main()