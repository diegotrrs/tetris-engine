import unittest

import numpy as np
from core import tetris_block
from core.tetris_block_factory import TetrisBlockFactory
from core.tetris_board import TetrisBoard


# fmt: off
''' 
Include tests for drop_block_at_board when it does not result in new top rows added.
'''
class TestDropBlockAtBoardNoTopRowsAdded(unittest.TestCase):

    def test_drop_block_at_board_at_column_0(
        self,
    ):
        board_with_z_on_it = np.array(
            [
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
                [ 0, 1, 1, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_z_on_it

        t_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T)

        column_to_be_dropped_at = 0

        height = tetris_board.drop_block_at_column(t_block, column_to_be_dropped_at)
        
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [
                        [ 1, 1, 1, 0 ],
                        [ 0, 1, 0, 0 ],
                        [ 1, 1, 0, 0 ],
                        [ 0, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            4
        )

    def test_drop_block_at_board_at_column_1(
        self,
    ):
        board_with_z_on_it = np.array(
            [
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
                [ 0, 1, 1, 0 ],
            ]
        )

        t_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T)

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_z_on_it

        column_to_be_dropped_at = 1

        height = tetris_board.drop_block_at_column(t_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [
                        [ 0, 0, 0, 0 ],
                        [ 0, 1, 1, 1 ],
                        [ 1, 1, 1, 0 ],
                        [ 0, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            4
        )

    def test_drop_block_at_board_at_column_2(
        self,
    ):
        board_with_z_on_it = np.array(
            [
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
                [ 0, 1, 1, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_z_on_it

        t_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T)

        column_to_be_dropped_at = 2

        height = tetris_board.drop_block_at_column(t_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [
                        [ 0, 0, 0, 0 ],
                        [ 0, 1, 1, 1 ],
                        [ 1, 1, 1, 0 ],
                        [ 0, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            4
        )

    
''' 
Include tests for drop_block_at_board when it results in new top rows added.
'''
class TestDropBlockAtBoardTopRowsAreAdded(unittest.TestCase):

    def test_drop_block_at_board_resulting_in_1_row_added(
        self,
    ):
        board_with_l_on_it = np.array(
            [
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_l_on_it

        t_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T)

        column_to_be_dropped_at = 0

        height = tetris_board.drop_block_at_column(t_block, column_to_be_dropped_at)

        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        [ 1, 1, 1, 0 ],                     
                        [ 1, 1, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 1, 0, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            5
        )

    def test_drop_block_at_board_resulting_in_2_rows_added(
        self,
    ):
        board_with_z_on_it = np.array(
            [
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
                [ 0, 1, 1, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_z_on_it

        l_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.L)

        column_to_be_dropped_at = 1

        height = tetris_board.drop_block_at_column(l_block, column_to_be_dropped_at)

        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [                        
                        [ 0, 1, 0, 0 ],
                        [ 0, 1, 0, 0 ],
                        [ 0, 1, 0, 0 ],
                        [ 0, 1, 1, 0 ],
                        [ 1, 1, 0, 0 ],
                        [ 0, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            6
        )

    def test_drop_block_at_board_resulting_in_4_row_added(
        self,
    ):
        board_with_l_on_it = np.array(
            [
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 1, 0, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board_with_l_on_it

        l_block = TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.L)

        column_to_be_dropped_at = 0

        height = tetris_board.drop_block_at_column(l_block, column_to_be_dropped_at)

        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        [ 1, 0, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 1, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 0, 0, 0 ],
                        [ 1, 1, 0, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            8
        )
    

if __name__ == "__main__":
    unittest.main()
# fmt: on
