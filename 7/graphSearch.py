import re

# read rules into list one line at a time
def readRules(filename):
    lines = []
    with open(filename) as ruleset:
        for i in ruleset:
            lines.append(i.strip('\n'))

    return lines

# arrange rule in graph structure
def createRulesGraph(ruleset):
    rGraph = {}
    for r in ruleset:
        colors = [c[::-1] for c in re.findall(r'(\d+)?\s?(\w+\s\w+)\sbag', r) if 'no other' not in c]
        rGraph[colors[0][0]] = {k:int(v) for (k,v) in colors if v != ''}
    return rGraph

# reverse depth first search of graph starting with inner most bag
def reverseDepthFirstSearch(graph, start, visited=set()):
    visited.add(start)
    # print(visited)

    containers = set([k for k in graph if start in graph[k].keys()])
    # print(containers)
    for next in containers - visited:
        # print(next)
        reverseDepthFirstSearch(graph, next, visited)

    return visited

# forward depth first search starting with outermost bag
# not tracking visited in order to go down each different path
def forwardDepthFirstSearch(graph, start):
    innerBags = sum(graph[start].values())

    for next in graph[start]:
        # print(next)
        innerBags += forwardDepthFirstSearch(graph, next) * graph[start][next]

    # print(innerBags)
    return innerBags

####################

# rules = readRules('test.txt')
# rules = readRules('test2.txt')
# rules = readRules('test3.txt')
rules = readRules('rules.txt')

graph = createRulesGraph(rules)
startBag = 'shiny gold'

# for k,v in zip(graph.keys(), graph.values()):
#     print(k,':',v)

outerBags = reverseDepthFirstSearch(graph, 'shiny gold') - set([startBag])
# print(outerBags)
print('outer bags:',len(outerBags))

# innerBags = forwardDepthFirstSearch(graph, 'dark red')
innerBags = forwardDepthFirstSearch(graph, 'shiny gold')
print('inner bags:', innerBags)