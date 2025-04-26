from maze import Maze
from window import Window


def main():

    win = Window(1920, 1080)

    Maze(10, 10, 10, 10, 100, 100, win)

    win.wait_for_close()






if __name__ == "__main__":
    main()
