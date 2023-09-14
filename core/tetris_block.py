from dataclasses import (
    dataclass,
)

from enum import (
    Enum,
)
from numpy import ndarray

from tabulate import (
    tabulate,
)


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
    block_id: BlockId
    matrix: ndarray

    @property
    def height(self):
        return self.matrix.shape[0]

    @property
    def width(self):
        return self.matrix.shape[1]

    def __str__(
        self,
    ):
        return tabulate(
            self.matrix,
            tablefmt="grid",
        )
