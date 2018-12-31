"""
Name: validateInput.py,
Description: repeatedly asks users for their age and password until they provide valid input.
Page: 130,
Date: 5/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new passworrd (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('Password can only have lettes and numbers.')
