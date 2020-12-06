def readBoardingPasses(filename):
    bPasses = []
    with open(filename) as passList:
        bp = passList.readlines()
        for p in bp:
            bPasses.append([p.strip('\n')])
    return bPasses

rowRange = list(range(0,127+1))
columnRange = list(range(0,7+1))

def parseRowColumn(pid):
    row = rowRange[:]
    column = columnRange[:]

    for c in pid:
        if c == 'F':
            # print('c:',c,'len:',len(row),'len/2:',int(len(row)/2))
            row = row[:int(len(row)/2)]
            # print(row)
        elif c == 'B':
            row = row[int(len(row)/2):]
        elif c == 'L':
            column = column[:int(len(column)/2)]
        elif c == 'R':
            column = column[int(len(column)/2):]
        else:
            raise ValueError('Incorrect Input: ' + c)

    position =(row[0], column[0])
    return position

def calcSeatID(row, column):
    return (row * 8) + column

passes = readBoardingPasses('boardingpasses.txt')
seatIDs = []
for i in range(0, len(passes)):
    passes[i].append(parseRowColumn(passes[i][0]))
    passes[i].append(calcSeatID(*passes[i][1]))
    seatIDs.append(passes[i][2])

print(passes)
print(max(seatIDs))

seatIDs.sort()
allIDs = set(range(seatIDs[0], seatIDs[-1]))
print(allIDs - set(seatIDs))