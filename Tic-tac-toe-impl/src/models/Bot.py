from src.models.players import Player
from src.models.PlayerType import PlayerType

class Bot(Player):

    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        