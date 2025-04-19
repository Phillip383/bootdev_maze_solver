from vector2 import Vector2
from tkinter import Canvas

class Line():
    def __init__(self, start: Vector2, end: Vector2):
        self.__start = start
        self.__end = end
        
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.__start.x, self.__start.y,
            self.__end.x, self.__end.y,
            fill=fill_color,
            width=2
        )