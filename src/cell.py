from window import Window
from vector2 import Vector2
from line import Line

class Cell():
    def __init__(self, window: Window, top_left: Vector2=None, bottom_right: Vector2=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, top_left: Vector2 = None, bottom_right: Vector2 = None):
        
        if self.has_left_wall:
            self._win.draw_line(Line(Vector2(top_left.x, top_left.y), Vector2(top_left.x, bottom_right.y)), "black")
        if self.has_right_wall:
             self._win.draw_line(Line(Vector2(bottom_right.x, top_left.y), Vector2(bottom_right.x, bottom_right.y)), "black")
        if self.has_top_wall:
             self._win.draw_line(Line(Vector2(top_left.x, top_left.y), Vector2(bottom_right.x, top_left.y)), "black")
        if self.has_bottom_wall:
             self._win.draw_line(Line(Vector2(top_left.x, bottom_right.y), Vector2(bottom_right.x, bottom_right.y)), "black")
    
    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        start = Vector2(
            abs(self._x1 - self._x2),
            abs(self._y1 - self._y2)
        )
        end = Vector2(
            abs((to_cell._x1 - to_cell._x2)) + abs(self._x2 - self._x1) + abs(self._x2 - to_cell._x1),
            abs((to_cell._y1 - to_cell._y2))
        )
        self._win.draw_line(Line(start, end), color)