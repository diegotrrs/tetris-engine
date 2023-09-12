from dataclasses import dataclass
from typing import List
from enum import Enum
from tabulate import tabulate


class BlockId(Enum):
    Q = "Q"
    Z = "Z"
    S = "S"
    T = "T"
    I = "I"
    L = "L"
    J = "J"
    X = "X"


@dataclass
class TetrisBlock:
    EMPTY_SPACE = "0"
    NON_EMPTY_SPACE = "1"

    block_id: BlockId
    matrix: List[List[str]]

    def get_width(self) -> int:
        """Return the width of the Tetris block."""
        return len(self.matrix[0]) if self.matrix else 0

    def get_height(self) -> int:
        """Return the height of the Tetris block."""
        return len(self.matrix)
    
    def get_column(self, col_id: int) -> List[str]:
        """Return the specified column as a list."""
        return [row[col_id] for row in self.matrix]
    
    def __str__(self):
        # for row_idx, row in enumerate(self.matrix):
        #     for cell_idx, cell in enumerate(row):
        #         print(f"Row {row_idx}, Column {cell_idx}: {cell}")
        return tabulate(self.matrix, tablefmt="grid")
    
    def count_consecutive_non_empty_from_bottom(self, column_index: int) -> int:
        """Count consecutive NON_EMPTY_SPACE cells from the bottom to the top for a specific column."""
        count = 0
        for row in reversed(self.matrix):
            if row[column_index] == TetrisBlock.NON_EMPTY_SPACE:
                count += 1
            else:
                break  # stop counting when an EMPTY_SPACE is encountered
        return count

    def __post_init__(self):
        # Check if all matrix cells contain either the blockId or a space
        for row in self.matrix:
            for cell in row:
                if (
                    cell != TetrisBlock.EMPTY_SPACE
                    and cell != TetrisBlock.NON_EMPTY_SPACE
                ):
                    raise ValueError(
                        f"Invalid value {cell} in matrix for block {self.block_id}"
                    )
