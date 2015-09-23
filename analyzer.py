from os import listdir
from os.path import isfile, join
import json
from Grammer import Grammer

mypath = './books/'

# Gets all books in books/
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

Grammer = Grammer()

# text = raw_input('What text would you like to validate: ')
# print Grammer.checkStringForCorrectness(text)

# 10 times to get 1-10grams for each book
for book in onlyfiles:
    for x in range(10,0,-1):
        print Grammer.importNGrams(x, mypath + book)