import pygame

import functions

pygame.init()


Board = functions.Board()
player1 = functions.player('white')
player2 = functions.player('black')


running = True
while(running):
    Board.drawBoard()
    player1.draw()
    player2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()
pygame.quit()
    
