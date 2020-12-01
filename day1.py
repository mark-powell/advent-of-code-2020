file1 = open('day1_input.txt', 'r') 
lines = file1.readlines()

for lineCount in range(len(lines)):
    for lineCount2 in range(lineCount+1, len(lines)):
        num1 = int(lines[lineCount].strip());
        num2 = int(lines[lineCount2].strip());
        if num1 + num2 == 2020:
            print('Part 1:', num1* num2)
        for lineCount3 in range(lineCount2+1, len(lines)):
            num3 = int(lines[lineCount3].strip());
            if num1 + num2 + num3 == 2020:
                print('Part 2:', num1 * num2 * num3);
    
