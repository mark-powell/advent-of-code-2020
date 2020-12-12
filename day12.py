import math
lines = open('day12_input.txt').readlines()

actions = [l.strip() for l in lines]
     
def doAction(a, state):
    if a[0] == 'N':
        state[1] += int(a[1:])
    if a[0] == 'E':
        state[0] += int(a[1:])
    if a[0] == 'S':
        state[1] -= int(a[1:])
    if a[0] == 'W':
        state[0] -= int(a[1:])
    if a[0] == 'L':
        state[2] -= int(a[1:])
        if state[2] < 0:
            state[2] += 360
    if a[0] == 'R':
        state[2] += int(a[1:])
        if state[2] >= 360:
            state[2] -= 360
    if a[0] == 'F':
        if state[2] == 0:
            state = doAction('N' + a[1:], state)
        if state[2] == 90:
            state = doAction('E' + a[1:], state)
        if state[2] == 180:
            state = doAction('S' + a[1:], state)
        if state[2] == 270:
            state = doAction('W' + a[1:], state)
    return state

shipState = [0, 0, 90]
for a in actions:
    doAction(a, shipState)

print('Part 1:', abs(shipState[0]) + abs(shipState[1]))

def doAction2(a, state):
    if a[0] == 'N':
        state[3] += int(a[1:])
    if a[0] == 'E':
        state[2] += int(a[1:])
    if a[0] == 'S':
        state[3] -= int(a[1:])
    if a[0] == 'W':
        state[2] -= int(a[1:])
    if a[0] == 'L' or a[0] == 'R':
        degs = -int(a[1:]) if a[0] == 'R' else int(a[1:])
        rad = math.radians(degs)
        newX = round(math.cos(rad)*state[2], 4) - round(math.sin(rad)*state[3], 4)
        newY = round(math.sin(rad)*state[2], 4) + round(math.cos(rad)*state[3], 4)
        state[2] = int(newX)
        state[3] = int(newY)
    if a[0] == 'F':
        state[0] += state[2] * int(a[1:])
        state[1] += state[3] * int(a[1:])
    return state

shipState = [0, 0, 10, 1]
for a in actions:
    doAction2(a, shipState)

print('Part 2:', abs(shipState[0]) + abs(shipState[1]))