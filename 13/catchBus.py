import math

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

# def findGCD(x,y):
#     while y:
#         x, y = y, x % y
#     return x

# def findLCM(x,y):
#     return (x*y)//findGCD(x,y)

def findOffsetDepartures(schedule):
    baseInts = [n for n in schedule if n != 'x']
    
    # baseInts = [n for n in schedule if n != 'x']
    # # intsIndex = [schedule.index(n) for n in schedule if n != 'x']
    # maxID = max(baseInts)
    # # print(baseInts)
    # # print(intsIndex)

#####

earliestTime, busSchedule = readSchedule('test1.txt')
# earliestTime, busSchedule = readSchedule('busSchedule.txt')
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
# print(offsetTimestamp)
