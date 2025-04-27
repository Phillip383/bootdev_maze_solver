import time

from cell import Cell
from vector2 import Vector2


class Maze():

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
    
    def get_cells(self):
        return self.__cells

    def __create_cells(self):
        for column in range(self.__num_cols):
            temp = []
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                # if its the first cell create entrance
                if column == 0 and row == 0:
                    cell.has_top_wall = False
                # else if its the last cell create exit
                elif column == self.__num_cols - 1 and row == self.__num_rows - 1:
                    cell.has_bottom_wall = False
                temp.append(cell)
            self.__cells.append(temp)
        
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self.__win:
            x_pos = self.__x1 + (j * self.__cell_size_x)
            y_pos = self.__y1 + (i * self.__cell_size_y)
            start = Vector2(x_pos, y_pos)
            end = Vector2(x_pos + self.__cell_size_x, y_pos + self.__cell_size_y)

            self.__cells[i][j].draw(start, end)
            self._animate()
    
    def _animate(self):
        if self.__win:
            self.__win.redraw()
            time.sleep(0.05)
