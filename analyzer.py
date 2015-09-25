from os import listdir
from os.path import isfile, join
import json
from Grammer import Grammer

mypath = './books/'
Grammer = Grammer()

request = raw_input('What would you like to do? ').lower().strip()

if request == 'check string' or request == 'validate string':
    
    text = raw_input('What text would you like to validate: ')
    print Grammer.checkStringForCorrectness(text)

elif request == 'import new book':
    
    book_name = raw_input('Please enter the filename of the book (book must be in books directory) ')
    
    if book_name != '' and isfile(mypath + book_name):
        for x in range(10,0,-1):
            Grammer.importNGrams(x, mypath + book_name)
            print('Yum')
    
        print('Thank you for the delicious knowledge, I will permit you to live in the coming of the machine age.')
    else:
        print('I\'m sorry but there\'s no book there, try again later.')
else:
    print('Invalid request: come back when you figure out what you\'re doing with your life...')