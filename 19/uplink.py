import re

def readInput(filename):
    lines = [l.strip('\n') for l in open(filename).readlines()]
    halves = [lines[:lines.index('')], lines[lines.index('')+1:]]

    ruleset = {}
    for h in halves[0]:
        data = re.search(r'(\d+): (.+)', h)
        d2 = data.group(2).strip('"')#.replace(' | ', '|').replace(' ', '')
        if '|' in d2:
            d2 = '( ' + d2 + ' )'
        # print(d2)
        # else:
        #     d2 = d2.split(' ')
        ruleset.update({data.group(1) : d2})
    # print(ruleset)

    # for k,v in zip(ruleset.keys(), ruleset.values()):
    #     print(k,v)

    return ruleset, halves[1]

def decodeRules(rules):
    letterKeysPattern = r'^[ab| \(\)\+]+$'
    letterKeys = dict(filter(lambda item: re.match(letterKeysPattern, str(item[1])), rules.items()))
    # print('lk:', letterKeys)
    ruleItems = dict(filter(lambda item: item not in letterKeys.items(), rules.items()))
    # print('ri:', ruleItems)
    
    while len(ruleItems) > 0:

        for rk in ruleItems.keys():
            for lk in letterKeys.items():
                rule = ruleItems.get(rk)
                if lk[0] in rule:

                keyCheck = re.search(rf'\D*{lk[0]}\D*', rule)

                if keyCheck is not None:
                    # print('lk[0]:', lk[0])
                    regexp = rf'(?:(?=\D)|(?<=\b))({lk[0]})(?:(?=\D)|(?=\b))'
                    # print('regexp:', regexp)

                    repl = lk[1]
                    # print('repl:', repl)

                    # print('before:', rule)
                    rule = re.sub(regexp, repl, rule)
                    # print('after:', rule)

                    ruleItems.update({rk : rule})

        newLKeys = dict(filter(lambda item: re.match(letterKeysPattern, str(item[1])), ruleItems.items()))
        ruleItems = dict(filter(lambda item: item not in newLKeys.items(), ruleItems.items()))
        letterKeys.update(newLKeys)

        # print('nlk:', newLKeys)
        # print('lk:', letterKeys)
        # print('ri:', ruleItems)
        # return {}

    # print(letterKeys)
    return letterKeys

def validateMessages(zRule, messages):
    # non-capture groups, yo
    zRule = zRule.replace(' ', '').replace('(', '(?:')
    pattern = rf'^{zRule}$'
    # print(pattern)
    valid = []
    for m in messages:
        check = re.match(pattern, m)
        if check is not None:
            valid.append(m)
    return valid

##############
import time
start = time.time()
# rules, receivedMessages = readInput('test0.txt')
# rules, receivedMessages = readInput('test1.txt')
rules, receivedMessages = readInput('test2.txt')
# rules, receivedMessages = readInput('satelliteData.txt')
# rules, receivedMessages = readInput('satelliteData2.txt')
# print(rules, '\n', receivedMessages)

decodedRules = decodeRules(rules)
# print(decodedRules.get('0'))

validMessages = validateMessages(decodedRules.get('0'), receivedMessages)
print('num valid messages =>', len(validMessages))

print(time.time() - start)
