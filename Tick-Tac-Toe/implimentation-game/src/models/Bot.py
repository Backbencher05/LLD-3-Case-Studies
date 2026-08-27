# - Bot will have 
# - in bot also we need all the thinks player have
# - so Botshould inherit Player 

# bot also have difficulty 

from src.models.players import Player
from src.models.PlayerType import PlayerType

class Bot(Player):
    
    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        self.difficulty = difficulty # will get it from user , for now let's sympity store it
        # type: will get from enum values we already have , so let's go for player type 
    
    # let's go for symbol
