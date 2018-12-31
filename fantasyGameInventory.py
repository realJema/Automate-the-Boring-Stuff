"""
Name: fantasyGameInventory.py,
Description: working with dictionaries.
Page: 120,
Date: 5/12/18,
Author: realJema,
Book: Automate the Boring stuff with python 2015,
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for item, qty in inventory.items():
        print(qty, item)
        total += qty
    print('Total number of items:', total)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) # sets default value to all elements(key)  which are not present in the dictionary
        inventory[item] += 1

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
