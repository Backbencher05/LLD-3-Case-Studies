## 1:
 Board.py --> size , matrics of cell

we created board class 
as we want to store board size and matrics of cell 
so let's create cell class
##
class Board:
    def __init__(self, board_size):
        self.board_size = board_size
## 2:
 cell.py  --> row, column , initally player = None, initially cell status = Empty
we created cell class 
will have row , column , initially player will be None
initially we also need cell status (default status will be EMPTY)
so let's create cellStatus class ENUM

## 3:
 cellStatus.py --> ENUM --> empty, filled, block 

## 4:
let's back to the board class
board.py

we initiallised board size
now when board is initializing the cell , how they will initialize it
i.e once we have board_size how we will initialize a board

so ans is : with row and column as every cell have row and column but i have to iterate it till the size of board

class Board:
    # let's first initialize the board
    def __init__(self, board_size):
        self.board_size = board_size
        self.grid = [[Cell(i,j) for j in range(board_size)] for i in range(board_size)]



board : done
cell: done
now let's move toward player class
## 5:
 player.py 
initially it have -> name, id, type(BOT/HUMAN), symbol

class Player:
    # initially player will have 
    def __init__(self, name, id, type, symbol):
        self.name = name 
        self.id = id 
        self.type = type
        self.symbol = symbol


board : done
cell: done
player : done 
now let's move toward te bot 
## 6:
bot will also havename, id , type, symbol it also have "difficulty"
so bot should inherit player first

lass Bot(Player):
    
    def __init__(self, name, id, type, symbol, difficulty):
        super().__init__(name, id, PlayerType.BOT, symbol)
        self.difficulty = difficulty # will get it from user , for now let's sympity store it

here we have type i.e type of player so
let's create playerType enum



## 7
playerType.py --> ENUM : BUT / HUMAN

class PlayerType:
    HUMAN = "HUMAN"
    BOT = "BOT"


## 8:
botDifficulty.py : ENUM


class BotDifficulty:
    EASY = "EASY"
    HARD = "HARD"

## 9
symbol.py
we can put lot of things like colour and all 
# for now let take as integer


class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol

## 10 
now game.py

class Game:
    def __init__(self, dimension, players, winning_strategy):
        self.board = Board(dimension)
        self.players = players
        self.winning_strategy = winning_strategy
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.INPROGRESS

## 11
gameStatus.py : ENUM --> Inprogress, completed, draw



now our model(cook is ready have ingreedients) is ready 
now we need controller (waiter)

