from core.TetrisBlock import (
    TetrisBlock,
    BlockId,
)
from core.TetrisBoard import (
    TetrisBoard,
)


from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    Optional,
)


@dataclass
class TetrisEngine:
    blockTypes: List[TetrisBlock] = field(default_factory=list)
    board_width: int = 10

    def __post_init__(
        self,
    ):
        if not self.blockTypes:  # If blocks list is empty, populate with default blocks
            q_block = TetrisBlock(
                block_id=BlockId.Q,
                matrix=[
                    [
                        1,
                        1,
                    ],
                    [
                        1,
                        1,
                    ],
                ],
            )

            x_block = TetrisBlock(
                block_id=BlockId.X,
                matrix=[
                    [
                        0,
                        1,
                    ],
                    [
                        1,
                        1,
                    ],
                    [
                        1,
                        0,
                    ],
                ],
            )

            z_block = TetrisBlock(
                block_id=BlockId.Z,
                matrix=[
                    [
                        1,
                        1,
                        0,
                    ],
                    [
                        0,
                        1,
                        1,
                    ],
                ],
            )

            s_block = TetrisBlock(
                block_id=BlockId.S,
                matrix=[
                    [
                        0,
                        1,
                        1,
                    ],
                    [
                        1,
                        1,
                        0,
                    ],
                ],
            )

            t_block = TetrisBlock(
                block_id=BlockId.T,
                matrix=[
                    [
                        1,
                        1,
                        1,
                    ],
                    [
                        0,
                        1,
                        0,
                    ],
                ],
            )

            i_block = TetrisBlock(
                block_id=BlockId.I,
                matrix=[
                    [
                        1,
                        1,
                        1,
                        1,
                    ],
                ],
            )

            l_block = TetrisBlock(
                block_id=BlockId.L,
                matrix=[
                    [
                        1,
                        0,
                    ],
                    [
                        1,
                        0,
                    ],
                    [
                        1,
                        0,
                    ],
                    [
                        1,
                        1,
                    ],
                ],
            )

            j_block = TetrisBlock(
                block_id=BlockId.J,
                matrix=[
                    [
                        0,
                        1,
                    ],
                    [
                        0,
                        1,
                    ],
                    [
                        0,
                        1,
                    ],
                    [
                        1,
                        1,
                    ],
                ],
            )

            # Add the blocks to the engine's blocks list
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

    def __find_block_type(
        self,
        block_id: str,
    ) -> Optional[TetrisBlock]:
        for block_type in self.blockTypes:
            if block_type.block_id.value == block_id:
                return block_type

    def process_line(
        self,
        line: str,
    ) -> int:
        # print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(f'Processing line {line}')
        # print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        tetris_board = TetrisBoard(width=self.board_width)
        items = line.split(",")

        for item in items:
            print(f"Processing item {item}")
            block_type = item[0]  # Assumption: Block ids are one character only
            column_index = int(item[1:])  # Assumption: Positions are valid numbers

            block = self.__find_block_type(block_type)
            if block:
                tetris_board.drop_block_at_column(
                    block,
                    column_index,
                )
            print("\n\n")
        # print(tetris_board)
        # return tetris_board.get_board_height()
