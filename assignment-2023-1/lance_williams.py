import sys

method = sys.argv[2]
if method == "simple":
    print('OK')

allNumbers = []
with open(sys.argv[1]) as myfile:
    for line in myfile:
        allNumbers.extend((int(number) for number in line.split(' ')))
        print(allNumbers)
    
    
    
    print(allNumbers)

