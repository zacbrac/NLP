import json

class Grammer(object):
    """Grammer creates N-Grams for building language models as well as checks incoming sentences for correctness"""

    def getGramFile(self, n):

        return 'ngrams/' + str(n) + '.json'

    def getNGramsFromFile(self, n, inputFile):
        
        text = open(inputFile, 'r')

        count = len(open(inputFile, 'r').read().lower().strip().split())

        grams = {}
        grams2 = {}

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

                if gram[0] in grams2:
                    grams2[gram[0]] += 1
                else: 
                    grams2[gram[0]] = 1

        text.close()

        return [grams, grams2]

    def importNGrams(self, n, inputFile):
        
        text = open(inputFile, 'r')

        count = len(open(inputFile, 'r').read().lower().strip().split())

        gramFile = self.getGramFile(n)

        with open(gramFile) as file_data:
            grams = json.load(file_data)

        for line in text: 
            
            myArr = line.lower().strip().split()
            
            size = len(myArr) - ( n - 1 )

            for x in range(0, size):
                
                gram = []

                for y in range(0,n):
                    gram.append(myArr[x + y])

                if ' '.join(gram) in grams[0]:
                    grams[0][' '.join(gram)] += 1
                else:
                    grams[0][' '.join(gram)] = 1

                if gram[0] in grams[1]:
                    grams[1][gram[0]] += 1
                else: 
                    grams[1][gram[0]] = 1

        text.close()

        json.dump(grams, open(gramFile, 'w'))


    def checkStringForCorrectness(self, myString):

        sentence_to_check = myString.lower().split()

        gramSize = len(sentence_to_check)

        gramFile = self.getGramFile(gramSize)

        with open(gramFile) as file_data:
            grams = json.load(file_data)

        try:
            message = str(float(grams[0][' '.join(sentence_to_check)]) / float(grams[1][sentence_to_check[0]])) + ' likelihood of correctness (based on test set)'
        
        except Exception, e:
           
            print "Owch, I've never seen that phrase before, I believe it's incorrect."
            s = raw_input('What do you think? (yes: valid, no: invalid): ')
           
            if s == 'yes':
                if ' '.join(sentence_to_check) in grams[0]:
                    grams[0][' '.join(sentence_to_check)] += 1
                else:
                    grams[0][' '.join(sentence_to_check)] = .01

                if sentence_to_check[0] in grams[1]:
                    grams[1][sentence_to_check[0]] += 1
                else: 
                    grams[1][sentence_to_check[0]] = .01

                json.dump(grams, open(gramFile, 'w'))

                message = str(float(grams[0][' '.join(sentence_to_check)]) / float(grams[1][sentence_to_check[0]])) + ' likelihood of correctness (based on test set)'

            else:
                message = "Ok, I won't add that to my library then."

        finally:
            return message
