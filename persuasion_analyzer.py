from subprocess import call

def getNGrams(n,inputFile):
    
    text = open(inputFile, 'r')

    count = len(open(inputFile, 'r').read().lower().strip().split())

    grams = {}

    for line in text: 
        
        myArr = line.lower().strip().split()
        
        size = len(myArr) - ( n - 1 )

        for x in range(0, size):
            
            gram = []

            for y in range(0,n):
                gram.append(myArr[x + y])

            if ' '.join(gram) in grams:
                grams[' '.join(gram)] += 1
            else:
                grams[' '.join(gram)] = 1

    return grams

trigrams = getNGrams(8,'persuasion.txt')

for x in trigrams:
    
    print str(x) + ': ' + str(trigrams[x])
