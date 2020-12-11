import itertools
import copy

def findStability(chart):
    topEnd = 0
    bottomEnd = len(chart) - 1
    leftEnd = 0
    rightEnd = len(chart[0]) - 1

    lastPhase = copy.deepcopy(chart)
    thisPhase = None
    
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

            adjacent = []
            if (r != topEnd):
                adjacent.append(lastPhase[r-1][c])
            if (r != bottomEnd):
                adjacent.append(lastPhase[r+1][c])
            if (c != leftEnd):
                adjacent.append(lastPhase[r][c-1])
            if (c != rightEnd):
                adjacent.append(lastPhase[r][c+1])
            if (r != topEnd and c != leftEnd):
                adjacent.append(lastPhase[r-1][c-1])
            if (r != topEnd and c != rightEnd):
                adjacent.append(lastPhase[r-1][c+1])
            if (r != bottomEnd and c != leftEnd):
                adjacent.append(lastPhase[r+1][c-1])
            if (r != bottomEnd and c != rightEnd):
                adjacent.append(lastPhase[r+1][c+1])

            if lastPhase[r][c] == 'L' and adjacent.count('#') == 0:
                thisPhase[r][c] = '#'
            elif lastPhase[r][c] == '#' and adjacent.count('#') >= 4:
                thisPhase[r][c] = 'L'

            # print(lastPhase[r][c], '-', adjacent)

        # print('this\n')
        # for r in thisPhase:
        #     print(r)
        # print('\n----------------')
    occupiedSeats = sum([row.count('#') for row in thisPhase])
    return occupiedSeats

# seats = [list(x.strip('\n')) for x in open('test1.txt')]
# seats = [list(x.strip('\n')) for x in open('test2.txt')]
seats = [list(x.strip('\n')) for x in open('seating.txt')]
# print(seats)

endSeatsOccupied = findStability(seats)
print('stable, occupied seats =>', endSeatsOccupied)
