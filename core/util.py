import numpy as np
from numpy import ndarray

def get_matrix_box(matrix: ndarray, cols: int, rows: int, start_row: int, start_col: int):
    # Create an initial box filled with zeros
    matrix_box = np.zeros((rows, cols), dtype=int)

    row_end = min(start_row + rows, matrix.shape[0])
    col_end = min(start_col + cols, matrix.shape[1])

    # Adjust start indices for matrix_box assignment based on the original matrix's bounds
    matrix_box_row_start = max(0, -start_row)
    matrix_box_col_start = max(0, -start_col)

    # Adjust end indices for matrix_box assignment based on the original matrix's bounds
    matrix_box_row_end = matrix_box_row_start + (row_end - max(0, start_row))
    matrix_box_col_end = matrix_box_col_start + (col_end - max(0, start_col))

    # Adjust start indices when they are negative
    start_row = max(0, start_row)
    start_col = max(0, start_col)

    # Copy over valid values from the original matrix to the matrix_box
    matrix_box[matrix_box_row_start:matrix_box_row_end, matrix_box_col_start:matrix_box_col_end] = matrix[start_row:row_end, start_col:col_end]
    return matrix_box


def drop_block_at_board(board: ndarray, block: ndarray, col: int) -> ndarray:
    block_height, block_width = block.shape
    board_height, board_width = board.shape

    # Cap the col taking into account the width of the block and the board.
    col = block_width - col if col + block_width > board_width else col

    # Represents the potential row (x dimension) where the block might be.
    # It starts with an initial value of matrix_height - block_height
    potential_row = board_height - block_height

    # Indicates if there would be a collision if the block would be put in (potential_row, col)
    is_there_a_collision = True

    # Get the box of where the block would be if it was positioned in (potential_row, col)
    # Keep decrementing potential_row until there isn't a collision (is_there_a_collision)
    while is_there_a_collision:
        # Get the potential area in the board (potential_row, col)
        board_box = get_matrix_box(board, block_width, block_height, potential_row, col)

        # Sum up both matrixes, the block and the current potential area in the board (board_box).
        sum_result = np.add(board_box, block)
        # If there is at least one element 2 or higher then there is a collision
        is_there_a_collision = np.any(sum_result >= 2)

        # Move up one position if there was a collision
        if is_there_a_collision:
            potential_row = potential_row - 1

    number_of_rows_to_insert = 0 if potential_row > 0 else abs(potential_row)

    new_board = board.copy()
    # Insert rows in the board at the top, if needed
    if number_of_rows_to_insert > 0:
        zeros = np.zeros((number_of_rows_to_insert, board_width))
        new_board = np.insert(board, 0, zeros, axis=0)

    # Coordinates (x, y) are given, for example
    x = potential_row if potential_row > 0 else 0
    y = col

    # Create a mask so only the 0 are copied from the block to the board.
    mask = block == 1
    # Copy the 1s from the block to the sub-area in the board
    new_board[x : x + block_height, y : y + block_width][mask] = 1

    return new_board

def remove_filled_rows(board: ndarray) -> ndarray:
    mask_of_filled_rows = np.all(board == 1, axis=1) # axis:1 means column, we aggregate along columns

    # 'where' returns a tuple of rows and columns where the condition match, we only need rows in this case
    indexes_to_delete = np.where(mask_of_filled_rows)[0] 

    board_without_filled_rows = np.delete(board, indexes_to_delete, axis=0) # axis:0 means row

    return board_without_filled_rows
