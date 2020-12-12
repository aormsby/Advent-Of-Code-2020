import itertools
import copy

def checkAdjacentSeats(phase, top, bottom, left, right, r, c):
    seatStatus = []
    if (r != top):
        seatStatus.append(phase[r-1][c])
    if (r != bottom):
        seatStatus.append(phase[r+1][c])
    if (c != left):
        seatStatus.append(phase[r][c-1])
    if (c != right):
        seatStatus.append(phase[r][c+1])
    if (r != top and c != left):
        seatStatus.append(phase[r-1][c-1])
    if (r != top and c != right):
        seatStatus.append(phase[r-1][c+1])
    if (r != bottom and c != left):
        seatStatus.append(phase[r+1][c-1])
    if (r != bottom and c != right):
        seatStatus.append(phase[r+1][c+1])

    return seatStatus

def storeVisibleSeats(chart, top, bottom, left, right):
    lineOfSightMap = {}

    for row,col in itertools.product(range(bottom+1), range(right+1)):
        if chart[row][col] == '.':
            continue
        
        visibleSeatCoords = []

        r,c = row,col
        while r != top:
            if chart[r-1][c] == '.':
                r -= 1
                continue;
            visibleSeatCoords.append([r-1, c])
            break
        r,c = row,col
        while r != bottom:
            if chart[r+1][c] == '.':
                r += 1
                continue;
            visibleSeatCoords.append([r+1, c])
            break
        r,c = row,col
        while c != left:
            if chart[r][c-1] == '.':
                c -= 1
                continue;
            visibleSeatCoords.append([r, c-1])
            break
        r,c = row,col
        while c != right:
            if chart[r][c+1] == '.':
                c += 1
                continue;
            visibleSeatCoords.append([r, c+1])
            break
        r,c = row,col
        while r != top and c != left:
            if chart[r-1][c-1] == '.':
                r -= 1
                c -= 1
                continue;
            visibleSeatCoords.append([r-1, c-1])
            break
        r,c = row,col
        while r != bottom and c != right:
            if chart[r+1][c+1] == '.':
                r += 1
                c += 1
                continue;
            visibleSeatCoords.append([r+1, c+1])
            break
        r,c = row,col
        while r != top and c != right:
            if chart[r-1][c+1] == '.':
                r -= 1
                c += 1
                continue;
            visibleSeatCoords.append([r-1, c+1])
            break
        r,c = row,col
        while r != bottom and c != left:
            if chart[r+1][c-1] == '.':
                r += 1
                c -= 1
                continue;
            visibleSeatCoords.append([r+1, c-1])
            break
        
        rowCoord = str(row)
        if (len(rowCoord) == 1): rowCoord = '0' + rowCoord
        colCoord = str(col)
        if (len(colCoord) == 1): colCoord = '0' + colCoord

        lineOfSightMap[rowCoord + colCoord] = visibleSeatCoords
    
    # for k in lineOfSightMap.keys():
    #     v = list(map(lambda x: chart[x[0]][x[1]], lineOfSightMap[k]))
    #     print(k, ':', lineOfSightMap[k])
        # print(v)
    
    return lineOfSightMap

# def checkLineOfSight(phase, top, bottom, left, right, row, col):
def checkLineOfSight(lPhase, seatMap, row, col):
    seatStatus = []

    rowCoord = str(row)
    if (len(rowCoord) == 1): rowCoord = '0' + rowCoord
    colCoord = str(col)
    if (len(colCoord) == 1): colCoord = '0' + colCoord

    for seat in seatMap.get(rowCoord + colCoord):
        seatStatus.append(lPhase[seat[0]][seat[1]])

    return seatStatus

def findStability(chart, lineOfSight=False):
    topEnd = 0
    bottomEnd = len(chart) - 1
    leftEnd = 0
    rightEnd = len(chart[0]) - 1

    occupationThreshold = 4

    if lineOfSight:
        occupationThreshold = 5
        seatMap = storeVisibleSeats(chart, topEnd, bottomEnd, leftEnd, rightEnd)
        # print(seatMap)

    lastPhase = copy.deepcopy(chart)
    thisPhase = None
    
    # i = 0
    while lastPhase != thisPhase:
        # i += 1

        if thisPhase is None:
            thisPhase = copy.deepcopy(lastPhase)
        else:
            lastPhase = copy.deepcopy(thisPhase)
        
        # print('\nlast phase\n')
        # for r in lastPhase:
        #     print(r)
        # print()
        
        for r,c in itertools.product(range(bottomEnd+1), range(rightEnd+1)):
            if lastPhase[r][c] == '.':
                continue

            if lineOfSight:
                seatCheck = checkLineOfSight(lastPhase, seatMap, r, c)
            else:
                seatCheck = checkAdjacentSeats(lastPhase, topEnd, bottomEnd, leftEnd, rightEnd, r, c)

            # print(seatCheck)

            if lastPhase[r][c] == 'L' and seatCheck.count('#') == 0:
                thisPhase[r][c] = '#'
            elif lastPhase[r][c] == '#' and seatCheck.count('#') >= occupationThreshold:
                thisPhase[r][c] = 'L'
            
            # if 0 < i < 4 and r == 9 and 19 < c < 24:
                # print('\n')
                # print(r,c, lastPhase[r][c], '-', seatCheck, thisPhase[r][c])
            
        # if (1 < i < 3):
        #     print(f'this phase ({i})\n')
        #     line = 0;
        #     for r in thisPhase:
        #         line += 1
        #         print(line, r)
        #     print('\n----------------')
        
    # print(i)

    # print('final phase\n')
    # for r in thisPhase:
    #     print(r)
    # print('\n----------------')

    occupiedSeats = sum([row.count('#') for row in thisPhase])
    return occupiedSeats

#################################

# seats = [list(x.strip('\n')) for x in open('test1.txt')]
# seats = [list(x.strip('\n')) for x in open('test2.txt')]
seats = [list(x.strip('\n')) for x in open('seating.txt')]
# print(seats)

endSeatsOccupied = findStability(seats)
print('stable, occupied seats =>', endSeatsOccupied)

import time
start = time.time()

losSeatsOccupied = findStability(seats, True)
print('line of sight, occupied seats =>', losSeatsOccupied)

end = time.time()
print(end - start)