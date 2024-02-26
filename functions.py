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
whiteRook = pygame.image.load('images/whiterook.png')
blackRook = pygame.image.load('images/blackrook.png')
whiteKnight = pygame.image.load('images/whitehorse.png')
blackKnight = pygame.image.load('images/chess.png')
whiteBishop = pygame.image.load('images/whiterook.png')
blackBishop = pygame.image.load('images/blackrook.png')
whiteQueen = pygame.image.load('images/whitequeen.png')
blackQueen = pygame.image.load('images/blackqueen.png')
whiteKing = pygame.image.load('images/whiteking.png')
blackKing = pygame.image.load('images/blackking.png')



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
        rowSelected, columnSelected = rowSelected//100, columnSelected//100
        if(Board.chessBoard[rowSelected][columnSelected] != None):
            Board.square(rowSelected, columnSelected, red)
        pygame.display.update()

def eatPiece():
    pass


class Pawn():
    def __init__(self, x, y , color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []
        self.image = whitePawn if self.color == 'white' else blackPawn


    def draw(self):
        screen.blit(self.image, (self.x * squareSize[0], self.y * squareSize[1]))
    
    def validMoves(self):
        #need to add in logic so that pieces can move in two squares in first move
        #need to add logic so that pieces can move diagonally to eat
        if(self.color == 'white'):
            self.validMoves = [self.x + 1, self.y + 1]
        else:
            self.validMoves = [self.x - 1, self.y - 1]
            

    def becomeQueen(self):
        if(self.color == 'white'):
            if(self.y == 7):
                return Queen(self.x, self.y, self.color)
            elif(self.color == 'black'):
                if(self.y == 0):
                    return Queen(self.x, self.y, self.color)

class Queen():
    #need to find way to end game if a color pieces eaten
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []

        
        
    def validMoves(self):
        self.validMoves = [self.x + 1, self.y + 1, self.x + 1 & self.y + 1, self.x - 1, self.y - 1, self.x - 1 & self.y - 1]

        def draw(self):
            pass
        
class Rook():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []
    def validMoves(self):
        pass

class Bishop():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []
    def validMoves(self):
        pass

class King():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []
    def validMoves(self):
        pass

class Knight():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.validMoves = []
    def validMoves(self):
        pass


#player class can intiliaze and store the data needed for players
#instead of using classes in main and event loop

#might be better to just store in normal list

class player:
    def __init__(self, color):
        self.color = color
        self.pieces = []
        

    def  pieces(self):
        if(self.color == 'white'):
            return self.pieces [
                Pawn(1, 1, self.color),
                Pawn(1, 2, self.color),
                    
                ]
        
