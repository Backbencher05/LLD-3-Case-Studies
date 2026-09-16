from src.CustomExceptions.InvalidPlayerException import InvalidPlayerException
from src.models.Game import Game

class GameBuilder:
    def __init__(self):
        self.dimention = None
        self.players = None
        self.winning_strategies = None

    # we can created satter methods 
    def set_dimention(self, dimention):
        self.dimention = dimention
        return self

    def set_player(self, players):
        self.players = players
        return self

    def set_winning_strategy(self, winning_strategy):
        self.winning_strategies = self.winning_strategies
        return self


    # To create the object of Game class , we need to Build() methods as well 
    # Also on the top of that before building the game / before creating the object of the game 
    # we need to validate 

    def validate(self):
        if len(self.players) > self.dimention - 1:
            raise InvalidPlayerException() # this type of exception ot exist in our systerm  so let's create custom Exception 


    def build(self):
        self.validate()
        # from src.models.Game import Game 
        return Game(self.dimention, self.players, self.winning_strategies)