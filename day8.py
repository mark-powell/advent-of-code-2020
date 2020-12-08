lines = open('day8_input.txt').readlines()
value = 0
executedLines = []
running = True
currentLine = 0
while running:
    if currentLine in executedLines:
        running = False
        break
    executedLines.append(currentLine)
    operation = lines[currentLine].strip().split(' ')[0]
    qty = int(lines[currentLine].strip().split(' ')[1])
    if operation == 'acc':
        value += qty
        currentLine += 1
    elif operation == 'jmp':
        currentLine += qty
    elif operation == 'nop':
        currentLine += 1

print('Part 1:', value)

for lineNum in range(len(lines)):
    value = 0
    executedLines = []
    running = True
    currentLine = 0
    while running:
        if currentLine in executedLines:
            value = -1
            running = False
            break
        if currentLine == len(lines):
            running = False
            break
        executedLines.append(currentLine)
        operation = lines[currentLine].strip().split(' ')[0]
        if(currentLine == lineNum):
            if operation == 'nop':
                operation = 'jmp'
            elif operation == 'jmp':
                operation = 'nop'
        qty = int(lines[currentLine].strip().split(' ')[1])
        if operation == 'acc':
            value += qty
            currentLine += 1
        elif operation == 'jmp':
            currentLine += qty
        elif operation == 'nop':
            currentLine += 1
    if value > 0:
        break

print('Part 2:', value)
