# board will have , input we need
# - board size
# - we need cell, board contain , wee need matrics of cell , 

from src.models.Cell import Cell

class Board:
    # let's first initialize the board
    def __init__(self, board_size):
        self.board_size = board_size
        # let's go for cell class first
        # we created/initialize Cell
        # Now
        # when board will be initializing the cell , how they will initialize it, 
        # i.e once we have board size, how we will initialize the cell 
        # ans: with row and column, every cell will have unique row and column
        # but i have to iterate till board size
        self.grid = [[Cell(i,j) for j in range(board_size)] for i in range(board_size)]

        # now let's move ahead for player class 