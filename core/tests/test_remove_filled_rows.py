import unittest

import numpy as np
from core.util import (
    remove_filled_rows,
)
# fmt: off
class TestRemoveFilledRows(unittest.TestCase):
    def remove_filled_rows_no_rows_actually_filled(
        self,
    ):
        board = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )
      
        result_matrix = remove_filled_rows(board)

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
                result_matrix,
                expected_result,
            )
        ) 

    def test_remove_filled_rows_1_row_filled(
        self,
    ):
        board = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 1, 1, 1, 1 ],
                [ 0, 1, 0, 1 ],
            ]
        )
      
        result_matrix = remove_filled_rows(board)

        expected_result = np.array(
            [
                [ 0, 1, 1, 1 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 0, 1 ],
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