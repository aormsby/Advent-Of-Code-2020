
compass = {
    0 : 'N',
    270 : 'W',
    180 : 'S',
    90 : 'E',
    'N' : [0, (0,1)],
    'W' : [270, (-1,0)],
    'S' : [180, (0,-1)],
    'E' : [90, (1,0)]
}

def followCourse(course, heading=0, position=(0,0)):
    for step in course:
        direction = step[0]
        distance = int(step[1])
        # print('\ndirection:', direction)
        # print('distance:', distance)
        # print('heading:', heading)

        if direction == 'R':
            heading = (heading + distance) % 360
            # print(direction, distance, ': new heading :', heading)
            continue
        elif direction == 'L':
            heading = (heading - distance) % 360
            # print(direction, distance, ': new heading :', heading)
            continue

        if direction == 'F':
            direction = compass.get(heading)
        
        move = tuple(n*distance for n in compass.get(direction)[1])
        position = tuple(sum(x) for x in zip(move, position))
        # print('move:', move)
        # print('position:', position)
    
    return position

def followWaypointCourse(course, waypoint=(10,1), position=(0,0)):
    for step in course:
        direction = step[0]
        distance = int(step[1])
        # print('\ndirection:', direction)
        # print('distance:', distance)
        # print('heading:', heading)
        
        # move ship
        if direction == 'F':
            move = tuple(n*distance for n in waypoint)
            position = tuple(sum(x) for x in zip(move, position))
            # print('move:', move)
            # print('position:', position)
            continue

        # rotate waypoint
        if direction == 'R': 
            turns = distance / 90
            t = 0
            while t < turns:
                waypoint = (waypoint[1], waypoint[0] * -1)
                t += 1
        elif direction == 'L':
            turns = distance / 90
            t = 0
            while t < turns:
                waypoint = (waypoint[1] * -1, waypoint[0])
                t += 1
            pass
        else:   # no rotation move waypoint
            move = tuple(n*distance for n in compass.get(direction)[1])
            waypoint = tuple(sum(x) for x in zip(move, waypoint))
    
    return position

# course = [[x[0], x[1:].strip('\n')] for x in open('test1.txt')]
# course = [[x[0], x[1:].strip('\n')] for x in open('test2.txt')]
course = [[x[0], x[1:].strip('\n')] for x in open('navChart.txt')]
# print(course)

finalPosition = followCourse(course, compass.get('E')[0])
manhattanDistance = sum(abs(x) for x in finalPosition)
# print(finalPosition)
print('manhattan =>', manhattanDistance)

finalPosition = followWaypointCourse(course)
manhattanDistance2 = sum(abs(x) for x in finalPosition)
# print(finalPosition)
print('manhattan 2 =>', manhattanDistance2)
