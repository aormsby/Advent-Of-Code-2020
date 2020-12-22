import regex
import copy

def readInput(filename):
    lines = [l.strip('\n') for l in open(filename).readlines()]
    halves = [lines[:lines.index('')], lines[lines.index('')+1:]]

    rules = {}
    for h in halves[0]:
        data = h.split(': ')
        val = data[1].replace('"', '').strip(' ')
        val = ' ' + val + ' '
        rules.update({data[0] : val})

    return rules, halves[1]

def checkForLoops(rSet):
    for key in rSet.keys():
        krMatch = regex.search(rf'\D{key}\D', rSet[key])
        if krMatch:
            val = rSet[key]
            numGroups = [g.strip().split(' ') for g in regex.search(r'(.*)\|(.*)', val).groups()]
            numGroups = sorted(numGroups, key=len)
            print(numGroups)
            print(val)
            temp = numGroups[1].copy()
            temp.remove(key)

            # haaaaaaaack
            if len(numGroups[0]) == 1:
                val = numGroups[0][0] + ' + '
                rSet.update({key : val})
            elif numGroups[0] == temp:
                val = '( ' + ' '.join(numGroups[1]).replace(key, '( ? @ ) *') + ' )'
                rSet.update({key : val})

    return rSet


def getRegexPattern(rSet):
    zRule = rSet['0']

    # while zero rule is still coded ...
    while any(x.isdigit() for x in list(zRule)):
        zRule = zRule.split()

        for i,num in enumerate(zRule):
            if num.isdigit():
                repl = rSet[num]

                if repl not in ['a', 'b']:
                    if '|' in repl:
                        repl = '( ? : ' + repl + ' )'
                
                zRule[i] = repl
        zRule = ' '.join(zRule)

    # cleanup
    zRule = '^' + zRule.replace(' ', '').replace('@', '1') + '$'
    return zRule

def checkValid(expr, messages):
    return len([m for m in messages if regex.match(expr, m)])

######

# ruleset, receivedMessages = readInput('test1.txt')
# ruleset, receivedMessages = readInput('satelliteData.txt')
# ruleset, receivedMessages = readInput('test2.txt')
ruleset, receivedMessages = readInput('satelliteData2.txt')

ruleset = checkForLoops(ruleset)
print(ruleset)

zeroExpression = getRegexPattern(ruleset)
print(zeroExpression)

numValidMessages = checkValid(zeroExpression, receivedMessages)
print('num valid =>', numValidMessages)
