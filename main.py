from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import *
from maze import Maze
import time

def main():
    win = Window(1920, 1080)

    maze = Maze(100, 100, 10, 10, 30, 30, win,)
    maze.break_entrance_and_exit()
    maze.break_walls_r()


    win.wait_for_close()















main()