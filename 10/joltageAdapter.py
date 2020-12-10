from functools import reduce

def readList(filename):
    return [int(x.strip('\n')) for x in open(filename)]

def mapJoltageDiffs(jolts):    
    jolts.append(0)          # add oultet joltage
    jolts.sort()
    jolts.append(jolts[-1]+3)  # add device joltage
    print(jolts)

    diffsMap = {}

    for i in range(1, len(jolts)):
        diff = jolts[i-1] - jolts[i]
        dMapValue = diffsMap.get(diff)
        dMapValue = dMapValue + 1 if dMapValue is not None else 1
        diffsMap.update({diff : dMapValue})

    return diffsMap

joltageList = readList('test1.txt')
# joltageList = readList('test2.txt')
# joltageList = readList('joltageList.txt')
# print(joltageList)

diffs = mapJoltageDiffs(joltageList)
# print(diffs)

diffsProduct = reduce(lambda a,b: a*b, diffs.values())
print('diffs product =>', diffsProduct)
