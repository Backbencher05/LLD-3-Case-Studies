from src.helper.Strategy.winning import Winning


class DiagonalWS(Winning):

    def __init__(self):
        self.count1 = {}
        self.count2 = {}


    def check_winner(self, cell, board):
        row = cell.row
        col = cell.col
        symbol = cell.player.symbol

    #     |\ | |
    #   ---------
    #     | |\ |
    #   ----------
    #     | | | \

        if row == col:   # left diagonal
            if symbol not in self.count1:
                self.count1[symbol] = 0
            self.count1[symbol] += 1 

            if self.count1[symbol] == board.board_size:
                return True
  #     | | | /
    #   ---------
    #   | |/ |
    #   ----------
    #  /| | | 
        if row + col == board.board_size - 1:
            if symbol not in self.count2:
                self.count2[symbol] = 0
            self.count2[symbol] += 1

            if self.count2[symbol] == board.board_size:
                return True


    def undo_handle(self, cell, board):
        row = cell.row 
        col = cell.col
        symbol = cell.player.symbol 

        if row == col: 
            self.count1[symbol] -= 1 

        if row + col == board.board_size - 1:
            self.count2[symbol] -= 1

        