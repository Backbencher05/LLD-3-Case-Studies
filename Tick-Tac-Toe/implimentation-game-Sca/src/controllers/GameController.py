# Now if we start implimenting the feature the first things we required after 
# "models" is --> "controller"(wiater) pass the info taken by user / input to the service (cook) 

# we need to think like

# - what are the things we have in game controller
# - what are the functionality we need to implement
# - what are the inputs, user intracting with 

# once every 
# think about it, we are going to play tic-tac-toe, what is the first button you are going to press, when everyone join the room 
 
# we are taking about once you selected everythink, now you are intracting with game think on that percepective 

# chossing symbol and all will happen in main class , prior to the game start , this is game controller 


# let we start the game

""" 
- status move to in progress once game start 
IN loop 
- display the board
- player make some move on board
- once player make the move , check for winer ..on every move
- if no winner OR not all cell filled:
    - change next player index (controller goes to next player)
    - other player chance
"""


# game controller is not a main file , it is controlling the game part only 
class GameController:

    def __init__(self, gameService):
        self.gameService = gameService

    def start_game(self, size, players, winning_stg):
        # validations if we have any 
        self.gameService.start_game(size, players, winning_stg)

    def display_board(self, game):
        self.gameService.display_game(game)

    def take_move(self, game):
        self.gameService.take_move(game)

    def undo_move(self, game):
        self.gameService.undo(game)


# now all the logic goes to service and repo layer 
# which service take the controller data i.e which cook takes the order (data)