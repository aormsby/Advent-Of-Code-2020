import regex

def readInput(filename):
    lines = [l.strip('\n') for l in open(filename).readlines()]
    halves = [lines[:lines.index('')], lines[lines.index('')+1:]]

    rules = {}
    for h in halves[0]:
        data = h.split(': ')
        val = data[1].replace('"', '').strip(' ')
        rules.update({data[0] : val})

    return rules, halves[1]

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
    zRule = '^' + zRule.replace(' ', '') + '$'
    return zRule

def checkValid(expr, messages):
    return len([m for m in messages if regex.match(expr, m)])

######

ruleset, receivedMessages = readInput('test1.txt')
ruleset, receivedMessages = readInput('satelliteData.txt')
print(ruleset)

zeroExpression = getRegexPattern(ruleset)
print(zeroExpression)

numValidMessages = checkValid(zeroExpression, receivedMessages)
print('num valid =>', numValidMessages)
