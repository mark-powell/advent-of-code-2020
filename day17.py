import copy
lines = open('day17_input.txt').readlines()

board = {}
def setLoc(x, y, z, value, board):
    board[str(x) + ',' + str(y) + ',' + str(z)] = value
def getLoc(x, y, z, board):
    key = str(x) + ',' + str(y) + ',' + str(z)
    if key in board:
        return board[key]
    return '.'

def getNeighbours(xPos, yPos, zPos, board):
    surroundingLocs = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if x != 1 or y != 1 or z != 1:
                    surroundingLocs.append(getLoc(xPos+x-1,yPos+y-1,zPos+z-1,board))
    return surroundingLocs

def cycleBoard():
    newState = copy.deepcopy(board)
    for x in range(-25,25):
        for y in range(-25,25):
            for z in range(-6,6):
                surroundingLocs = getNeighbours(x,y,z, board)
                if getLoc(x,y,z, board) == '#' and (surroundingLocs.count('#') != 2 and surroundingLocs.count('#') != 3):
                    setLoc(x,y,z,'.', newState)
                if getLoc(x,y,z, board) == '.' and (surroundingLocs.count('#') == 3):
                    setLoc(x,y,z,'#', newState)
    return newState

for l in range(len(lines)):
    row = lines[l].strip()
    for r in range(len(row)):
        setLoc(r, l, 0, row[r], board)

for i in range(6):
    board = cycleBoard()
count = 0
for r in board:
    if board[r] == '#':
        count += 1

print('Part 1:', count)

board = {}

def setLoc2(x, y, z, w, value, board):
    board[str(x) + ',' + str(y) + ',' + str(z) + ',' + str(w)] = value
def getLoc2(x, y, z, w, board):
    key = str(x) + ',' + str(y) + ',' + str(z) + ',' + str(w)
    if key in board:
        return board[key]
    return '.'

def getNeighbours2(xPos, yPos, zPos, wPos, board):
    surroundingLocs = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for w in range(3):
                    if x != 1 or y != 1 or z != 1 or w != 1:
                        surroundingLocs.append(getLoc2(xPos+x-1,yPos+y-1,zPos+z-1,wPos+w-1,board))
    return surroundingLocs

def cycleBoard2():
    newState = copy.deepcopy(board)
    for x in range(-25,25):
        for y in range(-25,25):
            for z in range(-25,25):
                for w in range(-25,25):
                    surroundingLocs = getNeighbours2(x,y,z,w, board)
                    if getLoc2(x,y,z,w, board) == '#' and (surroundingLocs.count('#') != 2 and surroundingLocs.count('#') != 3):
                        setLoc2(x,y,z,w,'.', newState)
                    if getLoc2(x,y,z,w, board) == '.' and (surroundingLocs.count('#') == 3):
                        setLoc2(x,y,z,w,'#', newState)
    return newState

for l in range(len(lines)):
    row = lines[l].strip()
    for r in range(len(row)):
        setLoc2(r, l, 0, 0, row[r], board)

for i in range(6):
    board = cycleBoard2()
count = 0
for r in board:
    if board[r] == '#':
        count += 1

print('Part 2:', count)