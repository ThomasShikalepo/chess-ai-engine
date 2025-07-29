from const import *
from square import Square

class Board:
    def __init__(self):
        self.square = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create()

    def _create(self):
        for row in range(Rows):
            for col in range(COLS):
                self.square[row][col] = Square(row,col)


    def _add_pieces(self, color):
        pass