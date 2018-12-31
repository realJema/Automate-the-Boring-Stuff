#! python3
# pw.py - An insecure password locker program.

"""
Name: pw.py,
Description: password m anage project.
Page: 136,
Date: 5/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    print('Password for ' + account + ' present')
else:
    print('There is no account name ' + account)
