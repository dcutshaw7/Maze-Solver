from Window_Class import *
from tkinter import Tk, BOTH, Canvas
from Cell_Class import *

def main():
    win = Window(800, 600)
    test_cell = Cell(win, 50, 100,150, 200)
    test_cell2 = Cell(win, 300, 400, 500, 600)
    test_cell.has_bottom_wall = False 
    test_cell.draw()
    test_cell2.draw()
    win.wait_for_close()







if __name__ == "__main__":
    main()