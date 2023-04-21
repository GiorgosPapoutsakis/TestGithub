import sys
import time

def read():
    method = sys.argv[2]
    if method == "simple":
        print('OK')

    #DIAVAZW TA NOUMERA APTO TXT KAI TA VAZW SE MIA LISTA allNumbers
    allNumbers = []
    with open(sys.argv[1]) as myfile:
        for line in myfile:
            allNumbers.extend((int(number) for number in line.split(' ')))
    
    print(allNumbers)
    allNumbers.sort()
    print(allNumbers)

    apost = []
    for x in allNumbers:
        katheApost = []
        for n in allNumbers:
            if x!=n :
             katheApost.append(abs(x-n))
    apost.append(min(katheApost))
    
    print(apost)


#ME ANADROMI 
#Exw tupous gia d(s,t) kai d([s,t],v) opou s,t aploi arithmoi (oxi lista)
#Isxuei d(v,[s,t]) = d([s,t],v) epeidi praktika einai apostasi simeiwn
#An exw lista u = [s,...,t] tin spaw sunexeia se ([s,...] kai t) mexri na exei megethos 2 opou borw na upologisw tin apostasi apo ton tupo
def distance(u, v) -> int:
    if type(u) == int and type(v)==int:
        return abs(u-v)

    if type(u) == list:   
        if len(u) == 2:
            s, t = u[0], u[1]
            return 1/2 * distance(s, v) + 1/2 * distance(t, v) - 1/2 * abs( distance(s, v) - distance(t, v))
        else:
            *newS, newT = u #UNPACKING: spaw tin lista se (olaTaStoixeiaEktosTeleutaiou) kai (Teleutaio Stoixeio)
            return 1/2 * distance(newS, v) + 1/2 * distance(newT, v) - 1/2 * abs( distance(newS, v) - distance(newT, v))

    if type(u) == int and type(v)==list:
        return distance(v,u)


#a = [200,2,3,4]
#b = [35,20,22,28]
#print(distance(a,b))

def start2():
    mylist = [7, 10, 4, 20, 2, 25, 19, 6, 12, 1]
    mylist.sort()
    print(mylist)

    s = "simple"
    c = "complete"
    a = "average"
    w = "word"

    while(len(mylist)>1):
        temp = []
        min, pairPos = dis(mylist[0], mylist[1], w), [0,1]
       
        #VRISKW TO MIN APO OLA TA PITHANA ZEUGARIA KAI TIS THESEIS POU VRISKONTAI STIN LISTA
        #UPOLOGIZW TA IDIA ZEUGARIA PERISSOTERES APO 1 FORES = XANW XRONO
        for indexI, i in enumerate(mylist):
            for indexJ, j in enumerate(mylist):
               if indexI != indexJ and dis(i,j,w) < min:
                  min, pairPos = dis(i,j,w), [indexI, indexJ]

        #FTIAXNW LISTA TEMP ME TO SUGXONEUMENO ZEUGARI
        #EAN TOULAXISTON ENA APTA 2 MERI ITAN LISTA, TA SUNENWNW SE MIA ENNIA LISTA
        if type(mylist[pairPos[0]]) == list:
            for k in mylist[pairPos[0]]:
                temp.append(k)
        if type(mylist[pairPos[1]]) == list:
            for k in mylist[pairPos[1]]:
                temp.append(k)
        if type(mylist[pairPos[0]]) == int:
            temp.append(mylist[pairPos[0]])
        if type(mylist[pairPos[1]]) == int:
            temp.append(mylist[pairPos[1]])
        temp.sort()

        print("answer: ", mylist[pairPos[0]], mylist[pairPos[1]], min, len(temp))

        #PROSTHETW TIN LISTA TEMP KAI AFAIRW TO ZEUGARI APTIN ARXIKI LISTA
        mylist.append(temp)
        mylist.pop(pairPos[1])
        mylist.pop(pairPos[0])
        
  
    print(mylist)

#start2()

def coefficients(s,t,v,category):
    if type(s) == int:
        megethosS = 1
    else:
        megethosS = len(s)

    if type(t) == int:
        megethosT = 1
    else:
        megethosT = len(t)
    
    if type(v) == int:
        megethosV = 1
    else:
        megethosV = len(v)

    if category == "simple":
        return [1/2, 1/2, 0, -1/2]
    if category == "complete":
        return [1/2, 1/2, 0, 1/2]
    if category == "average":
        a1 = megethosS / (megethosS + megethosT)
        a2 = megethosT / (megethosS + megethosT)
        return [a1, a2, 0, 0]
    if category == "ward":
        a1 = (megethosS + megethosV) / (megethosS + megethosT + megethosV)
        a2 = (megethosT + megethosV) / (megethosS + megethosT + megethosV)
        b = (megethosV) / (megethosS + megethosT + megethosV)
        return [a1, a2, b, 0]

def dis(u,v,category):

    if type(u) == int and type(v)==int:
        return abs(u-v)

    if type(u) == list:   
        if len(u) == 2:
            s, t = u
        else:
            *s, t = u #UNPACKING: spaw tin lista se (olaTaStoixeiaEktosTeleutaiou) kai (Teleutaio Stoixeio)
        
        a1, a2, b, c  = coefficients(s, t, v, category)
        return a1*dis(s, v, category) + a2*dis(t, v, category) + b*dis(s,t,category) + c*abs( dis(s, v, category) - dis(t, v, category) )

    if type(u) == int and type(v)==list:
        return dis(v,u,category)
    


def calculateA1(x, y):
    if type(x) == int:
        megethosX = 1
    else:
        megethosX = len(x)
    
    if type(y) == int:
        megethosY = 1
    else:
        megethosY = len(y)
    
    return megethosX / (megethosX + megethosY) 
    


def calculateA2(x,y):
    if type(x) == int:
        megethosX = 1
    else:
        megethosX = len(x)
    
    if type(y) == int:
        megethosY = 1
    else:
        megethosY = len(y)
    
    return megethosY / (megethosX + megethosY)

def averDis(u,v):
    if type(u) == int and type(v)==int:
        return abs(u-v)
    
    if type(u) == list:   
        if len(u) == 2:
            s, t = u[0], u[1]
            a1 = calculateA1(s,t)
            a2 = calculateA2(s,t)
            return a1 * averDis(s, v) + a2 * averDis(t, v) 
        else:
            *newS, newT = u
            a1 = calculateA1(newS,newT)
            a2 = calculateA2(newS,newT)
            return a1 * averDis(newS, v) + a2 * averDis(newT, v) 

    if type(u) == int and type(v)==list:
        return averDis(v,u)
    
start = time.time()
start2()
end = time.time()
print("time:", end - start)
