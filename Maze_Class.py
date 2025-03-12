from tkinter import Tk, BOTH, Canvas
from Window_Class import Window
from Cell_Class import *
from Point_Class import Point, Line
import time 

class Maze: 
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win 
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols): 
            column = []
            for j in range(self.num_rows): 
                x1 = self.x1 + (i * self.cell_size_x)
                y1 = self.y1 + (j* self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y 
                cell = Cell(self.win, x1, y1, x2, y2)
                column.append(cell)
                
            self._cells.append(column)
    
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j): 
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self): 
        self.win.redraw()
        time.sleep(0.05)
