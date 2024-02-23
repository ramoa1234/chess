import pygame
pygame.init()


pygame.display.set_caption('chess')
width, height = 800, 800
white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
screen = pygame.display.set_mode((width, height))
screen.fill(white)
squareSize = (width/8, height/8)
#setboard(display)
#for every square created teh x and y can be stored in list with coordinated and able to change color fo object

whitePawn = pygame.image.load('whitepawn.png')
blackPawn = pygame.image.load('blackpawn.png')

chessBoard = ''





class Board():
    def __init__(self, row, column, color, isSelected):
        self.row = row
        self.column = column
        self.color = color
        self.isSelected = False 
        
    def drawBoard(self):
        chessBoard = [['' for i in range(8)] for j in range(8)]
        for x in range(8):
            for y in range(8):               
                color = white if (x + y) % 2 == 0 else black
                pygame.draw.rect(screen, color, (x * squareSize[0], y * squareSize[1], squareSize[0], squareSize[1]))
                
    def isSelectd(self, isClicked, row, column,):
        pass    
        #nned to make mouse click event
        
        
class Piece:
    def __init__(self,color, row, column, image, validMoves):
        self.color = color
        self.row = row
        self.column = column
        self.image = image
        self.validMoves = validMoves
            
    #draw can be called everytime a move is made to update chess list and also were the piece is drawn

    def draw(self, row, column, image):
        if self.color == 'white':
            self.image = whitePawn
        else:
            self.image = blackPawn
        
        x = self.column * squareSize[0] + squareSize[0]  // 2
        y = self.row * squareSize[1] + squareSize[1]  // 2
        screen.blit(self.image, (x - squareSize[0] // 2, y - squareSize[1] // 2))


class Pawn(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)


       
    
