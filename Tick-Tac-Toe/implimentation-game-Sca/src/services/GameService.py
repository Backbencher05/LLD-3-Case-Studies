from src.models.Game import Game

class GameService: 

    def start_game(self, size, players, winning_stg):
        # GBuilder = Game.gameBuilder()
        # GBuilder.set_player()
        # GBuilder.set_winning_strategy()
        # GBuilder.set_dimention()

        # to solve this chaining problem, as we are using same object again and again 
        # we can return directly self from these methods 
        # so go to these builder method and directly return the self 

        game = Game.gameBuilder().set_player().set_dimention().set_winning_strategy()
        game.build()
        # now we got the game object 

    def display_board(self, game):
        game.Board.print_board()


    def take_move(self, game):
         pass