from window import Window
from line import Line
from vector2 import Vector2

def main():

    win = Window(800, 600)
    
    line1 = Line(Vector2(0, 0), Vector2(200, 150))
    line2 = Line(Vector2(200, 150), Vector2(800, 0))
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")



    win.wait_for_close()











if __name__ == "__main__":
    main()