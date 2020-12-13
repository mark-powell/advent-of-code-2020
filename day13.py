import math
lines = open('day13_input.txt').readlines()

time = int(lines[0])
busIds = [int(id) for id in lines[1].split(',') if id.isnumeric()]

def doesBusDepart(timeStamp):
    for id in busIds:
        if timeStamp % id == 0:
            return id
    return 0

loopTime = time
busId = 0
while busId == 0:
    loopTime += 1
    busId = doesBusDepart(loopTime)

print('Part 1:', (loopTime - time) * busId)

busIndexs = [lines[1].split(',').index(str(id)) for id in busIds]
step = busIds[0]
time = 0
for index in range(len(busIds)):
    offset = 0
    while True:
        if (time + busIndexs[index]) % busIds[index] == 0:
            if offset == 0:
                offset = time
            else:
                step = time - offset
                break
        time += step

print('Part 2:', offset)
