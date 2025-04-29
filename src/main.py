import time
from maze import Maze
from window import Window


def main():

    win = Window(1920, 1080)

    maze = Maze(3, 3, 10, 10, 100, 100, win, time.time())
    maze.solve()
    
    win.wait_for_close()






if __name__ == "__main__":
    main()
