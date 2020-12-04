import re
lines = open('day4_input.txt').readlines()
requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validCount1 = validCount2 = 0
passportKeys = passportValues = []

def isValueValid(key, value):
    if key == 'pid': return value.isdigit() and len(value) == 9
    if key == 'ecl': return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'hcl': return value[0] == '#' and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value[1:]) and len(value) == 7
    if key == 'eyr': return value.isdigit() and len(value) == 4 and int(value) > 2019 and int(value) < 2031
    if key == 'iyr': return value.isdigit() and len(value) == 4 and int(value) > 2009 and int(value) < 2021
    if key == 'byr': return value.isdigit() and len(value) == 4 and int(value) > 1919 and int(value) < 2003
    if key == 'hgt': return value[-2:] in ['cm', 'in'] and value[0:-2].isnumeric() and ((int(value[0:-2]) > 58 and int(value[0:-2]) < 77),(int(value[0:-2]) > 149 and int(value[0:-2]) < 194))[value[-2:] == 'cm']
def isPassportValid1(keys):
    return all(x in keys for x in requiredKeys)
def isPassportValid2(keys, values):
    for i in range(len(keys)):
        if isValueValid(keys[i], values[i]) == False:
            return False
    return isPassportValid1(keys) 
def validatePassport(keys, values):
    global validCount1, validCount2
    if isPassportValid1(keys):
        validCount1 += 1
    if isPassportValid2(keys, values):
        validCount2 += 1

for lineCount in range(len(lines)):
    if(len(lines[lineCount].strip()) == 0):
        validatePassport(passportKeys, passportValues)
        passportKeys = []
        passportValues = []
        continue
    for part in lines[lineCount].strip().split(' '):
        passportKeys.append(part.split(':')[0])
        passportValues.append(part.split(':')[1])
    if(lineCount == len(lines)-1):
        validatePassport(passportKeys, passportValues)

print('Part 1:', validCount1)
print('Part 2:', validCount2)
