import pprint
import sys
from collections import deque

#A TROPOS: vazoume to weight entos tou adjacency list xrisimopoiwntas Tuples
#Ta adjacency lists twra entos twn listwn exoun TUPLES, oxi INTS
#Tuple: (Node,Weight)
def fillGraph(directed = True):
    g = {}
    filename = "graphs_data\weighted_graph3.txt"
    with open(filename) as input_file:
        for line in input_file:
            [n1, n2, w] = [ int(x) for x in line.split()]

            if n1 not in g: 
                g[n1] = []
            if n2 not in g:
                g[n2] = []
            g[n1].append((n2,w))
            if not directed:
                g[n1].append((n2,w))
    return g


#B TROPOS: ta adjacency lists menoun idia me ta apla graphs kai xrisimopoioume map(dicitionary) gia ta weights
def fillGraph_W_M(directed = True):
    g = {}
    weights = {} #key: tuple me to zeugari twn komvwn. value: to varos tou zeugariou
    filename = "graphs_data\weighted_graph4_negativeCycle.txt"
    
    with open(filename) as input_file:
        for line in input_file:
            [n1, n2, w] = [ int(x) for x in line.split()]

            if n1 not in g: 
                g[n1] = []
            if n2 not in g:
                g[n2] = []
            g[n1].append(n2)
            weights[(n1,n2)]= w
            if not directed:
                g[n2].append(n1)
                weights[(n2,n1)] = w
    return (g,weights)
        
#SOURCE & SINK
#Prosthetoume ston grafo Arxiko(Source/Pigi) kai Teliko(Sink/Xoani) komvo
#source: den einai pointed apo kanenan komvo, kanei point stous komvous pou den itan pointed
#.. ->noumero n(oi uparxontes einai 0-(n-1) )
#sink/xoani: einai pointed apo tous komvous pou den ekanan point kapou -> noumero n+1

#algorithmos
#vriskoume ta nodes pou EINAI POINTED apo alla nodes
#ta xrisimopoioume(allNodes-auta) gia na vroume ta nodes pou DEN EINAI POINTED apo alla nodes
#meta vriskoume ta nodes pou POINT NOWHERE
#telos prostetoume ta SOURCE and SINK NODES
def add_source_sink(g):
    to_nodes = { v for u in g.keys() for v in g[u] } #v: osoi komvoi emfanizontai ws geitones
    no_previous = g.keys() - to_nodes
    no_next = { u for u in g.keys() if len(g[u]) == 0 } #osoi exoun adeio adgagency list
    num_nodes = len(g.keys())
    source = num_nodes
    g[source] = [ u for u in no_previous] #oi geitones tou source einai osoi NoPointed #Weigh=0
    num_nodes += 1
    sink = num_nodes
    g[sink] = []
    for n in no_next: #osoi noPoint kanoun geitona ton sink #Weigh=0
        g[n].append(sink)
    return (source,sink)


#ALGORITHMOS KRISIMOTEROU MONOPATIOU(megalutero monopati)
#epistrefei 2 listes:
#pred: se kathe pos i, o komvos prin apo ton komvo i sto krisimo monopati
#dist: se kathe pos i, tin apostasi tou komvou i apo to source sto krisimo monopati
# -> arxikopoiountai me -1 kai xalarwnoun stous pragmatikous arithmous

#python
#get(k, default): epistrefei tin timi k apo to dictionary ean uparxei, alliws epistrefei default

#Θ(V+E)
def critical_path(g,w):
    source, sink = add_source_sink(g)
    n = len(g.keys())
    pred = [-1]*n
    dist = [-1]*n
    dist[source] = 0

    tsorted = topologicalSort(g)
    print("tsorted",tsorted)    
    for u in tsorted:
        for v in g[u]:
            if dist[v] < dist[u] + w.get((u,v),0):
                dist[v] = dist[u] + w.get((u, v), 0)
                pred[v] = u
    return (pred,dist)

def getPath(pred, t=None):
    path=[]
    if t== None:
        t = len(pred)-1 #thesi tou teleutaiou Node
    while t!=-1:
        path.insert(0,t)
        t=pred[t]
    return path


##########
#TopologicalSort -> unweighted
def topologicalSort(g):
    visited = [False] * len(g)
    sortedList = []
    for i in g:
        if visited[i]==False:
            dfsTS(g,i,visited,sortedList)
    return sortedList
def dfsTS(g,startNode,visited,sortedLista):
    visited[startNode] = True
    for u in g[startNode]:
        if visited[u]==False:
            dfsTS(g,u,visited,sortedLista)
    sortedLista.insert(0,startNode)
###########


#DIJKSTRA-O(V^2): vriskei to sudomotero monopati apo enan komvo pros OLOUS komvous tou grafou
#me OURA PROTERAIOTITAS = idia lista me tin dist: pairnw min apostasi -> kanw douleia -> tin kanw oo(oxi ksanaepileksw)
#den leitourgei me ARNITIKA WEIGHTS, oute an eksupna ta kanw ola thetika

#idea: epilegoume kathe fora ton komvo me tin mikroteri apostasi(greedy)
#ALGORITHMOS
#arxikopoiw, dist[]=oo,pred[]=-1,dist[source]=0
#vazw olous tou komvous stin Oura Proteraiotitas
#epanalamvanw mexri na adeiasei i oura proteraiotitas
    #vgazw ton komvo me tin mikroteri apostasi
    #elegxw tous geitones tou kai xalarwnw 
    #enimerwnw tin oura prwteraiotitas me tis nees apostasis

