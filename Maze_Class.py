from tkinter import Tk, BOTH, Canvas
from Window_Class import Window
from Cell_Class import *
from Point_Class import Point, Line
import time 
import random

class Maze: 
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1 
        self.y1 = y1 
        self.num_rows = num_rows 
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win 
        if seed is not None: 
            random.seed(seed) 

        self._create_cells()
        self._break_walls()
        self._break_entrance_and_exit()
        self._reset_cells_visited()
       

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):  
            row = []
            for j in range(self.num_cols):  
                x1 = self.x1 + (j * self.cell_size_x)  
                y1 = self.y1 + (i * self.cell_size_y)  
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y 
                cell = Cell(self.win, x1, y1, x2, y2)
                row.append(cell)
            self._cells.append(row)

    def _draw_cell(self, i, j,): 
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self): 
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self): 
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_top_wall = False 
        exit.has_bottom_wall = False 
        self._draw_cell(0,0)
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True 
        self._draw_cell(i, j)
        while True: 
            possible_directions = []
            if i > 0 and not self._cells[i-1][j].visited: 
                possible_directions.append((i-1, j, "up"))
            
            if j < self.num_cols - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1, "right"))
            
            if i < self.num_rows - 1 and not self._cells[i+1][j].visited: 
                possible_directions.append((i+1, j, "down"))

            if j > 0 and not self._cells[i][j-1].visited: 
                possible_directions.append((i, j-1, "left"))

            if len(possible_directions) == 0: 
                return 
            
            next_i, next_j, direction = random.choice(possible_directions)

            if direction == "up": 
                self._cells[i][j].has_top_wall = False 
                self._cells[next_i][next_j].has_bottom_wall = False 
            
            elif direction == "down": 
                self._cells[i][j].has_bottom_wall = False 
                self._cells[next_i][next_j].has_top_wall = False 
            
            elif direction == "right": 
                self._cells[i][j].has_right_wall = False 
                self._cells[next_i][next_j].has_left_wall = False 
            
            elif direction == "left": 
                self._cells[i][j].has_left_wall = False 
                self._cells[next_i][next_j].has_right_wall = False 
            
            self._break_walls_r(next_i, next_j)
            
    def _break_walls(self): 
        self._break_walls_r(0,0)

    def _reset_cells_visited(self): 
        for row in self._cells: 
            for cell in row:
                cell.visited = False

    def _solve_r(self, i=0, j=0): 
        self._animate()
        self._cells[i][j].visited = True 
        if self._cells[i][j] == self._cells[-1][-1]:
            return True 
        
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if j < self.num_cols - 1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if i < self.num_rows -1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_bottom_wall: 
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True 
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True 
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        return False     

    def solve(self): 
        return self._solve_r(0,0)
        
