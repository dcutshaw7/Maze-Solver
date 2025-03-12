from Window_Class import *
from tkinter import Tk, BOTH, Canvas
from Cell_Class import *
from Maze_Class import Maze
import time 

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 15, 40, 40, win)
    time.sleep(5)
    win.wait_for_close()







if __name__ == "__main__":
    main()