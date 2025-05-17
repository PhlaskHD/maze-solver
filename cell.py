from graphics import *

class Cell:
    def __init__(self, window, visited=False):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1, self.x2, self.y1, self.y2 = -1, -1, -1, -1
        self.win = window
        self.visited = visited

    def __repr__(self):
       # return f"x1: {self.x1} y1: {self.y1}, x2: {self.x2}, y2 {self.y2}"
       return f"cell"

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        point_tl = Point(x1, y1)
        point_tr = Point(x2, y1)
        point_bl = Point(x1, y2)
        point_br = Point(x2, y2)
        top_wall = Line(point_tl, point_tr)
        right_wall = Line(point_tr, point_br)
        bottom_wall = Line(point_bl, point_br)
        left_wall = Line(point_tl, point_bl)
        if self.has_left_wall == True:
            self.win.draw_line(left_wall)
        else:
            self.win.draw_line(left_wall, "#d9d9d9")
        if self.has_right_wall == True:
            self.win.draw_line(right_wall)
        else:
            self.win.draw_line(right_wall, "#d9d9d9")
        if self.has_top_wall == True:
            self.win.draw_line(top_wall)
        else:
            self.win.draw_line(top_wall, "#d9d9d9")
        if self.has_bottom_wall == True:
            self.win.draw_line(bottom_wall)
        else:
            self.win.draw_line(bottom_wall, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            color = "red"
        else:
            color = "gray"
        departure_point = Point(self.x1 + ((self.x2 - self.x1)//2), self.y1 + ((self.y2 - self.y1)//2))
        arrival_point = Point(to_cell.x1 + ((to_cell.x2 - to_cell.x1)//2), to_cell.y1 + ((to_cell.y2 - to_cell.y1)//2))
        path = Line(departure_point, arrival_point)
        self.win.draw_line(path, color)
