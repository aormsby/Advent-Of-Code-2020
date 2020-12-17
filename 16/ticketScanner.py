import re
from functools import reduce

def parseTicketData(filename):
    groups = [l.strip('\n').split('\n') for l in open(filename, 'r').read().split('\n\n')]
    
    fields = []
    for i in range(len(groups[0])):
        sides = groups[0][i].split(':')
        f = [sides[0]]
        f.append(tuple(int(d) for d in re.findall(r'\d+', sides[1])))
        fields.append(f)
    
    mine = tuple(int(n) for n in groups[1][1].split(','))
    theirs = []
    for i in range(1, len(groups[2])):
        theirs.append(tuple(int(n) for n in groups[2][i].split(',')))
    
    return fields, mine, theirs

def findScanErrorRate(fields, mine, theirs):
    validValues = set()

    for f in fields:
        validValues.update(range(f[1][0], f[1][1]+1))
        validValues.update(range(f[1][2], f[1][3]+1))
    # print(validValues)

    testValues = []
    for t in theirs:
        testValues.extend(t)
    # print(testValues)

    invalidValues = set(testValues).difference(validValues)
    # print(invalidValues)

    errorRate = reduce(lambda a,b: a + (testValues.count(b) * b), invalidValues)
    return invalidValues, errorRate

def matchFieldsToValues(fields, mine, theirs, invalids):
    validTickets = []
    for t in theirs:
        add = True
        for n in invalids:
            if n in t:
                add = False
                break
        if add:
            validTickets.append(t)
    # print(theirs)
    # print(validTickets)

    fieldRanges = {}
    for f in fields:
        r = set(range(f[1][0], f[1][1]+1))
        r.update(range(f[1][2], f[1][3]+1))
        fieldRanges.update({f[0] : r})
    # print(fieldRanges)


    possibleMatches = []
    for ticket in validTickets:

        vGroup = []
        for i in range(len(ticket)):
            vMatches = set()

            for f in fieldRanges:
                if ticket[i] in fieldRanges.get(f):  # possible match
                    vMatches.add(f)
            vGroup.append((i, vMatches))
        
        possibleMatches.append(vGroup)
    
    # for pm in possibleMatches:
    #     print(pm)

    indexMatches = {}
        
    for i in range(len(possibleMatches[0])):    # num indices
        inData = []

        for j in possibleMatches:   # num tickets
            # print(j[i])
            inData.append(j[i][1])
        # print(inData)
        match = reduce(lambda a,b: a.intersection(b), inData)
        # print(match)
        indexMatches.update({i : match})

    sureMatchFields = []
    while len(sureMatchFields) < len(fields):
        for k in indexMatches:
            vals = indexMatches.get(k)
            if len(vals) == 1:
                v = [x for x in vals]
                if v[0] not in sureMatchFields:
                    sureMatchFields.append(v[0])
            else:
                vals = vals.difference(sureMatchFields)
                indexMatches[k] = vals

    # for k,v in zip(indexMatches.keys(), indexMatches.values()):
    #     print(k,v)

    departKeys = [k for k in indexMatches if 'departure' in str(indexMatches.get(k))]
    departProd = reduce(lambda a,b: a * mine[b], departKeys, 1)
    return departProd


########


# ticketFields, myTicket, theirTickets = parseTicketData('test1.txt')
ticketFields, myTicket, theirTickets = parseTicketData('ticketData.txt')
# print(ticketFields)
# print(myTicket)
# print(theirTickets)

invalidVals, scanErrorRate = findScanErrorRate(ticketFields, myTicket, theirTickets)
print('scan error rate =>', scanErrorRate)

# ticketFields, myTicket, theirTickets = parseTicketData('test2.txt')
departureProduct = matchFieldsToValues(ticketFields, myTicket, theirTickets, invalidVals)
print('departure product =>', departureProduct)

# TODO: learn more about var scope in Python, this is a mess
