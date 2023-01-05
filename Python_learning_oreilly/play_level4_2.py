#Use a Python Module

# The Python module is simply a collection of plug and play functionalities to solve a specific problem. 
# And there are so many Python modules
#  I'm going to simply do import os,  
# The os module is simply going to give you some new functionality to interact with the os, and for example, to create files, remove files, create directories, etc. 

import os

if os.path.exists('file_test.txt'):
    os.remove('file_test.txt')
    print('removed')
else:
    print('Didnt exist')


# instead of using import os, okay, which is going to import all the os module, you can import specific functions. 
# So if you want to do that, you can do from os import, for example, remove. 
# This is going to import the remove function from the os module. And you can do from os.path import exist. 
# Removing file with diff. method of importing function from os

from os import remove
from os.path import exists

file_name = 'file_test.txt'

if exists('file_name.txt'):
    remove('file_name.txt')
    print('removed diff')
else:
    print('didnt exists')

#Below is example of using my own created python module
#Importing my own created custom pyhton module

import crete_python_module

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))


print(str(number1) + '+' + str(number2) + '=' + str(crete_python_module.add_2_nnumbers(number1, number2)))




