# - Bot will have 
# - in bot also we need all the thinks player have
# - so Bot should inherit Player 
# bot also have difficulty 

from src.models.players import Player
from src.models.PlayerType import PlayerType

class Bot(Player):
    
    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        # type: will get from enum values we already have , so let's go for player type 
        self.difficulty = difficulty # will get it from user , for now let's sympity store it

    # let's go for symbol

    def decide_cell(self, board):
        pass