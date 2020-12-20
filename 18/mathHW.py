def collectExpressions(filename):
    return [[splitEx for splitEx in ex.strip('\n') if splitEx != ' ']
        for ex in open(filename).readlines()]

# input expression chunk, calc left to right, return value
def evalChunkLTR(chunk):    
    if len(chunk) > 1:
        n1 = chunk[0]
        n2 = chunk[2]
        op = chunk[1]
        # print(n1, op, n2)

        if op == '*':
            chunk = [int(n1) * int(n2)] + chunk[3:]
        if op == '+':
            chunk = [int(n1) + int(n2)] + chunk[3:]

        chunk = evalChunkLTR(chunk)

    return chunk

# # find all parentheses sets recursively
# def getParenSets(e, lastI=0, iList=None):
#     if iList is None:
#         iList = [e.index(x) for x in e if x == '(' or x == ')']
#         print(iList)
#     ps = []
#     lastP = ''

#     for i in range(lastI, len(e)):
#         if e[i] == '(':
#             if e[i] == lastP:
#                 ps.append(getParenSets(e, i))

#             else:
#                 ps.append(i)
#                 lastP = e[i]        

#         elif e[i] == ')':
#             lastP = e[i]
#             ps.append(i)

#     print(ps)
#     return ps


# eval parens inside to out, replace chunks with with ouput
def evalParenIn2Out(ex):
    # no parentheses, early out
    if '(' not in ex and ')' not in ex:
        return ex

    # init pos
    pPos = [-1, -1]

    for i in range(len(ex)):
        if ex[i] == '(':
            pPos[0] = i
        elif ex[i] == ')':
            pPos[1] = i
            break

    # print(*ex)
    # print('ppos:', *pPos)
    if -1 not in pPos:
        ex = ex[:pPos[0]] + [*evalChunkLTR(ex[pPos[0]+1:pPos[1]])] + ex[pPos[1]+1:]
        # print(*ex)
        # print()
        ex = evalParenIn2Out(ex)

    return ex

# evaluate entire expression in steps
# 1 - parentheses replacements (calculated inners)
# 2 - full ltr expression eval
def evalExpression(expr):
    # print(expr)
    expr = evalParenIn2Out(expr)
    output = evalChunkLTR(expr)[0]

    return output

# collect and sum expression values
def sumExpressionResults(exprList):
    sum = 0
    for e in exprList:
        sum += evalExpression(e)
    return sum

#####

# expressions = collectExpressions('test1.txt')
expressions = collectExpressions('expressions.txt')
# for e in expressions:
#     print(e)

sumExpressions = sumExpressionResults(expressions)
print('sum expressions:', sumExpressions)
