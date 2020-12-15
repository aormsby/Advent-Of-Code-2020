import re
from itertools import product

def readMaskGroups(filename):
    index = []
    with open(filename) as data:
        mask = ''
        for line in data.readlines():
            if 'mask' in line:
                mask = re.search(r'[01X]+', line)
                index.append([mask.group(0)])
            else:
                val = re.findall(r'\[(\d+)\] = (\d+)', line)
                index[-1].append([int(s) for s in list(*val)])
    return index

def decode(groups):
    output = {}

    for g in groups:
        baseMask = g[0]
        andMask = int(baseMask.replace('X', '1'), 2)
        orMask = int(baseMask.replace('X', '0'), 2)
        # print('and:', bin(andMask))
        # print('or:', bin(orMask))

        for i in range(1, len(g)):
            ind = g[i][0]
            num = g[i][1]
            num &= andMask
            num |= orMask
            # print('num:', num)
            output[ind] = num
    
    return output

def decodeMemory(groups):
    output = {}

    for g in groups:
        baseMask = g[0]
        dualMask = int(baseMask.replace('X', '1'), 2)
        print('mask:', bin(dualMask))

        for i in range(1, len(g)):
            ind = g[i][0]
            num = g[i][1]
            ind &= dualMask
            ind |= dualMask
            print('new mem:', ind)
            # output[ind] = num
    
    return output
            

#######

maskingGroups = readMaskGroups('test1.txt')
# maskingGroups = readMaskGroups('init.txt')
# for g in maskingGroups:
#     print(g)

initOutput = decode(maskingGroups)
print('sum leftovers =>', sum(initOutput.values()))

initMemOutput = decodeMemory(maskingGroups)
print('mem sum leftovers =>', sum(initMemOutput.values()))
