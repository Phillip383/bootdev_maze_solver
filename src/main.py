from window import Window
from line import Line
from vector2 import Vector2
from cell import Cell

def main():

    win = Window(1920, 1080)

    cell = Cell(Vector2(100, 100), Vector2(300, 300), win)
    cell.has_right_wall = False
    cell2 = Cell(Vector2(400, 100), Vector2(600, 300), win)
    cell2.has_left_wall = False
    cell.draw()
    cell2.draw()
    cell.draw_move(cell2)





    win.wait_for_close()











if __name__ == "__main__":
    main()