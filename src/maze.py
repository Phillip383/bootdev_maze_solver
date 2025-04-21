

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.cells = [[]]
    
    def _create_cells(self):
        ...

    def _draw_cell(self, i, j):
        ...
    
    def _animate(self):
        ...