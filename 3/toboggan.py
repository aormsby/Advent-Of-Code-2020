from functools import reduce

def readMap():
    mapArr = []
    with open("map.txt") as map:
        mapArr = map.read().splitlines()
    return mapArr

def getRoute(map, xT, yT):
    route = []
    x,y = 0,0
    end = len(map[0])

    while y < len(map):
        if x >= end:
            x -= end
        
        route.append(map[y][x]);

        x += xT
        y += yT

    return route

def countTrees(route, tree):
    return route.count(tree)

map = readMap()
route = getRoute(map, 3, 1)
trees = countTrees(route, '#')

print (trees)

routeSet = [[1,1],[3,1],[5,1],[7,1],[1,2]]
routesTrees = []
for r in routeSet:
    routesTrees.append(countTrees(getRoute(map, r[0], r[1]), '#'));
productTrees = reduce((lambda x,y: x * y), routesTrees)

print (productTrees)