lines = open('day9_input.txt').readlines()

def sumExists(target, numRange):
    for i in range(len(numRange)):
        for j in range(i+1, len(numRange)):
            if int(numRange[i]) + int(numRange[j]) == int(target):
                return True
    return False

def getSumRange(target):
    for i in range(len(lines)):
        numberRange = [int(lines[i].strip())]
        for j in range(i+1, len(lines)):
            numberRange.append(int(lines[j].strip()))
            if sum(numberRange) == target:
                return numberRange
            if sum(numberRange) > target:
                break
    return numberRange

numberRange = []
for i in range(25):
    numberRange.append(lines[i].strip())

for i in range(25, len(lines)):
    if sumExists(lines[i].strip(), numberRange) == False:
        value = lines[i].strip()
        break
    del numberRange[0]
    numberRange.append(lines[i].strip())

print('Part 1:', value)

range = getSumRange(int(value))
print('Part 1:', min(range) + max(range))
