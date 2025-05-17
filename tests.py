from maze import *
from graphics import Window
import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, Window(1920, 1080))
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_init_breaks(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, Window(1920, 1080))
        m1.break_entrance_and_exit()
        self.assertEqual(m1.cells[0][0].has_top_wall, False)
        self.assertEqual(m1.cells[len(m1.cells) - 1][len(m1.cells[len(m1.cells) - 1]) - 1].has_bottom_wall, False)

    def test_reset(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10, Window(1920, 1080))
        m1.break_entrance_and_exit()
        m1.break_walls_r()
        m1.reset_cells_visited()
        self.assertEqual(m1.cells[0][0].visited, False)







if __name__ == "__main__":
    unittest.main()
