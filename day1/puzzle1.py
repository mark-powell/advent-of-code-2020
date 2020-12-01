file1 = open('day1/data.txt', 'r') 
lines = file1.readlines()

for lineCount in range(len(lines)):
    for lineCount2 in range(lineCount+1, len(lines)):
        num1 = int(lines[lineCount].strip());
        num2 = int(lines[lineCount2].strip());
        if num1 + num2 == 2020:
            print(num1 * num2);
    