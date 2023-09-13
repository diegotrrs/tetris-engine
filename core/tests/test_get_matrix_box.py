import unittest

import numpy as np
from core.util import (
    get_matrix_box,
)
# fmt: off
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
        start_row = 0
        start_col = 0
        rows = 2
        cols = 2
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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
        result_matrix = get_matrix_box(
            matrix,
            cols,
            rows,
            start_row,
            start_col,
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