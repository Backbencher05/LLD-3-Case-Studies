from src.models.Game import Game
from src.models.CellStatus import CellStatus
from src.models.GameStatus import GameStatus

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

        # now let's implement winning strategies
        # now, after every move we need to check winner 
        if self.check_winner(game, cell):
            # if someone wonn, update the game status 
            game.gameStatus = GameStatus.COMPLETED
            # declear the winner 
            game.winner = current_player

        # if no one won and all the all the moves are played means: DRAW
        # how we check ?
        # we already hjave moves in our stack and we know the size of board
        elif len(game.moves) == game.Board.board_size * game.Board.board_size:
            game.gameStatus = GameStatus.DRAW

        # if no one won or game not drawn give turn to next player 
        game.next_turn += 1
        game.next_turn %= len(game.players) # lenght should not be inclease

        
        # now we will check for the winner 
    def check_winner(self, game, cell):
        pass
        # for checking winner we will have different strategies 
        # so let
        # s first create different strategies (we are going to use strategy design patterns)

        return any(ws.check_winner(game.board, cell) for ws in game.winning_stratergies)


    def undo(self, game):
        if not game.moves:
            print("No moves left to undo") 
            return

        cell = game.moves.pop()

        for ws in game.winning_stratergies:
            ws.undo_handle(cell, game.board)

        cell.status = CellStatus.EMPTY
        cell.player = None

        game.next_turn -= 1
        game.next_turn %= len(game.players)