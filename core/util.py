import numpy as np
from numpy import ndarray
from tabulate import tabulate

def sub_box(matrix: ndarray, cols: int, rows: int, start_row: int, start_col: int):  
  # Create an initial submatrix filled with zeros
  submatrix = np.zeros((rows, cols), dtype=int)

  # Determine valid ranges for row and col
  row_end = min(start_row + rows, matrix.shape[0])
  col_end = min(start_col + cols, matrix.shape[1])

  # Adjust start indices for submatrix assignment based on the original matrix's bounds
  submatrix_row_start = max(0, -start_row)
  submatrix_col_start = max(0, -start_col)

  # Adjust end indices for submatrix assignment based on the original matrix's bounds
  submatrix_row_end = submatrix_row_start + (row_end - max(0, start_row))
  submatrix_col_end = submatrix_col_start + (col_end - max(0, start_col))

  # Adjust start indices for M when they are negative
  start_row = max(0, start_row)
  start_col = max(0, start_col)

  
  # Copy over valid values from the original matrix to the submatrix
  submatrix[submatrix_row_start:submatrix_row_end, submatrix_col_start:submatrix_col_end] = matrix[start_row:row_end, start_col:col_end]
  return submatrix


if __name__ == '__main__':
  matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
  ])
  start_row = -2
  start_col = 0  # These values can be out of the matrix range or negative
  rows = 2
  cols = 2

  sub_box(matrix, cols, rows, start_row, start_col)

