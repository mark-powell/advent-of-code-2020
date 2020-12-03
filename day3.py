lines = open('day3_input.txt').readlines()

mapHeight = len(lines)
mapWidth = len(lines[0])-1

def hasTreeAt(x, y):
    actualX = x if x < mapWidth else x % mapWidth
    return lines[y][actualX:actualX+1] == '#'

def getTreeHits(xVel, yVel):
    treeCount = 0
    xPos = 0
    for yPos in range(0, mapHeight, yVel):
        if hasTreeAt(xPos, yPos):
            treeCount += 1
        xPos += xVel
    return treeCount

part1result = getTreeHits(3, 1)
test1 = getTreeHits(1, 1)
test2 = getTreeHits(5, 1)
test3 = getTreeHits(7, 1)
test4 = getTreeHits(1, 2)

part2result = part1result*test1*test2*test3*test4

print('Part 1:', part1result)
print('Part 2:', part2result)
