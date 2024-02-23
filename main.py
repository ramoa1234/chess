import pygame
import test

pygame.init()

piece = test.Piece(None, None, None, None, None)
board = test.Board((None, None, None, None))
whitepawn = test.Pawn('white', 1 , 1)
screen = test.screen

running = True
while(running):
    board.drawBoard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    board.drawBoard()   
    whitepawn.draw(screen)
    pygame.display.update()
        
        

