# Second magic8Ball2.py

import random 

message = [
    'It is certain',
    'Its is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(message[random.randint(0, len(message) - 1)])