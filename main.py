from tkinter import Tk, BOTH, Canvas
from graphics import *
from cell import *
from maze import Maze
import time

def main():
    win = Window(1920, 1080)

    maze = Maze(100, 100, 20, 20, 25, 15, win)


    win.wait_for_close()















main()