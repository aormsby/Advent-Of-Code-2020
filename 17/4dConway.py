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

def generateEmptyCube(cube):
    empty = []
    for i in range(len(cube)):
        empty.append(generateEmptyZSpace(cube[0]))
    return empty

def setupStartCycle(filename):
    # read raw file
    initSlice = [[c for c in r.strip('\n')] for r in open(filename).readlines()]

    # pad = 2
    xypad = 6
    zpad = 6
    wpad = 6

    # widen slice with padding
    for i in range(len(initSlice)):
        initSlice[i] = generatePadding(xypad) + initSlice[i] + generatePadding(xypad)
    # print(*initSlice)

    #lengthen slice with rows
    initSlice = generateEmptyRows(len(initSlice[0]), xypad) + initSlice + generateEmptyRows(len(initSlice[0]), xypad)

    zCount = 0
    zLevels = []
    while zCount <= zpad:
        zLevels.append(generateEmptyZSpace(initSlice))
        zCount += 1

    cube = [*copy.deepcopy(zLevels), copy.deepcopy(initSlice), *copy.deepcopy(zLevels)]
    emptyCube = generateEmptyCube(cube)

    wCount = 0
    wLevels = []
    while wCount <= wpad:
        wLevels.append(copy.deepcopy(emptyCube))
        wCount += 1

    wCube = [*copy.deepcopy(wLevels), copy.deepcopy(cube), *copy.deepcopy(wLevels)]

    # for w in range(len(wCube)):
    #     for z in range(len(wCube[w])):
    #         print('w =', ((len(wCube) // 2) - w) * -1)
    #         print('z =', ((len(wCube[w][z]) // 2) - z) * -1)
    #         for x in wCube[w][z]:
    #             print(*x)
    #         print()

    return wCube

def adjPoints(wC, zC, xC, yC):
    ranges = [
        range(wC-1, wC+2),
        range(zC-1, zC+2),
        range(xC-1, xC+2),
        range(yC-1, yC+2)
    ]

    spaces = [s for s in itertools.product(*ranges)]
    spaces.remove((wC, zC, xC, yC))
    # print(*spaces)
    return spaces

def expandSlices(cube, amount):
    for s in range(len(cube)):
        for x in range(len(cube[0])):
            cube[s][x] = generatePadding(amount // 2) + cube[s][x] + generatePadding(amount // 2)
    
    for s in range(len(cube)):
        cube[s] = generateEmptyRows(len(cube[s][0]), amount // 2) + cube[s] + generateEmptyRows(len(cube[s][0]), amount // 2)
    
    return cube

def runCycles(start, numCycles):
    curCycle = copy.deepcopy(start)
    cycleCount = 1

    while cycleCount <= numCycles:
        print('cycle', cycleCount, '.......')
        nextCycle = copy.deepcopy(curCycle)

        # # @ start of cycle
        # if cycleCount == 1:
        #     for nz in nextCycle:
        #         for nx in nz:
        #             print(*nx)
        #         print()
        
        ranges = [
            range(1, len(curCycle)-1),          # wr
            range(1, len(curCycle[0])-1),       # zr
            range(1, len(curCycle[0][0])-1),    # xr
            range(1, len(curCycle[0][0])-1)     # yr
        ]
        # for ra in ranges:
        #     print(*ra)

        for w, z, x, y in itertools.product(*ranges):
            curVal = copy.copy(curCycle[w][z][x][y])
            # print(w, z, x, y, curVal)
            # print(nextCycle[w][z][x][y], '\n')
            
            adjacentPointVals = [curCycle[a][b][c][d] for a,b,c,d in adjPoints(w,z, x, y)]
            # if '#' in adjacentPointVals:
            #     print('\n', [curVal], ':', w,z,x,y, '\n', adjacentPointVals)
            if len(adjacentPointVals) != 80:
                print('wtf bro')

            numHash = adjacentPointVals.count('#')

            if curVal == '.' and numHash == 3:
                curVal = '#'
                # print('change to #')
            elif curVal == '#' and numHash != 2 and numHash != 3:
                curVal = '.'
                # print('change to .')

            nextCycle[w][z][x][y] = curVal


        # bounds expand
        # for zSlice in nextCycle:
        #     if '#' in zSlice[1] or '#' in zSlice[-2]:
        #         nextCycle = expandSlices(nextCycle, 6)
        #         break
        #     else:     # check side columns
        #         ind = 0
        #         while ind < len(zSlice[0]):
        #             if zSlice[ind][1] == '#' or zSlice[ind][-2] == '#':
        #                 nextCycle = expandSlices(nextCycle, 6)
        #                 break
        #             ind += 1

        
        # zExpand
        # zNet = list(itertools.chain.from_iterable([*nextCycle[1], *nextCycle[-2]]))
        # # print(zBounds)
        # if '#' in zNet:
        #     nextCycle.insert(0, generateEmptyZSpace(nextCycle[0]))
        #     nextCycle.append(generateEmptyZSpace(nextCycle[0]))

        # visualize @ end of cycle
        # if cycleCount == 2:
        #     for w in range(len(nextCycle)):
        #         for z in range(len(nextCycle[w])):
        #             print('w =', ((len(nextCycle) // 2) - w) * -1)
        #             print('z =', ((len(nextCycle[w][z]) // 2) - z) * -1)
        #             for x in nextCycle[w][z]:
        #                 print(*x)
        #             print()
        
        curCycle = copy.deepcopy(nextCycle)
        cycleCount += 1

    finalFlat = list(itertools.chain(*list(itertools.chain(*list(itertools.chain(*list(itertools.chain(*nextCycle))))))))
    print(finalFlat.count('#'))

########

# startCycle = setupStartCycle('test1.txt')
startCycle = setupStartCycle('slice.txt')
lastCycle = runCycles(startCycle, 6)
