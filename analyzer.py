# import os
import json
from Grammer import Grammer

os.system('clear')

Grammer = Grammer()

text = raw_input('What text would you like to validate: ')
print Grammer.checkStringForCorrectness(text)

# for x in range(10,0,-1):
#     print Grammer.importNGrams(x, 'books/the_new_hackers_dictionary.txt')
