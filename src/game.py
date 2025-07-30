import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        
        #show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                
                else:
                    color = (119, 154, 88) # dark green

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                #is there a piece on that square
                 if self.board.square[row][col].has_piece():
                     piece = self.board.square[row][col].piece

                    #all pieces except dragger pieces
                     if piece is not  self.dragger.piece:
                        piece.set_texture()
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2 #center the img or piece
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)