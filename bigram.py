text = "The boy went to the store on a Friday afternoon"

trigram = {}

myArr = text.lower().strip().split()

size = len(myArr) - 2

for x in range(0, size):
    
    stuff = [myArr[x],myArr[x+1],myArr[x+2]]

    if '-'.join(stuff) in trigram:
        trigram['-'.join(stuff)] += 1
    else:
        trigram['-'.join(stuff)] = 1

print trigram