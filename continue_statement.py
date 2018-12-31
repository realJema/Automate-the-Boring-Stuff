# using the continue statement 
# continues the execution of the loop
# moves to the next iteration of the loop

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue 
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break 
print('Acess granted.')