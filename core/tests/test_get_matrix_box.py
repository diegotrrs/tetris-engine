import unittest

import numpy as np
from core.tetris_board import TetrisBoard

# fmt: off

# Include tests for the get_board_box method used to get sub-areas of the matrix. This method could be private to TetrisBoard but it's worth testing it.
class TestGetMatrixBox(unittest.TestCase):
    def test_get_matrix_box_inside_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        start_row = 0
        start_col = 0
        rows = 2
        cols = 2
        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
                [ 1, 2 ],
                [ 5, 6 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )

    def test_get_matrix_box_outside_top_row_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )
        start_row = -1
        start_col = 0
        rows = 2
        cols = 2

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
                [ 0, 0 ],
                [ 1, 2 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )

    def test_get_matrix_box_outside_bottom_row_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )
        start_row = 4
        start_col = 0
        rows = 2
        cols = 2

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
                [ 0, 0 ],
                [ 0, 0 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )

    def test_get_matrix_box_outside_left_col_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )
        start_row = 2
        start_col = -1
        rows = 2
        cols = 2

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
                [ 0, 9 ],
                [ 0, 13 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )

    def test_get_matrix_box_outside_right_col_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )
        start_row = 2
        start_col = 3
        rows = 2
        cols = 2

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
                [ 12, 0 ],
                [ 16, 0 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )

    def test_get_matrix_box_outside_all_ranges(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 2, 3, 4 ],
                [ 5 ,6, 7, 8 ],
                [ 9, 10, 11, 12 ],
                [ 13 ,14, 15, 16 ],
            ]
        )
        start_row = -2
        start_col = -2
        rows = 2
        cols = 2

        tetris_board = TetrisBoard()
        tetris_board.board = matrix

        result_matrix = tetris_board.get_board_box(
            start_row,
            start_col,
            cols,
            rows,            
        )

        expected_result = np.array(
            [
               [ 0, 0 ],
               [ 0, 0 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                result_matrix,
                expected_result,
            )
        )


if __name__ == "__main__":
    unittest.main()
# fmt: on
