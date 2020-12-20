lines = open('day18_input.txt').readlines()

def getBracketIndex(string):
    start = -1
    bracket = 0
    for i, c in enumerate(string):
        if c == '(':
            bracket += 1
            if start == -1:
                start = i
        if c == ')':
            bracket -= 1
            if bracket == 0:
                return start+1, i

def resolveSection(string, bracketStart, bracketEnd):
    subString = string[bracketStart:bracketEnd]
    return resolve(subString)

def resolve(string):
    if '(' in string:
        start, end = getBracketIndex(string)
        substring = resolveSection(string, start, end)
        newString = string[:start-1] + str(substring) + string[end+1:]
        return resolve(newString)
    parts = string.split(' ')
    count = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == '+':
            count += int(parts[i+1])
        if parts[i] == '*':
            count = count * int(parts[i+1])
    return count

count = 0
for l in lines:
    count += resolve(l.strip())

print('Part 1:', count)

def resolveSection2(string, bracketStart, bracketEnd):
    subString = string[bracketStart:bracketEnd]
    return resolve2(subString)

def resolve2(string):
    if '(' in string:
        start, end = getBracketIndex(string)
        substring = resolveSection2(string, start, end)
        newString = string[:start-1] + str(substring) + string[end+1:]
        return resolve2(newString)
    if '+' in string:
        parts = string.split(' ')
        for i in range(1, len(parts), 2):
            if parts[i] == '+':
                parts[i] = str(int(parts[i-1]) + int(parts[i+1]))
                del parts[i-1]
                del parts[i]
                return resolve2(' '.join(parts))
    parts = string.split(' ')
    count = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == '*':
            count = count * int(parts[i+1])
    return count

count = 0
for l in lines:
    count += resolve2(l.strip())

print('Part 2:', count)
