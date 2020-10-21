inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(bag):
    sum = 0
    for i, k in bag.items():
        print(k, i)
        sum += k
    print('Total number of items: ', sum)


displayInventory(inventory)
print('--------------')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventor, addedItems):
    for i in addedItems:
        inventor.setdefault(i, 0)
        inventor[i] += 1


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
