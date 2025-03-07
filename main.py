from Window_Class import *
from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    point1 = Point(400, 300)
    point2 = Point(400, 600)
    point3 = Point(35, 600)
    point4 = Point(84, 320)
    line = Line(point1, point2)
    line2 = Line(point3, point4)
    win.draw_line(line2, "red")
    win.draw_line(line, "blue")

    
    win.wait_for_close()







if __name__ == "__main__":
    main()