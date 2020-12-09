def readBootCode(filename):
    bc = []
    with open(filename) as code:
        bc = list(map(lambda line: line.strip('\n'), [l for l in code.readlines()]))
    return bc    
    
    # didn't use, saving because awesome
    # ridiculous lambdas with list comprehensions :D
    # bc = list(map(lambda p: [p[0], p[1][0], int(p[1][1:len(p[1])])], map(lambda line: [l for l in line.strip('\n').split(' ')], [l for l in code.readlines()])))
    

def splitCode(code):
    c = code.split(' ')
    return [c[0], c[1][0], int(c[1][1:len(c[1])])]

def breakBootOnLoop(code):
    log = {}
    acc, i = 0, 0
    steps = []
    finished = True

    while i < len(code):
        codeKey = str(i) + '/' + code[i]
        steps.append(codeKey)
        # print(steps)

        n = log.get(codeKey)
        if n is None: n = 0
        # print(codeKey, ':', n)

        # if command is running a second time
        log.update({codeKey: n+1})
        if n == 1:
            finished = False
            break
        # print(log)

        command, op, num = splitCode(code[i])
        mod = 1 if op is "+" else -1
        # print(num, mod)
        
        if command == 'acc':
            acc += (num * mod)
        elif command == 'jmp':
            i += (num * mod) - 1
        
        i += 1
        
    return acc, log, steps, finished

def fixToComplete(code, steps):
    candidates = [x.split('/') for x in steps if 'jmp' in x or 'nop' in x]
    # print(candidates)

    acc = 0
    for i in range(len(candidates)-1, -1, -1):
        codeCopy = code.copy()  # fresh list
        cur = candidates[i]
        ind = int(candidates[i][0])

        change = cur[1].replace('jmp', 'nop') if 'jmp' in cur[1] else cur[1].replace('nop', 'jmp')
        # print(change)
        codeCopy[ind] = change
        # print(codeCopy)
        acc, log, steps, fin = breakBootOnLoop(codeCopy)
        # print(steps)

        if fin:
            # print('fin')
            break;

    return acc

################################

# boot = readBootCode('test.txt')
boot = readBootCode('boot.txt')
# print(boot)
acc, commandLog, steps, fin = breakBootOnLoop(boot)
print('acc =>', acc)
# print(steps)


finalAcc = fixToComplete(boot, steps)
print('final acc =>', finalAcc)