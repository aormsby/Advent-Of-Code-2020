import re

def getCreds(filename):
    c = []
    with open(filename) as creds:
        # separate cred sets
        people = creds.read().split('\n\n')
        # match all k/v pairs
        for p in people:
            singleSet = {}
            items = re.findall("\S+:\S+", p)
            # for each k/v pair, add entry to dict
            for i in items:
                key,value = i.split(':')
                singleSet[key] = value
            # add dict to array 'c'
            c.append(singleSet)
    return c

def hasAllKeys(cred, keys):
    for k in keys:
        if k in cred:
            continue
        else:
            return False
    return True

def removeCredsByKeys (credSet):
    cs = credSet[:]
    for c in credSet:
        if hasAllKeys(c, requiredKeys):
            continue
        else:
            cs.remove(c)
    
    return cs

def isValidYear(year, min, max):
    if not min <= int(year) <= max:
        return False
    return True

def isValidHeight(height):
    if not re.match(r'(^\d{3}cm)|(^\d{2}in)', height):
        return False
    
    num = int(height[:-2])
    unit = height[-2:]

    if unit == 'in' and (not 59 <= num <= 76):
        return False
    elif unit == 'cm' and (not 150 <= num <= 193):
        return False
    
    return True

def isValidHairColor(color):
    if not re.match(r'^#\w{6}$', color):
        return False
    
    return True

def isValidEyeColor(color):
    if not re.match(r'(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)', color):
        return False
    
    return True

def isValidPassportID(id):
    if not re.match(r'\d{9}$', id):
        return False
    
    return True
    

def removeInvalidCreds (credSet):
    cs = credSet[:]
    for c in credSet:
        if not isValidYear(c['byr'], 1920, 2002):
            cs.remove(c)
            continue
        if not isValidYear(c['iyr'], 2010, 2020):
            cs.remove(c)
            continue
        if not isValidYear(c['eyr'], 2020, 2030):
            cs.remove(c)
            continue
        if not isValidHeight(c['hgt']):
            cs.remove(c)
            continue
        if not isValidHairColor(c['hcl']):
            cs.remove(c)
            continue
        if not isValidEyeColor(c['ecl']):
            cs.remove(c)
            continue
        if not isValidPassportID(c['pid']):
            cs.remove(c)
            continue
    return cs

### end functions

requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
creds = getCreds('creds.txt')
# creds = getCreds('test.txt')
creds = removeCredsByKeys(creds)
print(len(creds))

### end part 1

creds = removeInvalidCreds(creds)
# print(creds)
print(len(creds))