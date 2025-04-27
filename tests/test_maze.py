import sys
sys.path.append("D:\\dev\\courses\\boot.dev\\bootdev_maze_solver\\src")

import unittest
from src.maze import Maze


class MazeTest(unittest.TestCase):



    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.get_cells()), num_cols)
        self.assertEqual(len(m1.get_cells()[0]), num_rows)

    def test_entrance_and_exit(self):
        m1 = Maze(0, 0, 12, 10, 10, 10)
        self.assertEqual(m1.get_cells()[0][0].has_top_wall, False)
        self.assertEqual(m1.get_cells()[9][11].has_bottom_wall, False)



if __name__ == "__main__":
    unittest.main()
