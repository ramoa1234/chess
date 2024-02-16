import pygame
pygame.init()

pygame.display.set_caption('chess')
width, height = 800, 800
white, black = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((width, height))
screen.fill(white)
squareSize = (width/8, height/8)

blackPawn = pygame.image.load('blackpawn.png')


chessBoard  = [['' for _ in range(8)] for  _ in range(8)]
#@chessBoard[2][1] = 



    

class Piece:
    def __init__(self, iamge, position  ):
        self.iamge = iamge
        self.position = position    
        
    def centerPiece():
        pass
    
    def drawPiece():
        pass
    
    def pieceSelected():
        pass
    
    
    
    
def pawn(piece):
    pass

#setboard(display)
def drawBoard(screen, white, black, squareSize):
    for row in range(8):
        for column in range(8):
            color = black if(row + column) % 2 == 0 else white
            pygame.draw.rect(screen, color, (column * squareSize[0], row * squareSize[1], squareSize[0], squareSize[1]))

def main():
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawBoard(screen, white, black,squareSize)
        pygame.display.flip()

main()
