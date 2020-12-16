def setupGame(starters):
    startN = {}
    for s in range(len(starters)-1):
        startN.update({starters[s] : s+1})

    nextN = starters[-1]
    turnCount = len(starters)

    return startN, nextN, turnCount

def playGame(input, limit):
    numDict, nextNum, turn = setupGame(input)
    # print(numDict)
    # print('turn:', turn)
    # print('this num:', nextNum)
    # print()

    while turn < limit:
    # while turn < 10:
        memory = numDict.get(nextNum)
        # print('turn', turn)
        # print('this num', nextNum)
        # print('memory', memory)

        if memory is None:  # this num *not* spoken before
            numDict[nextNum] = turn
            nextNum = 0
        else:   # last num spoken before
            turnsDiff = turn - memory
            # print('diff', turnsDiff)
            numDict[nextNum] = turn
            nextNum = turnsDiff

        # print('next num', nextNum)
        # print()

        turn += 1
    
    return nextNum


###################
import time
startTime = time.time()

# numsInput = [0, 3, 6]  # test 1
# numsInput = [1, 3, 2]  # test 2
numsInput = [0,5,4,1,10,14,7]  # input

result1 = playGame(numsInput, 2020)
print('result 1 =>', result1)

result2 = playGame(numsInput, 30000000)
print('result 2 =>', result2)

print(time.time() - startTime)