#python
MAX_INT = sys.maxsize #antoistoixo tou oo
#mylist.index((min(a)) #epistrefei to mikrotero stoixeio tis listas(pio grigora apto na kaname kanonika anazitisi)

def dijkstra(g,w,start_node):
    #arxikopoiw - O(V)
    n = len(g)
    dist = [MAX_INT] * n
    dist[start_node] = 0
    pred = [-1] * n
    pq = dist[:] #priority queue
    elemenets_in_pq = n

    while elemenets_in_pq != 0:
        u = pq.index(min(pq)) #O(V^2)
        pq[u] = MAX_INT #den thelw na epilextei ksana -> oti xrisimopoieitai paei oo(den kanei bros pisw o algorithmos)
        elemenets_in_pq -= 1

        #xalarwnw tous geitones tou u
        for v in g[u]: #O(E)
            if dist[u] + w.get((u,v),0) < dist[v]:
                dist[v] = dist[u] + w.get((u,v),0)
                pred[v] = u
                pq[v] = dist[v]

    return (dist,pred)
    #O(V + V^2 + E) = O(V^2)


#BELMAN-FORD -O(VE)(xeirotero apo dijkstra): vriskei to sudomotero monopati apo enan komvo pros OLOUS komvous tou grafou
#leitourgei me Arnitika Weights

#idea: sti xeiroteri periptwsi, to sudomotero monopati tha exei N-1 sundeseis
#ALGORITHMOS
#arxikopoiw, dist[]=oo,pred[]=-1,dist[source]=0
#epanalanvanw n-1 fores(n=arithmos komvwn):
    #gia kathe komvo u pairnw olous tous geitones tou
    #ean borw(exw prosvasi apo start se u) xalarwnw, diaforetika agnow

def bellman_ford(g,w,start):
    #arxikopoiw O(V)
    n = len(g) 
    pred = [-1] * n
    dist = [MAX_INT] * n
    dist[start] = 0
    
    #ousia
    for i in range(n-1): #V-1
        for u in g: #gia kathe komvo, pairnw tous geitones tou O(V*E)
            for v in g[u]:
                if dist[u]!=MAX_INT and dist[u] + w.get((u,v),0) < dist[v]: #ean o komvos v einai prosvasimos(kserw dist[u]), xalarwnw
                    dist[v] = dist[u] + w.get((u,v),0)
                    pred[v] = u

    return (dist,pred)


#gia na min diatrexoume kathe fora olous tous komvous, akoma kai autous pou den boroume na ftasoume ekeini ti stigmi
#oura(FIFO): tha periexei tous komvous pou xalarwsan stin teleutaia epanalipsi
#anti na epanalamvanoume N-1 fores, epanalamvanoume mexri nia adiasei i oura
def bellman_ford2(g,w,start):
    #arxikopoiw
    n = len(g)
    pred = [-1] * n
    dist = [MAX_INT] * n
    dist[start] = 0

    #arxikopoioume tin oura mono me ton start komvo
    queue = deque()
    in_queue = [False] * n
    in_queue[start] = True
    queue.appendleft(start)

    while len(queue)!=0:
        c = queue.pop()
        in_queue[c] = False
        
        for v in g[c]:
            if dist[c] + w.get((c,v),0) < dist[v]:
                dist[v] = dist[c] + w.get((c,v),0)
                pred[v] = c
                if in_queue[v] == False:
                    queue.appendleft(v)
                    in_queue[v] = True
        
    return (dist,pred) 

#entopizoume arnitikous kuklous mesw mias timis frouro(sentinel)
#ama o sentinel ginei pop apo tin oura ton ksanapetaw mesa -> ean auto ginei panw apo n-1 fores(max epanalipseis-arxikos algorithmos): arnitikos kuklos
def bellman_ford3(g,w,start):
    #arxikopoiw
    n = len(g)
    pred = [-1] * n
    dist = [MAX_INT] * n
    dist[start] = 0

    #arxikopoioume tin oura mono me ton start komvo
    queue = deque()
    in_queue = [False] * n
    in_queue[start] = True
    queue.appendleft(start)

    #arxikopoiw ton sentinel kai ton vazw stin oura
    sentinel = n #otidipote timi thelw arkei na min einai komvos
    queue.appendleft(sentinel)
    iterations = 1 #ama oi epanalipseis pane panw apo n-1, tote pesame se kuklo

    while len(queue)!=1 and iterations < n:
        c = queue.pop()
        if c == sentinel:
            iterations += 1
            queue.appendleft(sentinel)
        else:
            in_queue[c] = False
            for v in g[c]:
                if dist[c] + w.get((c,v),0) < dist[v]:
                    dist[v] = dist[c] + w.get((c,v),0)
                    pred[v] = c
                    if in_queue[v] == False:
                        queue.appendleft(v)
                        in_queue[v] = True

    print(iterations)
    return (pred,dist,iterations < n)



g,w = fillGraph_W_M()
dist,pred,cycle = bellman_ford3(g,w,0)
#dist,pred = bellman_ford2(g,w,0)
print("pred:",pred)
print("dist:", dist)
print("cycle:",not cycle)
#print(getPath(pred, 3),dist[3])

#Floyd-Marsal