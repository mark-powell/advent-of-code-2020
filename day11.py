import copy
lines = open('day11_input.txt').readlines()

rows = [l.strip() for l in lines]
seats = [list(s) for s in rows]
rowLength = len(lines[0].strip())
colLength = len(lines)

def getSeat(seats, xPos, yPos, xDir, yDir):
    if (xPos == 0 and xDir == -1) or (xPos == rowLength-1 and xDir == 1) or (yPos == 0 and yDir == -1) or (yPos == colLength-1 and yDir == 1):
        return 'x'
    return seats[yPos + yDir][xPos + xDir]

def getNextSeat(seats, xPos, yPos, xDir, yDir):
    seat = '.'
    while seat == '.':
        seat = getSeat(seats, xPos, yPos, xDir, yDir)
        xPos += xDir
        yPos += yDir
    return seat

def list_compare(a, b):
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c] != b[r][c]:
                return False
    return True

while True:
    newSeats = copy.deepcopy(seats)
    for r in range(colLength):
        for c in range(rowLength):
            surroundingSeats = []
            for i in range(3):
                for j in range(3):
                    if j != 1 or i != 1:
                        surroundingSeats.append(getSeat(seats,c,r,i-1,j-1))
            if seats[r][c] == 'L' and surroundingSeats.count('#') == 0:
                newSeats[r][c] = '#'
            if seats[r][c] == '#' and surroundingSeats.count('#') > 3:
                newSeats[r][c] = 'L'
    if list_compare(newSeats, seats):
        break
    seats = copy.deepcopy(newSeats)
    count = 0
    for r in range(len(seats)):
        count += seats[r].count('#')

print('Part 1:', count)

seats = [list(s) for s in rows]

while True:
    newSeats = copy.deepcopy(seats)
    for r in range(colLength):
        for c in range(rowLength):
            surroundingSeats = []
            for i in range(3):
                for j in range(3):
                    if j != 1 or i != 1:
                        surroundingSeats.append(getNextSeat(seats,c,r,i-1,j-1))
            if seats[r][c] == 'L' and surroundingSeats.count('#') == 0:
                newSeats[r][c] = '#'
            if seats[r][c] == '#' and surroundingSeats.count('#') > 4:
                newSeats[r][c] = 'L'
    if list_compare(newSeats, seats):
        break
    seats = copy.deepcopy(newSeats)
    count = 0
    for r in range(len(seats)):
        count += seats[r].count('#')

print('Part 2:', count)



