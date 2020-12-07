lines = open('day7_input.txt').readlines()
bags = {}

for lineCount in range(len(lines)):
    line = lines[lineCount].strip()
    bag = line.split(' bags contain ')[0]
    bags[bag] = []
    if line.split(' bags contain ')[1] == 'no other bags.':
        continue
    containsLine = line.split(' bags contain ')[1].split(' ')
    
    for i in range(0,len(containsLine),4):
        bags[bag].append({
           'qty':containsLine[i],
           'colour':containsLine[i+1] + ' ' + containsLine[i+2]
        })
        
def bagCanContain(search, find):
    for b in bags[search]:
        if b['colour'] == find:
            return True
        else:
            if bagCanContain(b['colour'], find):
                return True
    return False

def getBagCount(search):
    count = 0
    for b in bags[search]:
        count += int(b['qty'])
        count += getBagCount(b['colour']) * int(b['qty'])
    return count
        
answer1 = 0
for bagColour in bags.keys():
    if bagCanContain(bagColour, 'shiny gold'):
        answer1+=1

print('Part 1:', answer1)
print('Part 2:', getBagCount('shiny gold'))
