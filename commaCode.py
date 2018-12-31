"""
Name: commaCode.py
Description: write a function that takes a list value as an argument and returns a string with all the items separtated by a comma and a space, with "and" insert before the last item.
Page: 102
Date: 3/12/18
Author: realJema
Book: Automate the Boring stuff with python 2015
"""

# Variable
spam = ['apples', 'bananas', 'tofu', 'cats']

# Function
def formatIt(theList):
    result = ''
    theList[-2] = 'and' # adds  "and" before last word
    for i in theList: # goes through each word in list
        result = result + i
        if i in theList[-2:]: # doesn't put a comma for last two elements
            result = result + " "
        else:
            result = result + ", "

    print(result)

# main
formatIt(spam)
