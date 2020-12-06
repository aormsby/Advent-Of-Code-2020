# pull group answers into list
def readGroupAnswers(filename):
    a = []
    with open(filename) as answers:
        a = answers.read().split('\n\n')
    for i in range(len(a)):
        a[i] = {'input' : a[i]}
    return a

# count num responders
# count unique answers
def countGroupAnswers(group):

    g = group.split('\n')
    groupSize = len(g)

    group = group.replace('\n','')
    ans = set(group)
    uniqueAnswers = len(ans)

    ans2 = [x for x in ans if group.count(x) == groupSize]
    sharedAnswers = len(ans2)

    return ('group', groupSize),('ors', uniqueAnswers),('ands', sharedAnswers)

# sum all answers across groups

### ----------

# groupAnswers = readGroupAnswers('test.txt')
groupAnswers = readGroupAnswers('groupAnswers.txt')
sum1 = 0
sum2 = 0
for i in range(len(groupAnswers)):
    # this seems dumb, but whatever. it works.
    groupAnswers[i].update(*[countGroupAnswers(groupAnswers[i]['input'])])
    sum1 += groupAnswers[i]['ors']
    sum2 += groupAnswers[i]['ands']

# print(groupAnswers)
print(sum1)
print(sum2)