from src.models.CellStatus import CellStatus

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.player = None
        self.status = CellStatus.EMPTY