import unittest

import numpy as np
from core import tetris_block
from core.tetris_block_factory import TetrisBlockFactory
from core.tetris_board import TetrisBoard


# fmt: off

# Include tests for drop_block_at_board when it does not result in new top rows added.
class TestDropBlockAtBoardNoTopRowsAdded(unittest.TestCase):

    def test_drop_block_at_board_at_column_0(
        self,
    ):
        board = np.array(
            [
                [ 0, 0, 1, 0 ],
                [ 0, 0, 1, 0 ],
                [ 1, 1, 1, 0 ],
                [ 1, 1, 1, 0 ],
            ]
        )

        tetris_board = TetrisBoard()
        tetris_board.board = board

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.Q), 0)
        
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            4
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T), 1)

        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [
                        [ 0, 1, 1, 1 ],
                        [ 0, 0, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            6
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.I), 1)


        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [                        
                        [ 0, 1, 1, 1 ],
                        [ 0, 0, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            6
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.X), 0)


        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        [ 0, 1, 0, 0 ],                  
                        [ 1, 1, 0, 0 ],                       
                        [ 0, 0, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            7
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.T), 10) # test out of range 

        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        [ 0, 1, 1, 1 ],                        
                        [ 0, 1, 1, 0 ],                  
                        [ 1, 1, 0, 0 ],                       
                        [ 0, 0, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            8
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.Y), 0)
   
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        
                        [ 1, 0, 0, 0 ],  
                        [ 1, 0, 0, 0 ],                                                
                        [ 1, 1, 1, 0 ],                  
                        [ 1, 1, 0, 0 ],                       
                        [ 0, 0, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                        [ 1, 1, 1, 0 ],
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            9
        )


        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.Y), 3)
   
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        
                        [ 1, 0, 0, 0 ],  
                        [ 1, 0, 0, 0 ],  
                        [ 1, 1, 1, 0 ],                  
                        [ 1, 1, 0, 0 ],                       
                        [ 0, 0, 1, 0 ],                        
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            5
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.Q), 1)
   
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   
                        
                        [ 1, 1, 1, 0 ],  
                        [ 1, 1, 1, 0 ],  
                        [ 1, 1, 1, 0 ],                  
                        [ 1, 1, 0, 0 ],                       
                        [ 0, 0, 1, 0 ],                        
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            5
        )

        height = tetris_board.drop_block_at_column(TetrisBlockFactory.create_tetris_block(tetris_block.BlockId.Y), 3)
   
        self.assertTrue(
            np.array_equal(
                tetris_board.board,
                np.array(
                    [   [ 1, 1, 1, 0 ],
                        [ 1, 1, 0, 1 ],                       
                        [ 0, 0, 1, 1 ],                       
                    ]
                ),
            )
        )

        self.assertEqual(
            height,
            3
        )
  
    

if __name__ == "__main__":
    unittest.main()
# fmt: on
