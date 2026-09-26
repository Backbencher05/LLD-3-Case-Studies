from src.models.Game import Game
from src.models.CellStatus import CellStatus


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
        current_player = game.players[game.next_turn]
        cell = current_player.decide_cell() # user selected the cell
        cell.player = current_player # store who played the turn
        cell.status = CellStatus.FILLED # cell status moved from EMPTY to FILLED
        game.moves.append(cell)  # add all the values to stack so that we can perform UNDO if required

        # now we will check for the winner 

    def check_winner(self, game, board, cell):
        pass
        # for checking winner we will have different strategies 
        # so let
        # s first create different strategies (we are going to use strategy design patterns)