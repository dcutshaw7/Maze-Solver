from tkinter import Tk, BOTH, Canvas
from Point_Class import * 
from Window_Class import * 



class Cell: 
    def __init__(self, win, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self.__x1 = x1 
        self.__x2 = x2 
        self.__y1 = y1 
        self.__y2 = y2 
        self.win = win 
        self.visited = False 
    
    def draw(self, color="black"):
   
        left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.win.draw_line(left_wall, color if self.has_left_wall else "#d9d9d9")
    
        right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.win.draw_line(right_wall, color if self.has_right_wall else "#d9d9d9")
    
        top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.win.draw_line(top_wall, color if self.has_top_wall else "#d9d9d9")
    
        bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.win.draw_line(bottom_wall, color if self.has_bottom_wall else "#d9d9d9")
    
    def get_center(self):
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        return center_x, center_y
    
    def draw_move(self, to_cell, undo=False): 
        center_x1, center_y1 = self.get_center()
        center_x2, center_y2 = to_cell.get_center()
        line = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        color = "gray" if undo else "red"
        self.win.draw_line(line, color)