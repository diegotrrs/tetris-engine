 #
 start_row no uede ser menor de -2 o se cae
 
 def test_sub_matrix_outside_all_ranges(self):
        matrix = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        start_row = -2
        start_col = 0
        rows = 2
        cols = 2
        result_matrix = sub_box(matrix, cols, rows, start_row, start_col)
        print(result_matrix)

        expected_result = np.array([[0, 0], [0, 0]])    