from dataclasses import dataclass, field
from typing import List
from tabulate import tabulate
from core.TetrisBlock import TetrisBlock


@dataclass
class TetrisBoard:
    CHARACTER_FOR_EMPTY_CELL = " "
    width: int
    """
     The reason we use default_factory for mutable objects, like lists, is to prevent unexpected behavior due to shared references. For instance, if you were to set data=[] directly as the default value, every instance of the dataclass would share the same list, which is rarely what you want. Using default_factory=list ensures each instance gets its own unique list.
    """
    board: List[List[str]] = field(default_factory=list)

    def add_empty_row(self):
        self.board.append([TetrisBoard.CHARACTER_FOR_EMPTY_CELL] * self.width)

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
    
    def is_cell_empty(self, row_idx: int, column_idx: int) -> bool:
        try:
            return self.board[row_idx][column_idx] == TetrisBoard.CHARACTER_FOR_EMPTY_CELL
        except IndexError:
            return False

    def drop_block_at_column(self, block: TetrisBlock, column_index: int):
        if column_index > self.width:
            raise ValueError(
                f"Column index must be less than the board's width  ({self.width})"
            )
        print('drop_block_at_column')
        first_row_with_empty_space_at_column_index = None
        for row_index in enumerate(self.board):
            if self.board[row_index][column_index] == TetrisBoard.CHARACTER_FOR_EMPTY_CELL:
                first_row_with_empty_space_at_column_index = row_index

        print(f'first_row_with_empty_space_at_column_index {first_row_with_empty_space_at_column_index}')

        new_block_height = block.get_height()
        if first_row_with_empty_space_at_column_index is None:
            print(f'Adding empty {new_block_height} rows')
            first_row_with_empty_space_at_column_index = 0
            self.add_empty_rows(new_block_height)

        # for row_idx, row in enumerate(block.matrix):
        #     for cell_idx, cell in enumerate(row):
        #         print(f"Row {row_idx}, Column {cell_idx}: {cell}")

        for block_column_idx in range(block.get_width()):
            spaces_needed = block.count_consecutive_non_empty_from_bottom(block_column_idx)
            print(f" {column_index} -->  {spaces_needed} ")

            is_all_cells_empty = all(
                self.is_cell_empty(row, column_index)
                for row in range(
                    first_row_with_empty_space_at_column_index,
                    first_row_with_empty_space_at_column_index + new_block_height
                )
            )
            print('xxx')
            # for row in range(
            #     first_row_with_empty_space_at_column_index,
            #     first_row_with_empty_space_at_column_index + new_block_height
            # ):
            #     print(row)
        print(block)
        print(self)
        self.check_for_filled_rows()
        
        
    def check_for_filled_rows(self):
        return

    def __str__(self):
        for row_idx, row in enumerate(self.board):
            for cell_idx, cell in enumerate(row):
                print(f"Row {row_idx}, Column {cell_idx}: {cell}")
        return tabulate(self.board, tablefmt="grid")
