# board will have , input we need
# - board size
# - we need cell, board contain , wee need matrics of cell , 

from src.models.Cell import Cell

class Board:
    # let's first initialize the board
    def __init__(self, board_size):
        self.board_size = board_size
        # let's go for cell class first
        self.grid = [[Cell(i,j) for j in range(board_size)] for i in range(board_size)]

        # now let's move ahead for player class 