import pygame
pygame.init()

white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
height, width = 800, 600
gameDisplay = pygame.display.set_mode((height, width))   
squareSize = (height/8, width/8)


pygame.display.set_caption('chess')
gameDisplay.fill(white)

def setBoard(gameDisplay, squareSize, white, black):
    for row in range(8):
        for column in range(8):
            color =  black if(row + column) % 2 == 0 else white
            index = (row, column)
            pygame.draw.rect(gameDisplay, color, [row*squareSize[0], column*squareSize[1], squareSize[0], squareSize[1]])
    
    #format the grid
        

    
    
def pawn():
    d
    
    
    


def main(gameDisplay, setBoard):
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        setBoard(gameDisplay, squareSize, white, black)
        pygame.display.flip()
        
    pygame.quit()
    
main(gameDisplay, setBoard)
