from cell import Cell
from vector2 import Vector2
from window import Window
from maze import Maze

def main():

    win = Window(1920, 1080)

    maze = Maze(10, 10, 5, 5, 50, 50, win)



    win.wait_for_close()






if __name__ == "__main__":
    main()
