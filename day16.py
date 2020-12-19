lines = open('day16_input.txt').readlines()
validation = {}
for lineCount in range(len(lines)):
    line = lines[lineCount].strip()
    if len(line) == 0:
        break
    parts = line.strip().split(':')
    key = parts[0]
    values = [p.strip() for p in parts[1].split(' or ')]
    lineCount += 1
    validation[key] = [v.split('-') for v in values]

def checkValue(value, validation):
    for vp in range(len(validation)):
        if value >= int(validation[vp][0]) and value <= int(validation[vp][1]):
            return True
    return False
        
def validateTicket(line):
    for l in line.split(','):
        passed = False
        for v in validation:
            passed = checkValue(int(l),validation[v]) or passed
        if passed == False:
            return int(l)
    return 0

def findLineNumber(searchString):
    for l in range(len(lines)):
        line = lines[l].strip()
        if searchString == line:
            return l

count = 0
for l in range(findLineNumber('nearby tickets:')+1, len(lines)):
    count += validateTicket(lines[l])

print('Part 1:', count)

validTickets = []
for l in range(findLineNumber('nearby tickets:')+1, len(lines)):
    if validateTicket(lines[l]) == 0:
        validTickets.append(lines[l].strip())

myTicket = lines[findLineNumber('your ticket:')+1].strip()
validTickets.append(myTicket)

def validateTicketIndex(index, validationKey):
    for t in validTickets:
        if checkValue(int(t.split(',')[index]), validation[validationKey]) == False:
            return False
    return True

fieldIndex = {}
fieldCount = len(validTickets[0].split(','))
for i in range(fieldCount):
    fieldIndex[i] = []
for v in validation:
    for i in range(fieldCount):
        if validateTicketIndex(i, v):
            fieldIndex[i].append(v)

foundIndexes = []
for i in range(fieldCount):
    for fi in fieldIndex:
        if len(fieldIndex[fi]) == i+1:
            for v in range(len(foundIndexes)):
                fieldIndex[fi].remove(foundIndexes[v])
            foundIndexes.append(fieldIndex[fi][0])

count = 1
for fi in fieldIndex:
    if fieldIndex[fi][0].startswith('departure'):
        count *= int(myTicket.split(',')[fi])

print('Part 2:', count)