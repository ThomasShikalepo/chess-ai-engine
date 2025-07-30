from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.square = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')    # Add white pieces to board
        self._add_pieces('black')    # Add black pieces to board

    def cal_moves(self, piece, row, col):
       '''
        Calculates all the possible (valid) moves of a specific piece, on a specific position
       '''
       def knight_moves():
           #8 possible moves
           possible_moves = [
               (row-2, col+1),
               (row-1, col+2),
               (row+1, col+2),
               (row+2, col+1),
               (row+2, col-1),
               (row+1, col-2),
               (row-1, col-2),
               (row-2, col-1)
           ]

           for possible_moves in possible_moves:
               possible_moves_row, possible_moves_col = possible_moves

               if Square.in_range(possible_moves_row, possible_moves_col):
                   if self.square[possible_moves_row][possible_moves_col].isempty_or_rival(piece.color):
                       #create squares of the new move
                       initial = Square(row, col)
                       final = Square(possible_moves_row, possible_moves_col) # piece=piece
                       #move new move 
                       move = Move(initial, final)
                       #append new valid move
                       piece.add_move(move)

       if isinstance(piece, Pawn):
           pass
       
       elif isinstance(piece, Knight):
           knight_moves()
       
       elif isinstance(piece, Bishop):
           pass
       
       elif isinstance(piece, Queen):
           pass
       
       elif isinstance(piece, King):
           pass
       
       elif isinstance(piece, Rook):
           pass

    def _create(self):
        for row in range(ROWS):
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
        

