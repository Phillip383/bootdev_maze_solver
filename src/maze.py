import time
import random
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
        seed=None,
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
        
        if seed is not None:
            random.seed(seed)
    
    def get_cells(self):
        return self.__cells

    def __create_cells(self):
        for column in range(self.__num_cols):
            temp = []
            for row in range(self.__num_rows):
                cell = Cell(self.__win) #type: ignore
                # if its the first cell create entrance
                if column == 0 and row == 0:
                    cell.has_top_wall = False
                # else if its the last cell create exit
                elif column == self.__num_cols - 1 and row == self.__num_rows - 1:
                    cell.has_bottom_wall = False
                temp.append(cell)
            self.__cells.append(temp)
        
        self._break_walls_r(0, 0)
        
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        directions = {"up" : (-1, 0), "down" : (1, 0), "left" : (0, -1), "right" : (0, 1)}

        while True:
            adjacent = {}

            for key in directions.keys():
                row = i + directions[key][0]
                col = j + directions[key][1]

                if 0 <= row <= self.__num_rows - 1 and 0 <= col <= self.__num_cols - 1:
                    if not self.__cells[row][col].visited:
                        adjacent[key] = (row, col)

            if not adjacent:
                self._draw_cell(i, j)
                return

            random_dir = random.choice(list(adjacent.keys()))
            ran_r = adjacent[random_dir][0]
            ran_c = adjacent[random_dir][1]
            match random_dir:
                case "up":
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[ran_r][ran_c].has_bottom_wall = False
                case "down":
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[ran_r][ran_c].has_top_wall = False
                case "left":
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[ran_r][ran_c].has_right_wall = False
                case "right":
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[ran_r][ran_c].has_left_wall = False

            self._break_walls_r(ran_r, ran_c)


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
