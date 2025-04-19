from window import Window
from line import Line
from vector2 import Vector2
from cell import Cell

def main():

    win = Window(1920, 1080)

    #cell = Cell(Vector2(100, 100), Vector2(300, 300), win)
    # cell.has_right_wall = False
    # cell2 = Cell(Vector2(300, 300), Vector2(500, 500), win)
    # cell2.has_top_wall = False
    cell3 = Cell(Vector2(500, 250), Vector2(700, 200), win)
    # cell3.has_bottom_wall = False
    cell4 = Cell(Vector2(400, 100), Vector2(500, 150), win)
    cell5 = Cell(Vector2(2, 2), Vector2(550, 750), win)
    cell5.has_right_wall = False
    #cell.draw()
    # cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()




    win.wait_for_close()











if __name__ == "__main__":
    main()