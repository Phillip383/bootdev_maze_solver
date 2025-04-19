from window import Window
from vector2 import Vector2
from line import Line

class Cell():
    def __init__(self, top_left: Vector2, bottom_right: Vector2, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = window

    def draw(self, top_left: Vector2 = None, bottom_left: Vector2 = None):
        
        if self.has_left_wall:
            self._win.draw_line(Line(Vector2(self._x1, self._y1), Vector2(self._x1, self._y2)), "black")
        if self.has_right_wall:
             self._win.draw_line(Line(Vector2(self._x2, self._y1), Vector2(self._x2, self._y2)), "black")
        if self.has_top_wall:
             self._win.draw_line(Line(Vector2(self._x1, self._y1), Vector2(self._x2, self._y1)), "black")
        if self.has_bottom_wall:
             self._win.draw_line(Line(Vector2(self._x1, self._y2), Vector2(self._x2, self._y2)), "black")
    
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