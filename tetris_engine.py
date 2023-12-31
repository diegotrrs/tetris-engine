#!/usr/bin/env python3

import sys
from core.tetris_board import TetrisBoard

def process_line(
        line: str,
    ) -> int:    
        items = line.split(",")     

        tetris_board = TetrisBoard()

        for item in items:
            block_type = item[0]  # Assumption: Block ids are one character only
            col_idx = int(item[1:])  # Assumption: Positions are valid numbers

            block = tetris_board.find_block_type(block_type)
       
            if block:
                tetris_board.drop_block_at_column(
                    block,
                    col_idx,
                )
        print(tetris_board.height)

def main():
    for line in sys.stdin:
        # If line is not commented
        if line[0] != '#':
            process_line(line.strip())            

if __name__ == "__main__":
    main()
