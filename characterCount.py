"""
Name: characterCount.py,
Description: exploring the setdefault() method.
Page: 110,
Date: 4/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


print(count)
# program to count number of occurences of characters

pprint.pprint(count)
