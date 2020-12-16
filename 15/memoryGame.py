def setupGame(starters):
    startN = {}
    for s in range(len(starters)):
        startN.update({starters[s] : [s+1, 1]})
    
    # for first check of last num after starters to get 0, goal is simpler logic
    startN.update({starters[-1] : [len(starters), 0]})

    lastN = starters[-1]
    turnCount = len(starters)

    return startN, lastN, turnCount

def playGame(input, limit):
    numDict, lastNum, turn = setupGame(input)
    # print(numDict)
    # print('last num:', lastNum)
    # print('turn:', turn)
    # print()

    while turn < limit:
    # while turn <= 10:
        memory = numDict.get(lastNum)
        # print('turn', turn)
        # print('num', lastNum)
        # print('memory', memory)

        if memory[1] == 0:  # last num *not* spoken before
            memory[1] = 1
            numDict.update({lastNum : memory})
            nextNum = 0
        elif memory[1] == 1:   # last num spoken before
            turnsDiff = turn - memory[0]
            # print('diff', turnsDiff)
            memory[0] = turn
            numDict.update({lastNum : memory})
            nextNum = turnsDiff

        if numDict.get(nextNum) is None:
            numDict.update({nextNum : [turn+1, 0]})

        # print()

        lastNum = nextNum
        turn += 1
    
    return lastNum


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