import re

def parseInput(filename):
    arr = []
    with open(filename) as input:
        raw = input.read().splitlines()
        for r in raw:
            full = r.split(': ')
            crit = full[0].split()
            nums = crit[0].split('-')
            arr.append([int(nums[0]), int(nums[1]), crit[1], full[1]])
    return arr

def checkPassword1(passSet):
    found = re.findall(f'{passSet[2]}', passSet[-1])
    if passSet[0] <= len(found) <= passSet[1]:
        return True
    return False

def checkPassword2(passSet):
    p1 = passSet[-1][passSet[0]-1] == passSet[2]
    p2 = passSet[-1][passSet[1]-1] == passSet[2]
    
    if p1 == p2:
        return False
    return True

passArr = parseInput('input.txt')

numValid1 = 0
for p in passArr:
    if checkPassword1(p):
        numValid1 += 1

print(numValid1)

numValid2 = 0
for p in passArr:
    if checkPassword2(p):
        numValid2 += 1

print(numValid2)