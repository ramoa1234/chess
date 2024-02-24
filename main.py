import pygame

import functions

pygame.init()


white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
Board = functions.Board()


running = True
while(running):
    Board.drawBoard()
    for i in range(8):
        for i in range(8):
            pawn_white = functions.Pawn(1, i, white)
            pawn_white.draw(1, i, white)
            Board.chessBoard[1][i] = pawn_white

            pawn_black = functions.Pawn(6, i, black)
            pawn_black.draw(6, i, black)
            Board.chessBoard[6][i] = pawn_black
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()
pygame.quit()
