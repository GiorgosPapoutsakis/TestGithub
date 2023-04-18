import sys

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

