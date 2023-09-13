import unittest

import numpy as np
from core.util import (
    drop_block_at_board,
)
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

        t_block = np.array(
            [
                [ 1, 1, 1 ],
                [ 0, 1, 0 ],                             
            ]
        )

        column_to_be_dropped_at = 0

        result = drop_block_at_board(board_with_z_on_it, t_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                result,
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

        t_block = np.array(
            [
                [ 1, 1, 1 ],
                [ 0, 1, 0 ],                             
            ]
        )

        column_to_be_dropped_at = 1

        result = drop_block_at_board(board_with_z_on_it, t_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                result,
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

        t_block = np.array(
            [
                [ 1, 1, 1 ],
                [ 0, 1, 0 ],                             
            ]
        )

        column_to_be_dropped_at = 2

        result = drop_block_at_board(board_with_z_on_it, t_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                result,
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

        t_block = np.array(
            [
                [ 1, 1, 1 ],
                [ 0, 1, 0 ],
            ]
        )

        column_to_be_dropped_at = 0

        result = drop_block_at_board(board_with_l_on_it, t_block, column_to_be_dropped_at)

        self.assertTrue(
            np.array_equal(
                result,
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

        l_block = np.array(
            [
                [ 1, 0 ],
                [ 1, 0 ],
                [ 1, 0 ],
                [ 1, 1 ],                             
            ]
        )

        column_to_be_dropped_at = 1

        result = drop_block_at_board(board_with_z_on_it, l_block, column_to_be_dropped_at)
        self.assertTrue(
            np.array_equal(
                result,
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

        l_block = np.array(
            [
                [ 1, 0 ],
                [ 1, 0 ],
                [ 1, 0 ],
                [ 1, 1 ],
            ]
        )

        column_to_be_dropped_at = 0

        result = drop_block_at_board(board_with_l_on_it, l_block, column_to_be_dropped_at)

        self.assertTrue(
            np.array_equal(
                result,
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
    

if __name__ == "__main__":
    unittest.main()
# fmt: on