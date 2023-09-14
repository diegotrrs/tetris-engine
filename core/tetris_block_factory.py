from core.tetris_block import BlockId, TetrisBlock
import numpy as np


class TetrisBlockFactory:    
    # Factory that takes care of the creation of TetrisBlocks        
    @staticmethod
    def create_tetris_block(blockId: BlockId) -> TetrisBlock:
        blocks = {
            BlockId.Q: TetrisBlock(
                block_id=BlockId.Q,
                matrix = np.array([
                    [1, 1],
                    [1, 1],
                ]),
            ),
            BlockId.X: TetrisBlock(
                block_id=BlockId.X,
                matrix = np.array([
                    [0, 1],
                    [1, 1],
                    [1, 0],
                ]),
            ),
            BlockId.Z: TetrisBlock(
                block_id=BlockId.Z,
                matrix = np.array([
                    [1, 1, 0],
                    [0, 1, 1],
                ]),
            ),
            BlockId.S: TetrisBlock(
                block_id=BlockId.S,
                matrix = np.array([
                    [0, 1, 1],
                    [1, 1, 0],
                ]),
            ),
            BlockId.T: TetrisBlock(
                block_id=BlockId.T,
                matrix = np.array([
                    [1, 1, 1],
                    [0, 1, 0],
                ]),
            ),
            BlockId.I: TetrisBlock(
                block_id=BlockId.I,
                matrix = np.array([
                    [1, 1, 1, 1],
                ]),
            ),
            BlockId.L: TetrisBlock(
                block_id=BlockId.L,
                matrix = np.array([
                    [1, 0],
                    [1, 0],
                    [1, 0],
                    [1, 1],
                ]),
            ),
            BlockId.J: TetrisBlock(
                block_id=BlockId.J,
                matrix = np.array([
                    [0, 1],
                    [0, 1],
                    [0, 1],
                    [1, 1],
                ]),
            ),
        }

        return blocks[blockId]
