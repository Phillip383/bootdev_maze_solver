from window import Window
from vector2 import Vector2
from line import Line

class Cell():
    def __init__(self, top_left: Vector2, bottom_right: Vector2, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.x
        self.__y1 = top_left.y
        self.__x2 = bottom_right.x
        self.__y2 = bottom_right.y
        self.__win = window

    def draw(self, top_left: Vector2 = None, bottom_left: Vector2 = None):
        
        if self.has_left_wall:
            self.__win.draw_line(Line(Vector2(self.__x1, self.__y1), Vector2(self.__x1, self.__y2)), "black")
        if self.has_right_wall:
             self.__win.draw_line(Line(Vector2(self.__x2, self.__y1), Vector2(self.__x2, self.__y2)), "black")
        if self.has_top_wall:
             self.__win.draw_line(Line(Vector2(self.__x1, self.__y1), Vector2(self.__x2, self.__y1)), "black")
        if self.has_bottom_wall:
             self.__win.draw_line(Line(Vector2(self.__x1, self.__y2), Vector2(self.__x2, self.__y2)), "black")