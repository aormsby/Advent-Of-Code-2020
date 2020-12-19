import copy
import itertools

def generateEmptyZSpace(slice):
    return [['.' for y in x] for x in slice]

def generateEmptyRows(sliceWidth, numRows=2):
    # return [*itertools.repeat(['.' for y in range(sliceWidth)], numRows)]
    emptyRows = []
    singleRow = ['.' for y in range(sliceWidth)]
    for i in range(numRows):
        emptyRows.append(copy.deepcopy(singleRow))
    return emptyRows

def generatePadding(amount=2):
    return list(itertools.repeat('.', amount))

def setupStartCycle(filename):
    # read raw file
    initSlice = [[c for c in r.strip('\n')] for r in open(filename).readlines()]

    # widen slice with padding
    for i in range(len(initSlice)):
        initSlice[i] = generatePadding() + initSlice[i] + generatePadding()
    # print(*initSlice)

    #lengthen slice with rows
    initSlice = generateEmptyRows(len(initSlice[0])) + initSlice + generateEmptyRows(len(initSlice[0]))

    cube = [generateEmptyZSpace(initSlice), generateEmptyZSpace(initSlice), 
        initSlice, generateEmptyZSpace(initSlice), generateEmptyZSpace(initSlice)]

    # for c in cube:
    #     for x in c:
    #         print(*x)
    #     print()

    return cube

def adjPoints(zC, xC, yC):
    ranges = [
        range(zC-1, zC+2),
        range(xC-1, xC+2),
        range(yC-1, yC+2)
    ]

    spaces = [s for s in itertools.product(*ranges)]
    spaces.remove((zC, xC, yC))
    # print(*spaces)
    return spaces

def expandSlices(cube, amount):
    for s in range(len(cube)):
        for x in range(len(cube[0])):
            cube[s][x] = generatePadding(amount // 2) + cube[s][x] + generatePadding(amount // 2)
    
    for s in range(len(cube)):
        cube[s] = generateEmptyRows(len(cube[s][0]), amount // 2) + cube[s] + generateEmptyRows(len(cube[s][0]), amount // 2)
    
    return cube


    # initSlice = generateEmptyRows(len(initSlice[0])) + initSlice + generateEmptyRows(len(initSlice[0]))

def runCycles(start, numCycles):
    curCycle = copy.deepcopy(start)
    cycleCount = 1

    while cycleCount <= numCycles:
        nextCycle = copy.deepcopy(curCycle)

        # # @ start of cycle
        # if cycleCount == 1:
        #     for nz in nextCycle:
        #         for nx in nz:
        #             print(*nx)
        #         print()

        ranges = [
            range(1, len(curCycle)-1),      # zr
            range(1, len(curCycle[0])-1),   # xr
            range(1, len(curCycle[0])-1)    # yr
        ]
        # for ra in ranges:
        #     print(*ra)

        for z, x, y in itertools.product(*ranges):
            curVal = copy.copy(curCycle[z][x][y])
            # print(z, x, y, curVal)
            # print(nextCycle[z][x][y], '\n')
            
            adjacentPointVals = [curCycle[a][b][c] for a,b,c in adjPoints(z, x, y)]
            # print([curVal], ':', z,x,y, '\n', adjacentPointVals)

            numHash = adjacentPointVals.count('#')

            if curVal == '.' and numHash == 3:
                curVal = '#'
            elif curVal == '#' and numHash != 2 and numHash != 3:
                curVal = '.'
            
            nextCycle[z][x][y] = curVal


        # bounds expand
        for zSlice in nextCycle:
            if '#' in zSlice[1] or '#' in zSlice[-2]:
                nextCycle = expandSlices(nextCycle, 6)
                break
            else:     # check side columns
                ind = 0
                while ind < len(zSlice[0]):
                    if zSlice[ind][1] == '#' or zSlice[ind][-2] == '#':
                        nextCycle = expandSlices(nextCycle, 6)
                        break
                    ind += 1

        
        # zExpand
        zNet = list(itertools.chain.from_iterable([*nextCycle[1], *nextCycle[-2]]))
        # print(zBounds)
        if '#' in zNet:
            nextCycle.insert(0, generateEmptyZSpace(nextCycle[0]))
            nextCycle.append(generateEmptyZSpace(nextCycle[0]))

        # @ end of cycle
        if cycleCount == 6:
            for nz in nextCycle:
                for nx in nz:
                    print(*nx)
                print()
        
        curCycle = copy.deepcopy(nextCycle)
        cycleCount += 1

    finalFlat = list(itertools.chain(*list(itertools.chain(*nextCycle))))
    print(finalFlat.count('#'))

########

# startCycle = setupStartCycle('test1.txt')
startCycle = setupStartCycle('slice.txt')
lastCycle = runCycles(startCycle, 6)
