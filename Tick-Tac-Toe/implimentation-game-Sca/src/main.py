from src.controllers.GameController import GameController
from src.models.PlayerType import PlayerType
from src.models.players import Player
from src.models.Symbol import Symbol
from src.models.BotDifficulty import BotDifficulty
from src.models.Bot import Bot

# Input required from the user 
# - dimention 
# - Players 
# - winning Strategy 

if __name__ == '__main__':
    # in very begening we have a game controller 
    gc = GameController()

    # when we create the object of GameController does the game started ?
    # the game will be started when we call the start_game() method 

    # now will take input's from user 
    # right now hard coded , convert into CLI
    dimentions = 3

    # we need to created the player before starting the game , i.e before calling the start menthod in the controller 
    players = [

        Player("karan",1, PlayerType.Human, Symbol("x")),
        Bot("Mohit",2, PlayerType.BOT, Symbol("y"), BotDifficulty.EASY),

        # playerType as object
        # Player symbol as object
    ]

    winning_strg = []

    gc.start_game(dimentions, players, winning_strg) # at this time we can say game started , as here we are calling start_game() method


    # we need to pass the info. to the controller 
    # we are coming to the restorent by our own
    # waiter(GameController) is taking the order and pass it to cook(Service)