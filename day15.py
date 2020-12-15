lines = open('day15_input.txt').readlines()
numbers = [int(n) for n in lines[0].split(',')]

for count in range(len(numbers)-1,2019):
    if numbers.count(numbers[count]) == 1:
        numbers.append(0)
    else:
        for i in range(len(numbers)-2, -1, -1):
            if numbers[i] == numbers[count]:
                numbers.append(count-i)
                break

print('Part 1:', numbers[-1])

startingRange = [int(n) for n in lines[0].split(',')]
numbers = {}
for i in range(len(startingRange)-1):
    numbers[startingRange[i]] = i

previousNumber = startingRange[-1]
for count in range(len(numbers),29999999):
    if previousNumber not in numbers:
        numbers[previousNumber] = count
        previousNumber = 0
    else:
        previousCount = numbers[previousNumber]
        numbers[previousNumber] = count
        previousNumber = count-previousCount
    
print('Part 2:', previousNumber)