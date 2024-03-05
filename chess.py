import pygame

pygame.init()

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

pieces = [whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn,
            whiteRook, whiteKnight, whiteBishop, whiteQueen, whiteKing, whiteBishop, whiteKnight, whiteRook,
            blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn,
            blackRook, blackKnight, blackBishop, blackQueen, blackKing, blackBishop, blackKnight, blackRook]

whitePieces=[whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn,
            whiteRook, whiteKnight, whiteBishop, whiteQueen, whiteKing, whiteBishop, whiteKnight, whiteRook]
whiteLocations=[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
blackPieces=[blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn,
            blackRook, blackKnight, blackBishop, blackQueen, blackKing, blackBishop, blackKnight, blackRook]
blackLocations=[(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
white, black, grey = (255, 255, 255), (0, 0, 0), (36, 36, 36)
screen.fill(white)
squareSize = (100, 100)

def drawBoard():
    for x in range(8):
        for y in range(8):
            color = white if (x + y) % 2 == 0 else grey
            pygame.draw.rect(screen, color, (x * squareSize[0], y * squareSize[1], squareSize[0], squareSize[1]))


def drawPieces(whitePieces, whiteLocations, blackPieces, blackLocations, pieces):
    mouseClick = pygame.mouse.get_pressed()
    turnStep = 0

    for i in range(len(whitePieces)):
        piece = whitePieces[i]
        location = whiteLocations[i]
        screen.blit(piece, (location[0] * 100 + 22, location[1] * 100 + 30))
#update turnStep steps need to be corrected
#and need to figure out how to use i and j vairable in the turn steps
    while(turnStep >= 1):
        if(mouseClick == whiteLocations):
            #update to have whiteePiecseSelected
            pieceSelected = pieces[mouseClick[0]][mouseClick[1]]
            if(turnStep == 1):
                if(mouseClick == validMove):
                    piecesSelected = mouseClick
                    turnStep = 2


    for j in range(len(blackPieces)):
        piece = blackPieces[j]
        location = blackLocations[j]
        screen.blit(piece, (location[0] * 100 + 22, location[1] * 100 + 30))
    while(turnStep >= 2):
        pass

def validMove():
    pass


running = True
while running:
    screen.fill(white)
    drawBoard()
    drawPieces(whitePieces, whiteLocations, blackPieces, blackLocations)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

