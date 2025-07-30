from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.square = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')    # Add white pieces to board
        self._add_pieces('black')    # Add black pieces to board

    def _create(self):
        for row in range(Rows):
            for col in range(COLS):
                self.square[row][col] = Square(row,col)


    def _add_pieces(self, color):
        
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)

        #Add pawns
        for col in range(COLS):
            self.square[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        #Add knights
        self.square[row_other][1] = Square(row_other, 1, Knight(color))
        self.square[row_other][6] = Square(row_other, 6, Knight(color))

        #Add bishop
        self.square[row_other][2] = Square(row_other, 2, Bishop(color))
        self.square[row_other][5] = Square(row_other, 5, Bishop(color))

        #Add rook
        self.square[row_other][0] = Square(row_other, 0, Rook(color))
        self.square[row_other][7] = Square(row_other, 7, Rook(color))

        #Add queen
        self.square[row_other][3] = Square(row_other, 3, Queen(color))
        

        #Add king
        self.square[row_other][4] = Square(row_other, 4, King(color))
        

