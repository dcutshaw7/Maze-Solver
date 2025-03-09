from Window_Class import *
from tkinter import Tk, BOTH, Canvas
from Cell_Class import *

def main():
    win = Window(800, 600)
    cell1 = Cell(win, 100, 200, 300, 400)
    cell1.has_right_wall = False 
    cell2 = Cell(win, 450, 500, 550, 600)
    cell2.has_left_wall = False 
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    
    win.wait_for_close()







if __name__ == "__main__":
    main()