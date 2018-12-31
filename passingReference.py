"""
Name: passingReference.py
Description: exploring the intricases of references between list and tuples
Date: 3/12/18
Author: realJema
"""

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # the original spam is modified since both variable (span and someParameter) have the reference to the same list
