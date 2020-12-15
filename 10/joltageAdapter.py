from functools import reduce

def readList(filename):
    return [int(x.strip('\n')) for x in open(filename)]

def mapJoltageDiffs(jolts):    
    diffsMap = {}
    branchGroups = []
    lastBranchIndex = 0

    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i-1]
        dMapValue = diffsMap.get(diff)
        dMapValue = dMapValue + 1 if dMapValue is not None else 1
        diffsMap.update({diff : dMapValue})

        if diff == 3:
            if lastBranchIndex != i-1:
                branchGroups.append(jolts[lastBranchIndex:i])
            lastBranchIndex = i

    return diffsMap, branchGroups
    
def makeAdjacencyList(branch):
    bGraph = {}

    for i in range(0, len(branch)):
        trip = branch[i:i+4]
        links = []
        j = 1

        while j < len(trip) and trip[j] - trip[0] <= 3:
            links.append(trip[j])
            j += 1

        bGraph.update({branch[i] : links})

    return bGraph

def dfsIterative(branch, start, end, pathCount=0):
    stack = []
    stack.append(start)

    while (len(stack) > 0):
        s = stack[-1]
        stack.pop()

        if s == end:
            pathCount += 1

        for next in branch[s]:
            stack.append(next)
    
    return pathCount

def findCombinations(branches):
    subPaths = []
    for b in branches:
        adjList = makeAdjacencyList(b)
        # print(adjList)
        subPaths.append(dfsIterative(adjList, b[0], b[-1]))
    # print(subPaths)
    return reduce(lambda a,b: a*b, subPaths)

########

# joltageList = readList('test1.txt')
# joltageList = readList('test2.txt')
joltageList = readList('joltageList.txt')
joltageList.sort()
joltageList.insert(0, 0)          # add outlet joltage
joltageList.append(joltageList[-1]+3)  # add device joltage
# print(joltageList)

diffs, branches = mapJoltageDiffs(joltageList)
# print(diffs)
# print(branches)

diffsProduct = reduce(lambda a,b: a*b, diffs.values())
print('diffs product =>', diffsProduct)

combinations = findCombinations(branches)
print('combinations =>', combinations)

