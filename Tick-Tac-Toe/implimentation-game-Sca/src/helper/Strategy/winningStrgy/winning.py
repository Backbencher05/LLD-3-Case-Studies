from abc import ABC, abstractmethod


class Winning(ABC):

    @abstractmethod
    def check_winner(self, cell, board):
        pass 

    @abstractmethod
    def undo_handle(self, cell, board):
        pass


    # we are going to implement wiining by : diagonal winning
    # do it row wise and column wise  