# for initalizing the game, what all things we reqired for game from user
# 
# from use we reuired :
# 
# - board (dimentions of board)
# - list of players
# - winning strategy 
# - bot difficult (we can pass from player class , from main we we are setting the list of player we can pass it there)
# - moves (list of moves)
# - next player turn: initially let's start it from 0th index 
# - winner : initially winner will be : None
# - game status: initially game status will be: inprogress

from src.models.board import Board
from src.models.GameStatus import GameStatus
from src.helper.GameBuilder import GameBuilder


class Game:
    def __init__(self, dimension, players, winning_strategy):
        self.board = Board(dimension)
        self.players = players
        self.winning_strategy = winning_strategy
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.INPROGRESS


# now if we start implimeting the  feature , the things we required after model 
# - let first have main class 
# -
#  
    @staticmethod
    def gameBuilder():
        return GameBuilder()