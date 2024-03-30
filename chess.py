import pygame

pygame.init()

whitePawn = pygame.image.load('images/whitepawn.png')
blackPawn = pygame.image.load('images/blackpawn.png')
whiteRook = pygame.image.load('images/whiterook.png')
blackRook = pygame.image.load('images/blackrook.png')
whiteKnight = pygame.image.load('images/whitehorse.png')
blackKnight = pygame.image.load('images/chess.png')
whiteBishop = pygame.image.load('images/whitebishop.png')
blackBishop = pygame.image.load('images/blackpawn.png')
whiteQueen = pygame.image.load('images/whitequeen.png')
blackQueen = pygame.image.load('images/blackqueen.png')
whiteKing = pygame.image.load('images/whiteking.png')
blackKing = pygame.image.load('images/blackking.png')

pieces = [whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn,
            whiteRook, whiteKnight, whiteBishop, whiteQueen, whiteKing, whiteBishop, whiteKnight, whiteRook,
            blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn,
            blackRook, blackKnight, blackBishop, blackQueen, blackKing, blackBishop, blackKnight, blackRook]
piecesLocation = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]

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
    for i in range(len(whitePieces)):
        piece = whitePieces[i]
        location = whiteLocations[i]
        screen.blit(piece, (location[0] * 100 + 22, location[1] * 100 + 30))

    for j in range(len(blackPieces)):
        piece = blackPieces[j]
        location = blackLocations[j]
        screen.blit(piece, (location[0] * 100 + 22, location[1] * 100 + 30))

validWhiteMoves = []
validBlackMoves = []

def validMove():
    validWhiteMoves.clear()
    for i, piece in enumerate(whitePieces):
        location = whiteLocations[i]
        if(whitePieces[i] == whitePawn):
            pawnMoves = checkPawn('white', location)
            validWhiteMoves.append(pawnMoves)
        if(whitePieces[i] == whiteRook):
            rookMoves = checkRook('white', location)
            validWhiteMoves.append(rookMoves)
        if(whitePieces[i] == whiteKnight):
            knightMoves = checkKnight(location)
            validWhiteMoves.append(knightMoves)
        if(whitePieces[i] == whiteBishop):
            bishopMoves = checkBishop(location)
            validWhiteMoves.append(bishopMoves)
        if(whitePieces[i] == whiteQueen):
            #queenMoves = checkQueen(location)
            #validWhiteMoves.append(queenMoves)
            pass
        if(whitePieces[i] == whiteKing):
            #kingMoves = checkKing(location)
            #validWhiteMoves.append(kingMoves)
            pass
    
    for i, piece in enumerate(blackPieces):
        location = blackLocations[i]
        if(blackPieces[i] == blackPawn):
            pawnMoves = checkPawn('black', location)
            validBlackMoves.append(pawnMoves)
        if(blackPieces[i] == blackRook):
            rookMoves = checkRook('black',location)
            validBlackMoves.append(rookMoves)
        if(blackPieces[i] == blackKnight):
            knightMoves = checkKnight(location)
            validBlackMoves.append(knightMoves)
        if(blackPieces[i] == blackBishop):
            bishopMoves = checkBishop(location)
            validBlackMoves.append(bishopMoves)
        if(blackPieces[i] == blackQueen):
            queenMoves = checkQueen(location)
            validBlackMoves.append(queenMoves)
            pass
        if(blackPieces[i] == blackKing):
            kingMoves = checkKing(location)
            validBlackMoves.append(kingMoves)
            pass

def checkPawn(color, location):
    #need to make black moves
    moves = []
    x, y = location
    if(color == 'white'):
        if(y == 1):
            moves.extend([(x, y + 1),(x, y + 2)])
        elif(y + 1 in (whiteLocations or blackLocations)):
            return moves
        elif((x + 1, y + 1) in blackLocations):
            moves.extend([(x + 1, y + 1)])
        elif((x - 1, y + 1) in blackLocations):
            moves.extend([x - 1, y + 1])
        else:
            moves.append((x, y + 1))
    else:
            if(y == 6):
                moves.extend([(x, y - 1),(x, y - 2)])
            elif(y - 1 in (whiteLocations or blackLocations)):
                return moves
            elif((x + 1, y - 1) in whiteLocations):
                moves.extend([(x + 1, y - 1)])
            elif((x - 1, y - 1) in whiteLocations):
                moves.extend([x - 1, y - 1])
            else:
                moves.append([(x, y - 1)])
    return moves

