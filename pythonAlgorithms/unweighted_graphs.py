import pprint
from collections import deque

#begginerGraph,DFS,BFS,TopologicalSort

g = {}

def fillGraph():
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

#paw oso pio vathia ginetai gia kathe komvo mexri na min exei alla paidia
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
#paw stous komvous pou apaixoun apostasi enosKomvou apo ton arxiko, meta stous komvous me apostasi duoKomvwn
#..apo ton arxiko kai sunexizw mexri na teleiwsoun oi komvoi 
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


##################
#topologiki taksinomisi-ginetai se akuklous kateuthinomenous grafous, den einai monadiki ana grafo
#taksinomei tous komvous wste na boroume na tous episkeftoume me ti seira, enw PANTA o o komvos pou vriskomaste 
#.. einai prin apo tous upoloipous komvous stous opoious deixnei

#ginetai me vasi tin DFS: 
#ftanoume sto teleutaio paidi tou kathe komvou anadromika kai to vazoume PANTA stin prwti thesi sti lista

#den boroume na episkeftoume panta olous tous komvous ksekinontas px apo enan komvo(kateuthinomenos-sunistwses)
#Θ(|V|+|E|)
def topologicalSort():
    g = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4],
    4: [2, 5],
    5: [],
    6: [3, 7],
    7: [],
    8: [6, 9],
    9: [7],
    10: []
    }

    #arxikopoiisi
    orderedVisits = [] #APOTELESMA: i teliki seira me tin opoia taksinomountai oi komvoi
    visited = [False] * len(g)

    #ousia algorithmou
    for node_I in g: #gia na episkeftoume sigoura olous tous komvous(mi prosvasimous apo 1 sugkekrimeno)
        if not visited[node_I]:
            dfs_T_S(g,node_I,orderedVisits,visited)
    
    #apotelesma
    return orderedVisits

def dfs_T_S(g, node, list_visits, visited):
        visited[node]=True
        for v in g[node]:
            if not visited[v]:
                dfs_T_S(g,v,list_visits,visited)
        
        list_visits.insert(0, node)

        #gia PIO EFFICIENT(python): anti insert, kanoume append kai sto telos reverse tin lista

print(topologicalSort())



