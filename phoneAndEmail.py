
"""
Name: phoneAndEmail.py,
Description: Finds phone numbers and email addresses on the clipboard.
Page: 166,
Date: 10/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""

import re

lorem = 'info@nostarch.commedia@nostarch.comacademic@nostarch.comhelp@nostarch.com'

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

results = emailRegex.findall(lorem)
print(results.group[1])
