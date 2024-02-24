import pygame

pygame.init()
white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)

pygame.display.set_caption('chess')
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
screen.fill(white)
#setboard(display)
#for every square created teh x and y can be stored in list with coordinated and able to change color fo object

whitePawn = pygame.image.load('images/whitepawn.png')
blackPawn = pygame.image.load('images/blackpawn.png')


squareSize = (100, 100)
class Square():
    def __init__(self, x , y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * squareSize[0], self.y * squareSize[1], squareSize[0], squareSize[1]))

class Board():
    def __init__(self):
        self.chessBoard = [[None for x in range(8)]for y in range(8)]
        self.squareSize = (100, 100)
        self.screen = pygame.display.set_mode((800, 800))

    def boardSquare(self, x, y, color):
        square = Square(x, y, color)
        self.chessBoard[x][y] = square

    def draw(self, x, y, color):
        pygame.draw.rect(screen, color, pygame.Rect(x*self.squareSize[0], y*self.squareSize[1], self.squareSize[0], self.squareSize[1]))
    
    def drawBoard(self):
        for x in range(8):
            for y in range(8):
                color = white if (x + y) % 2 == 0 else black
                self.boardSquare(x , y, color)
                self.draw(x, y, color)
            pygame.display.update()
    
    
def selectPiece(Board):
    if(pygame.MOUSEBUTTONDOWN):
        rowSelected, columnSelected = pygame.mouse.get_pos()
        rowSelected, columnselected = rowSelected//100, columnSelected//100
        if(Board.chessBoard[rowSelected][columnSelected] != None):
            Board.square(rowSelected, columnSelected, red)
        pygame.display.update()




class Pawn():
    def __init__(self, x, y , color):
        self.x = x
        self.y = y
        self.color = color
        #self.validMoves = []
        self.image = whitePawn if self.color == white else blackPawn


    def draw(self, x, y, color):
        screen.blit(self.image, (self.x * squareSize[0], self.y * squareSize[1]))
    
    def validMoves(self):
        pass
    

