# Ending a program early with sys.exit()

import sys 

while True:
    print('Tyep exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')