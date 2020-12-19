import copy
import itertools

def generateEmptyZSpace(slice):
    return [['.' for y in x] for x in slice]

def generateEmptyRows(sliceWidth, numRows=2):
    # return ['.' for y in range(sliceWidth)]
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

def printSlice(slice, text=''):
    print(text)
    for s in slice:
        print(*s)
    print()

def printCube(cube, text=''):
    print(text)
    for c in cube:
        for s in c:
            print(*s)
    print()

def printWCube(wCube, text=''):
    print(text)
    for w in wCube:
        for c in w:
            print()
            for s in c:
                print(*s)
    print()

#region - rows tests
# singleSlice = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
singleSlice = generateEmptyRows(3, 3)

printSlice(singleSlice, 'rows before')

singleSlice[0][0] = '#'
singleSlice[1][1] = '#'
singleSlice[2][2] = '#'

printSlice(singleSlice, 'rows after')
#endregion - rows tests

#region - pad tests
singleSlice = [['.'], ['.'], ['.']]
for i in range(len(singleSlice)):
    singleSlice[i] = generatePadding(2) + singleSlice[i] + generatePadding(2)

printSlice(singleSlice, 'pad before')

singleSlice[0][0] = '#'
singleSlice[1][1] = '#'
singleSlice[2][2] = '#'

printSlice(singleSlice, 'pad after')
#endregion - pad tests

#region - z level tests
cube = [generateEmptyRows(3, 3)]
cube.append(generateEmptyZSpace(cube[0]))
cube.insert(0, generateEmptyZSpace(cube[0]))

printCube(cube, 'z level before')

cube[0][0][0] = '#'
cube[1][1][1] = '#'
cube[2][2][2] = '#'

printCube(cube, 'z level after')
#endregion - z level tests

wCube = [generateEmptyCube(cube), generateEmptyCube(cube)]
printWCube(wCube, 'w before:')

wCube[0][0][0][0] = '#'
wCube[0][1][1][2] = '#'
wCube[0][2][2][2] = '#'

wCube[1][0][2][2] = '#'
wCube[1][1][1][0] = '#'
wCube[1][2][2][1] = '#'

printWCube(wCube, 'w after:')