def checkRook(color, location):
    moves = []
    x, y = location
    #need to make if black or white conditions
    for i in range(8):
        if((x, i) in whiteLocations and color == 'white'):
            break
        elif((x, i) in blackLocations and color == 'white'):
            moves.append((x, i))
            break
        else:moves.append((x, i))
    for j in range(8):
        if((i , j) in whiteLocations and color == 'white'):
            break
        elif((i , j) in blackLocations and color == 'white'):
            moves.append((i, y))
            break
        else:moves.append((i, y))
    return moves

def checkKnight(location):
    moves = []
    x, y = location
    moves.extend([(x + 1, y + 2)])
    moves.extend([(x + 1, y - 2)])
    moves.extend([(x - 1, y + 2)])
    moves.extend([(x - 1, y - 2)])
    moves.extend([(x + 2, y + 1)])
    moves.extend([(x + 2, y - 1)])
    moves.extend([(x - 2, y + 1)])
    moves.extend([(x - 2, y - 1)])
    return moves

def checkBishop(location):
    moves = []
    x, y = location
            #need to make it so that the loop also ends if a piece in way
    for i in range(8):
        for j in range(8):
            if(x == 8 or y == 8):
                break
            moves.extend((x + 1, y + 1))
    for i in range(8):
        for j in range(8):
            if(x == 8 or y == 0):
                break
            moves.extend((x + 1, y - 1))
    for i in range(8):
        for j in range(8):
            if(x == 0 or y == 8):
                break
            moves.extend((x - 1, y + 1))
    for i in range(8):
        for j in range(8):
            if(x == 0 or y == 0):
                break
            moves.extend((x - 1, y - 1))
    return(moves)

def checkQueen(location):
    moves = []
    x, y = location
    moves.extend([(x + 1, y)])
    moves.extend([(x + 1, y + 1)])
    moves.extend([(x, y + 1)])
    moves.extend([(x - 1, y + 1)])
    moves.extend([(x - 1, y)])
    moves.extend([(x - 1, y - 1)])
    moves.extend([(x, y - 1)])
    moves.extend([(x + 1, y - 1)])
    return moves
    
def checkKing(location):
    moves = []
    x, y = location
    moves.extend([(x + 1, y)])
    moves.extend([(x + 1, y + 1)])
    moves.extend([(x, y + 1)])
    moves.extend([(x - 1, y + 1)])
    moves.extend([(x - 1, y)])
    moves.extend([(x - 1, y - 1)])
    moves.extend([(x, y - 1)])
    moves.extend([(x + 1, y - 1)])

    for i in range(8):
        for j in range(8):
            if(x == 8 or y == 8):
                break
            moves.extend((x + 1, y + 1))
    for i in range(8):
        for j in range(8):
            if(x == 8 or y == 0):
                break
            moves.extend((x + 1, y - 1))
    for i in range(8):
        for j in range(8):
            if(x == 0 or y == 8):
                break
            moves.extend((x - 1, y + 1))
    for i in range(8):
        for j in range(8):
            if(x == 0 or y == 0):
                break
            moves.extend((x - 1, y - 1))
    return moves


validMove()
turnStep = 0
running = True
while running:
    screen.fill(white)
    drawBoard()
    drawPieces(whitePieces, whiteLocations, blackPieces, blackLocations, pieces)
    validMove()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            click_coords = (event.pos[0] //100, event.pos[1] //100)
            if(turnStep == 0):
                if(click_coords in whiteLocations):
                    selected = whiteLocations.index(click_coords)
                    turnStep = 1
            elif(turnStep == 1):
                removed = 0
                if(click_coords in whiteLocations):
                    selected = whiteLocations.index(click_coords)
                if selected is not None and selected < len(validWhiteMoves):
                    if(click_coords in validWhiteMoves[selected]):
                        if(click_coords in blackLocations):
                            blackLocations.remove(click_coords)
                            for i in range(len(blackLocations)):
                                if(click_coords == blackLocations[i]):
                                    removed = i
                            del blackPieces[removed]
                        whiteLocations[selected] = click_coords
                        drawPieces(whitePieces, whiteLocations, blackPieces, blackLocations, pieces)
                        turnStep = 2
            
            elif(turnStep == 2):
                if(click_coords in blackLocations):
                    selected = blackLocations.index(click_coords)
                    turnStep = 3
            elif(turnStep == 3):
                if(click_coords in blackLocations):
                    selected = blackLocations.index(click_coords)
                if selected is not None and selected < len(validBlackMoves):
                    if(click_coords in validBlackMoves[selected]):
                        if(click_coords in whiteLocations):
                                whiteLocations.remove(click_coords)
                                for i in range(len(whiteLocations)):
                                    if(click_coords == whiteLocations[i]):
                                        removed = i
                                del whitePieces[removed]
                        blackLocations[selected] = click_coords
                        drawPieces(whitePieces, whiteLocations, blackPieces, blackLocations, pieces)
                        turnStep = 0


