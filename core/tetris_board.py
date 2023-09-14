from dataclasses import (
    dataclass,
    field,
)

from typing import List, Optional
from tabulate import (
    tabulate,
)

from core.tetris_block import (
    BlockId,
    TetrisBlock,
)


from core.tetris_block_factory import TetrisBlockFactory

from numpy import ndarray
import numpy as np

@dataclass
class TetrisBoard:
    board: ndarray = None
    blockTypes: List[TetrisBlock] = field(default_factory=list)
    default_board_width: int = 10

    def __post_init__(
        self,
    ):
        """Initialises the blocks."""
        # fmt: off
        if not self.blockTypes:  # If blocks list is empty, populate with default blocks
            q_block = TetrisBlockFactory.create_tetris_block(BlockId.Q)
            x_block = TetrisBlockFactory.create_tetris_block(BlockId.X)
            z_block = TetrisBlockFactory.create_tetris_block(BlockId.Z)
            s_block = TetrisBlockFactory.create_tetris_block(BlockId.S)
            t_block = TetrisBlockFactory.create_tetris_block(BlockId.T)
            i_block = TetrisBlockFactory.create_tetris_block(BlockId.I)
            l_block = TetrisBlockFactory.create_tetris_block(BlockId.L)
            j_block = TetrisBlockFactory.create_tetris_block(BlockId.J)

            self.blockTypes += [
                x_block,
                q_block,
                z_block,
                s_block,
                t_block,
                i_block,
                l_block,
                j_block,
            ]
            # fmt: on
    
    def find_block_type(
        self,
        block_id: str,
    ) -> Optional[TetrisBlock]:
        for block_type in self.blockTypes:
            if block_type.block_id.value == block_id:
                return block_type

    @property
    def height(self):
        return self.board.shape[0]

    @property
    def width(self):
        return self.board.shape[1]


    def get_board_box(self, start_row: int, start_col: int, cols: int, rows: int):
        """Fetches rows from a Bigtable.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by big_table.  Silly things may happen if
        other_silly_variable is not None.

        Args:
            big_table: An open Bigtable Table instance.
            keys: A sequence of strings representing the key of each table row
                to fetch.
            other_silly_variable: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

            {'Serak': ('Rigel VII', 'Preparer'),
                'Zim': ('Irk', 'Invader'),
                'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        # Create an initial box filled with zeros
        matrix_box = np.zeros((rows, cols), dtype=int)

        row_end = min(start_row + rows, self.height)
        col_end = min(start_col + cols, self.width)

        # Adjust start indexes for matrix_box based on the original matrix's bounds
        matrix_box_row_start = max(0, -start_row)
        matrix_box_col_start = max(0, -start_col)

        # Adjust end indices for matrix_box assignment based on the original matrix's bounds
        matrix_box_row_end = matrix_box_row_start + (row_end - max(0, start_row))
        matrix_box_col_end = matrix_box_col_start + (col_end - max(0, start_col))

        # Adjust indexes when they are negative
        start_row = max(0, start_row)
        start_col = max(0, start_col)

        # Copy over valid values from the original matrix to the matrix_box
        matrix_box[matrix_box_row_start:matrix_box_row_end, matrix_box_col_start:matrix_box_col_end] = self.board[start_row:row_end, start_col:col_end]
        return matrix_box

    def drop_block_at_column(self, block: TetrisBlock, colIdx: int) -> int:
        """Fetches rows from a Bigtable.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by big_table.  Silly things may happen if
        other_silly_variable is not None.

        Args:
            big_table: An open Bigtable Table instance.
            keys: A sequence of strings representing the key of each table row
                to fetch.
            other_silly_variable: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

            {'Serak': ('Rigel VII', 'Preparer'),
                'Zim': ('Irk', 'Invader'),
                'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        # Init board if needed, of the same of the first block
        if self.board is None:
            self.board = np.zeros((block.height, self.default_board_width))

        # Cap the col taking into account the width of the block and the board.
        colIdx = block.width - colIdx if colIdx + block.width > self.width else colIdx

        # Represents the potential row (x dimension) where the block might be.
        # It starts with an initial value of matrix_height - block.height
        potential_row = self.height - block.height

        # Indicates if there would be a collision if the block would be put in (potential_row, col)
        is_there_a_collision = True

        # Get the box of where the block would be if it was positioned in (potential_row, col)
        # Keep decrementing potential_row until there isn't a collision (is_there_a_collision)
        while is_there_a_collision:
            # Get the potential area in the board (potential_row, col)
            board_box = self.get_board_box(potential_row, colIdx, block.width, block.height)

            # Sum up both matrixes, the block and the current potential area in the board (board_box).
            sum_result = np.add(board_box, block.matrix)
            # If there is at least one element 2 or higher then there is a collision
            is_there_a_collision = np.any(sum_result >= 2)

            # Move up one position if there was a collision
            if is_there_a_collision:
                potential_row = potential_row - 1

        number_of_rows_to_insert = 0 if potential_row > 0 else abs(potential_row)

        # Insert rows in the board at the top, if needed
        if number_of_rows_to_insert > 0:
            zeros = np.zeros((number_of_rows_to_insert, self.width))
            self.board = np.insert(self.board, 0, zeros, axis=0)

        # Coordinates (x, y) are given, for example
        x = potential_row if potential_row > 0 else 0
        y = colIdx

        # Create a mask so only the 0 are copied from the block to the board.
        mask = block.matrix == 1
        # Copy the 1s from the block to the sub-area in the board
        self.board[x : x + block.height, y : y + block.width][mask] = 1

        self.remove_filled_rows()

        return self.height

    def remove_filled_rows(self) -> ndarray:
        mask_of_filled_rows = np.all(self.board == 1, axis=1)  # axis:1 means column, we aggregate along columns

        # 'where' returns a tuple of rows and columns where the condition match, we only need rows in this case
        indexes_to_delete = np.where(mask_of_filled_rows)[0]

        board_without_filled_rows = np.delete(self.board, indexes_to_delete, axis=0)  # axis:0 means row

        self.board = board_without_filled_rows

    def __str__(
        self,
    ):
        return tabulate(
            self.board,
            tablefmt="grid",
        )
