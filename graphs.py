import pprint
from collections import deque

g = {}
input_filename = "example_1.txt"

with open(input_filename) as file:
    for line in file:
        nodes = [int(x) for x in line.split()]

        if len(nodes)!=2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])


#stack: FILO
def dfs(g,start):
    visited = [False]*len(g)
    inStack = [False]*len(g) #Gia na min vazw stin stack tautoxrona polles fores ton idio komvo, leitourgei kai xwris auto(+xronos -mnimi)
    stack = []
    stack.append(start)
    inStack[start]=True

    while not(len(stack)==0):
        node=stack.pop()
        print("Visiting", node)
        visited[node]=True
        inStack[node]=False

        for v in g[node]:
            if not visited[v] and not inStack[v]:
                stack.append(v)
                inStack[v]=True

    return visited

##################

visited2 = [False]*len(g)
def dfs2(g,start):
    print("Visiting", start)
    visited2[start]=True
    for v in g[start]:
        if not visited2[v]:
            dfs2(g,v)

##################
#queue : FIFO

def bfs(g,start):
    visited = [False]*len(g)
    inqueue = [False]*len(g) #Gia na min vazw stin oura tautoxrona polles fores ton idio komvo
    q = deque()
    q.appendleft(start)

    while not (len(q)==0):
        node=q.pop()
        print("Visiting", node)
        visited[node]=True
        inqueue[node]=False

        for v in g[node]:
            if not visited[v] and not inqueue[v]:
                q.appendleft(v)
                inqueue[v]=True

    return visited


pprint.pprint(g)

