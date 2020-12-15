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
        indeXes = [i for i,x in enumerate(baseMask) if x == 'X']
        xCombos = list(product('01', repeat=len(indeXes)))
        for i in range(len(xCombos)):
            xCombos[i] = tuple(int(x) for x in xCombos[i])
        # print('indeXes:', indeXes)
        # print('xCombos:', xCombos)

        bitCheckMasks = [(1 << 35 - X) for X in indeXes]
        # print('bc masks:', bitCheckMasks)

        orMask = int(baseMask.replace('X', '0'), 2)
        
        # apply all mask possibilities and store value in each mem space
        for i in range(1, len(g)):
            mem = g[i][0]   # mem index to manipulate
            val = g[i][1]   # value to save
            mem |= orMask  # initial OR with 0s
            # print('or\'d mem:', bin(mem))

            xBitStatus = tuple((mem & mask) for mask in bitCheckMasks)
            # print('x bit status:', xBitStatus)
            
            for xc in xCombos:
                memCopy = mem
                # print()
                for j in range(0, len(xc)):
                    target = xc[j]
                    status = xBitStatus[j]
                    # print('indeX', indeXes[j], 'target', target, 'status', status)

                    if target == 0 and status == 0:
                        pass
                    elif target == 1 and status != 0:
                        pass
                    else:
                            mask = 1 << 35 - indeXes[j]
                            # print('b:', bin(memCopy))
                            # print('m:', bin(mask))
                            memCopy ^= mask

                    # print('a:', bin(memCopy))
                    # print(memCopy)
                    # print()
                # print()

                output[memCopy] = val
    return output
            

#######

# maskingGroups = readMaskGroups('test1.txt')
# maskingGroups = readMaskGroups('test2.txt')
maskingGroups = readMaskGroups('init.txt')
# for g in maskingGroups:
#     print(g)

initOutput = decode(maskingGroups)
print('sum leftovers =>', sum(initOutput.values()))

initMemOutput = decodeMemory(maskingGroups)
print('mem sum leftovers =>', sum(initMemOutput.values()))
