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

def checkLineOfSight(phase, top, bottom, left, right, row, col):
    seatStatus = []

    r,c = row,col
    while r != top:
        if phase[r-1][c] == '.':
            r -= 1
            continue;
        seatStatus.append(phase[r-1][c])
        break
    r,c = row,col
    while r != bottom:
        if phase[r+1][c] == '.':
            r += 1
            continue;
        seatStatus.append(phase[r+1][c])
        break
    r,c = row,col
    while c != left:
        if phase[r][c-1] == '.':
            c -= 1
            continue;
        seatStatus.append(phase[r][c-1])
        break
    r,c = row,col
    while c != right:
        if phase[r][c+1] == '.':
            c += 1
            continue;
        seatStatus.append(phase[r][c+1])
        break
    r,c = row,col
    while r != top and c != left:
        if phase[r-1][c-1] == '.':
            r -= 1
            c -= 1
            continue;
        seatStatus.append(phase[r-1][c-1])
        break
    r,c = row,col
    while r != bottom and c != right:
        if phase[r+1][c+1] == '.':
            r += 1
            c += 1
            continue;
        seatStatus.append(phase[r+1][c+1])
        break
    r,c = row,col
    while r != top and c != right:
        if phase[r-1][c+1] == '.':
            r -= 1
            c += 1
            continue;
        seatStatus.append(phase[r-1][c+1])
        break
    r,c = row,col
    while r != bottom and c != left:
        if phase[r+1][c-1] == '.':
            r += 1
            c -= 1
            continue;
        seatStatus.append(phase[r+1][c-1])
        break

    return seatStatus


def findStability(chart, lineOfSight=False):
    topEnd = 0
    bottomEnd = len(chart) - 1
    leftEnd = 0
    rightEnd = len(chart[0]) - 1

    lastPhase = copy.deepcopy(chart)
    thisPhase = None

    occupationThreshold = 5 if lineOfSight else 4
    
    while lastPhase != thisPhase:
    # i = 0
    # while i < 2:
    #     i += 1

        if thisPhase is None:
            thisPhase = copy.deepcopy(lastPhase)
        else:
            lastPhase = copy.deepcopy(thisPhase)
        
        # print('\nlast\n')
        # for r in lastPhase:
        #     print(r)
        # print()
        
        for r,c in itertools.product(range(bottomEnd+1), range(rightEnd+1)):
            if lastPhase[r][c] == '.':
                continue

            if lineOfSight:
                seatCheck = checkLineOfSight(lastPhase, topEnd, bottomEnd, leftEnd, rightEnd, r, c)
            else:
                seatCheck = checkAdjacentSeats(lastPhase, topEnd, bottomEnd, leftEnd, rightEnd, r, c)

            if lastPhase[r][c] == 'L' and seatCheck.count('#') == 0:
                thisPhase[r][c] = '#'
            elif lastPhase[r][c] == '#' and seatCheck.count('#') >= occupationThreshold:
                thisPhase[r][c] = 'L'

            # print(lastPhase[r][c], '-', seatCheck)

        # print('this\n')
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

losSeatsOccupied = findStability(seats, True)
print('stable, line of sight, occupied seats =>', losSeatsOccupied)
