from collections import deque
from dataclasses import dataclass, field
from typing import Deque, List
from tabulate import tabulate
from core.TetrisBlock import TetrisBlock


@dataclass
class TetrisBoard:
    CHARACTER_FOR_EMPTY_CELL = "0"
    width: int
    """
     The reason we use default_factory for mutable objects, like lists, is to prevent unexpected behavior due to shared references. For instance, if you were to set data=[] directly as the default value, every instance of the dataclass would share the same list, which is rarely what you want. Using default_factory=list ensures each instance gets its own unique list.
    """
    board: Deque[List[str]] = field(default_factory=deque)

    def add_empty_row(self):
        self.board.appendleft([TetrisBoard.CHARACTER_FOR_EMPTY_CELL] * self.width)

    def add_empty_rows(self, rows_count: int):
        [self.add_empty_row() for _ in range(rows_count)]

    # Mark this as private
    def add_row(self, row: List[str]):
        if len(row) != self.width:
            raise ValueError(
                f"Row must have the same width of the board ({self.width})"
            )
        self.board.append(row)

    def get_board_height(self):
        return len(self.board)

    def set_cell(self, row_idx: int, column_idx: int, value):
        self.board[row_idx][column_idx] = value

    def is_cell_empty(self, row_idx: int, column_idx: int) -> bool:
        try:
            return (
                self.board[row_idx][column_idx] == TetrisBoard.CHARACTER_FOR_EMPTY_CELL
            )
        except IndexError:
            return False

    def get_first_empty_row_from_bottom_to_top(self, column_idx: int) -> int | None:
        board_height = self.get_board_height()
        for row_index in range(board_height - 1, -1, -1):  # Iterate it backwards
            if (
                self.board[row_index][column_idx]
                == TetrisBoard.CHARACTER_FOR_EMPTY_CELL
            ):
                return row_index

    def copy_matrix(self, block: TetrisBlock, start_row, start_col):
        # Iterate over each row and column of the source matrix
        for row in range(block.get_height()):
            for col in range(block.get_width()):
                # Calculate the position in the target matrix
                target_row = start_row + row
                target_col = start_col + col

                # Ensure we're not going out of bounds in the target matrix
                if 0 <= target_row < len(self.board) and 0 <= target_col < len(
                    self.board[0]
                ):
                    self.board[target_row][target_col] = block.get_value_at(row, col)

    def are_cells_clear(self, row_a, row_b, col):
        column_values = [row[col] for row in self.board[row_a:row_b]]
        # all(
        #     self.is_cell_empty(row, col)
        #     for row in range(row_b, row_a)
        # )

    def drop_block_at_column(self, block: TetrisBlock, col_idx: int):
        print(f">>>>>>>>>>>> BLOCK at {col_idx} >>>>>>")
        print(block)
        if col_idx > self.width:
            print("EXCEPTION")
            raise ValueError(
                f"Column index must be less than the board's width  ({self.width})"
            )
        block_height = block.get_height()
        block_width = block.get_width()

        if len(self.board) == 0:
            self.add_empty_rows(block_height)
            self.copy_matrix(block, 0, col_idx)

        print(">>>>>>>>>>>> BOARD >>>>>>")
        print(self)
        # self.check_for_filled_rows()

    def check_for_filled_rows(self):
        return

    def __str__(self):
        # for row_idx, row in enumerate(self.board):
        #     for cell_idx, cell in enumerate(row):
        #         print(f"Row {row_idx}, Column {cell_idx}: {cell}")
        return tabulate(self.board, tablefmt="grid")
