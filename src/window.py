from tkinter import Tk, Canvas
from line import Line
class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(height=self.__height, width=self.__width)
        self.__canvas.pack()
        self.__active = False
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__active = True
        while self.__active:
            self.redraw()

    def close(self):
        self.__active = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color=fill_color)
