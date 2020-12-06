lines = open('day6_input.txt').readlines()
groupAnswers = []
groupAnswers2 = []
answerSum = 0
answerSum2 = 0

for lineCount in range(len(lines)):
    line = lines[lineCount].strip()
    if(len(line) == 0):
        answerSum += len(groupAnswers)
        answerSum2 += len(groupAnswers2)
        groupAnswers = []
        groupAnswers2 = []
        continue
    for answer in range(len(line)):
        if(line[answer] not in groupAnswers):
            groupAnswers.append(line[answer])
    if lineCount == 0 or len(lines[lineCount-1].strip()) == 0:
        groupAnswers2 = []
        for answer in range(len(line)):
            groupAnswers2.append(line[answer])
    else:
        for a in groupAnswers2.copy():
            if(a not in line):
                groupAnswers2.remove(a)
    if(lineCount == len(lines)-1):
        answerSum += len(groupAnswers)
        answerSum2 += len(groupAnswers2)

print('Part 1:', answerSum)
print('Part 2:', answerSum2)
