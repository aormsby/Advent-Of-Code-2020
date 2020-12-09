def readCypher(filename):
    with open(filename) as cypher:
        c = [int(n) for n in cypher.readlines()]    
    return c

def findAnomaly (codes, preamble):
    i = preamble
    while i < len(codes):
        sumGroup = codes[i-preamble:i]
        sumGroup.sort()
        # print(sumGroup)

        x, y = 0, -1
        while sumGroup[x] < sumGroup[y]:
            sum = sumGroup[x] + sumGroup[y]
            
            if sum == codes[i]:
                break
            elif sum < codes[i]:
                x += 1
            else:   #if sum > codes[i]
                y -= 1
        else:
            return codes[i] # finished two-sum loop, found anomaly

        i += 1

def findWeakness(codes, target):
    # for i in codes[0:codes.index(target)]:
    i = 0
    while i < codes.index(target):
        summed = 0
        n = 2
        while summed < target:
            chunk = codes[i:n]
            summed = sum(chunk)
            if summed == target:
                return max(chunk) + min(chunk)
            n += 1
        i += 1

# cypher = readCypher('test.txt')
# anomaly = findAnomaly(cypher, 5)
cypher = readCypher('input.txt')
anomaly = findAnomaly(cypher, 25)
# print(cypher)
print('anomaly =>', anomaly)

weakness = findWeakness(cypher, anomaly)
print('weakness =>', weakness)