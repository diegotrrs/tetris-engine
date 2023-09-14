import unittest

import numpy as np
from core.tetris_board import TetrisBoard

# fmt: off
# Include tests cases to test the remove filled rows method of Tetris Board.
class TestRemoveFilledRows(unittest.TestCase):
        
    def test_remove_filled_rows_no_rows_actually_filled(
        self,
    ):
        matrix = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )       

        tetris_board = TetrisBoard()
        tetris_board.board = matrix
      
        tetris_board.remove_filled_rows()

        expected_result = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                expected_result,
            )
        ) 

    def test_remove_filled_rows_1_row_filled(
        self,
    ):
        matrix = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 1, 1, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = matrix
      
        tetris_board.remove_filled_rows()

        expected_result = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                expected_result,
            )
        )

    def test_remove_filled_rows_all_rows_filled(
        self,
    ):
        matrix = np.array(
            [
                [ 1, 1, 1, 1 ],
                [ 1, 1, 1, 1 ],
                [ 1, 1, 1, 1 ],
                [ 1, 1, 1, 1 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = matrix
        tetris_board.remove_filled_rows()

        self.assertEqual(len(tetris_board.board), 0 )  

if __name__ == "__main__":
    unittest.main()
# fmt: on
