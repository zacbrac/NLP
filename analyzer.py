from os import listdir
from os.path import isfile, join
import json
from Grammer import Grammer

mypath = './books/'
book_filename = 'king_james.txt'

# Gets all books in books/ 
# onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

# for book in onlyfiles:


Grammer = Grammer()

# text = raw_input('What text would you like to validate: ')
# print Grammer.checkStringForCorrectness(text)

# 10 times to get 1-10grams for each book
# for x in range(10,0,-1):
#     print Grammer.importNGrams(x, mypath + book_filename)