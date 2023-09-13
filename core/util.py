# import numpy as np
# from tabulate import tabulate

# M = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])


# if __name__ == '__main__':
#   start_row = 5
#   rows = 2
#   start_col = 0
#   cols = 2
#   submatrix = M[start_row:start_row+rows, start_col:start_col+cols]  
#   print(tabulate(submatrix, tablefmt="grid"))


# from ast import List
# from collections import deque
# from typing import Deque


# def sub_matrix(board: Deque, block: List[List[int]], x: int, y: int):
#   print('')


# if __name__ == '__main__':
#   board = [
#     [0,1,0,0,0],
#     [0,1,0,0,0],
#     [0,1,0,0,0],
#     [1,1,0,0,0]
#   ]

#   block = [
#       [0,1],
#       [1,1],
#       [1,0]
#   ]

#   sub_matrix(deque(board), block, )

import numpy as np
from numpy import ndarray
from tabulate import tabulate

def sub_box(matrix: ndarray, box_width: int, box_height: int, start_row: int, start_col: int):
  #matrix = M[::-1]
  sub_matrix = np.zeros((box_width, box_height))  
  matrix_height = M.shape[0]
  matrix_width = M.shape[1]  
  print('_______________________________________________________________')
  print('_______________________________________________________________')
  print(f'box size box_height {box_height} x box_width {box_width}')
  print(f'starting at start_row {start_row} x start_col {start_col}')
  print(tabulate(matrix))

  #print(tabulate(sub_matrix))
  print(f'matrix_height matrix_width {matrix_height} {matrix_width}')

  row_end = min(start_row + box_height, matrix_height)
  col_end = min(start_col + box_width, matrix_width)

  print(f'row_end {row_end} col_end {col_end}')
  

  sub_matrix[:row_end-start_row, :col_end-start_col] = matrix[start_row:row_end, start_col:col_end]
  print(tabulate(sub_matrix))


if __name__ == '__main__':
  M = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
  ])
  box_height = 2
  box_width = 2
  x = 3
  y = 3
  sub_box(M, box_width, box_height, x, y)

if __name__ == '__main__a':
  M = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
  ])

  start_row, start_col = 3, 0  # These values can be out of the matrix range
  rows, cols = 2, 2
  submatrix = np.zeros((rows, cols))

  # Determine valid ranges for row and col
  row_end = min(start_row + rows, M.shape[0])
  col_end = min(start_col + cols, M.shape[1])

  # Compute the number of rows and columns that were outside the range
  outside_rows = (start_row + rows) - row_end
  outside_cols = (start_col + cols) - col_end

  submatrix[:row_end-start_row, :col_end-start_col] = M[start_row:row_end, start_col:col_end]

  print(tabulate(submatrix))
  print(f"Number of rows outside the range: {outside_rows}")
  print(f"Number of columns outside the range: {outside_cols}")

