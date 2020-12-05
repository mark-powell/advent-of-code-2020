file = open('day5_input.txt', 'r')
lines = file.readlines()

def binarySearch(list, upperChar):
    upperVal = 2**len(list)
    lowerVal = 0
    for i in range(len(list)):
        half = (upperVal-lowerVal)/2
        if list[i] == upperChar:
            lowerVal += half
        else:
            upperVal -= half
    return lowerVal

hightestSeatId = 0
mySeatId = 0
seatList = []
for line in lines:
    seatId = binarySearch(line[:7].strip(),'B') * 8 + binarySearch(line[7:].strip(),'R')
    seatList.append(seatId)
    if seatId > hightestSeatId:
        hightestSeatId = seatId
for i in range(int(hightestSeatId)):
    if i not in seatList and i+1 in seatList and i-1 in seatList:
        mySeatId = i
        break



print('Part 1:', hightestSeatId)
print('Part 2:', mySeatId)
