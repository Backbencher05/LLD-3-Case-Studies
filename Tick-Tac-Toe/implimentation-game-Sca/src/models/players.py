# player will have
# - name, 
# - id , 
# - type,
# - symbol

class Player:
    # initially player will have 
    def __init__(self, name, id, type, symbol):
        self.name = name 
        self.id = id 
        self.type = type
        self.symbol = symbol

    # let's move to bot 

    def decide_cell(self, board):
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if 0 <= row < board.board_size and 0 <= col < board.board_size:
                if board.grid[row][col].status == "EMPTY": # means it's a correct move
                    return board.grid[row][col]

            # other wise invalid move 
            # we are not throwing the error , i am asking the user to retry
            print("Invalid row or column or cell is filled")
        