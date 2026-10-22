# cell will have

# - row and column
# - initially player will be None 
# - cell status: inital cell status will be : Empty

from src.models.CellStatus import CellStatus

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.player = None
        # let's go for cell status
        # initially cell status will be EMPTY
        self.status = CellStatus.EMPTY

        # let's go back to board

    def display(self):
        if self.status == CellStatus.EMPTY:
            print("| - |", end="")

        # if cell have value print that value 
        else:
            print(f"| {self.player.symbol.symbol} |", end="")