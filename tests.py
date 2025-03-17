import unittest 
from Maze_Class import Maze 
from Window_Class import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        maze1._reset_cells_visited()
        for row in maze1._cells: 
            for cell in row:
                self.assertEqual(cell.visited, False)

    
if __name__ == "__main__":
    unittest.main()