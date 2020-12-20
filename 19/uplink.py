import re

def readInput(filename):
    lines = [l.strip('\n') for l in open(filename).readlines()]
    halves = [lines[:lines.index('')], lines[lines.index('')+1:]]

    ruleset = {}
    for h in halves[0]:
        data = re.search(r'(\d): (.+)', h)
        d2 = data.group(2).strip('"').replace(' | ', '|').replace(' ', '')
        # if '|' in d2:
        #     d2 = d2.split('|')
        # else:
        #     d2 = d2.split(' ')
        ruleset.update({data.group(1) : d2})
    print(ruleset)

    return ruleset, halves[1]

def decodeRules(rules):
    letterKeys = dict(filter(lambda item: re.match(r'^[ab|_ ]+$', str(item[1])), rules.items()))
    ruleItems = dict(filter(lambda item: item not in letterKeys.items(), rules.items()))
    print(letterKeys)
    print(ruleItems)
    
    while len(ruleItems) > 0:

        for rk in ruleItems.keys():
            for lk in letterKeys.items():
                rule = ruleItems.get(rk)
                if lk[0] in rule:
                    lkupdate = lk[1]
                    if '|' in lkupdate:
                        lkupdate = ' ' + lkupdate + ' '
                    rule = rule.replace(lk[0], lkupdate)
                    ruleItems.update({rk : rule})
        
        newLKeys = dict(filter(lambda item: re.match(r'^[ab|_ ]+$', str(item[1])), ruleItems.items()))
        ruleItems = dict(filter(lambda item: item not in newLKeys.items(), ruleItems.items()))
        newLKeys = map(lambda item: (item[0], item[1] if item[0] != '0' else item[1]), newLKeys.items())
        letterKeys.update(newLKeys)
        # print(letterKeys)
        # print(ruleItems)

    # print(letterKeys)
    return letterKeys


##############

# rules, messages = readInput('test0.txt')
rules, messages = readInput('test1.txt')
# rules, messages = readInput('satelliteData.txt')
# print(rules, '\n', messages)

decodedRules = decodeRules(rules)
print(decodedRules)
