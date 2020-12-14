from functools import reduce

def readSchedule(filename):
    with open(filename) as table:
        etime = int(table.readline().strip('\n'))
        schedule = [n for n in table.readline().strip('\n').split(',')]
    return etime, schedule

def catchEarliestBus(time, schedule):
    waitTimes = [b - (time % b) for b in schedule]
    wait = min(waitTimes)
    busID = schedule[waitTimes.index(wait)]
    return busID, wait

def modMultInverse(a, mod):
    b = a % mod
    for x in range(0, mod):
        if (b * x) % mod == 1:
            return x

def chineseRemainder(n, a):
    N = reduce(lambda a,b: a*b, n)
    # print(N)  # 4199
    
    sum = 0
    for n_i, a_i in zip(n, a):
        Np = N // n_i
        sum += a_i * modMultInverse(Np, n_i) * Np
    
    return (N % sum)-(sum % N)

def findOffsetDepartures(schedule):
    data = {schedule.index(n):n for n in schedule if n != 'x'}
    # print(data)
    
    x = chineseRemainder(list(data.values()), list(data.keys()))
    return x
    


#####

# earliestTime, busSchedule = readSchedule('test1.txt')
# earliestTime, busSchedule = readSchedule('test2.txt')
earliestTime, busSchedule = readSchedule('busSchedule.txt')
# print(earliestTime)
# print(busSchedule)

intOnlySchedule = [int(n) for n in busSchedule if n != 'x']
idMatch, waitTime = catchEarliestBus(earliestTime, intOnlySchedule)
# print(idMatch, waitTime)
print('arbitrary product 1 =>', idMatch * waitTime)

mixedSchedule = []
for t in busSchedule:
    if t != 'x':
        mixedSchedule.append(int(t))
    else:
        mixedSchedule.append(t)
# print(mixedSchedule)

offsetTimestamp = findOffsetDepartures(mixedSchedule)
print('sequence offset:', offsetTimestamp)
