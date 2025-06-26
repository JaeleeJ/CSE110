# 10 Prepare: Checkpoint
# Jaelee Hutchinson

print('Please enter the items of the shopping list (type: quit to finish):')

shoppingList = []
item = ''
while item != 'quit':
    item = str(input('Item: '))
    if item != 'quit':
        shoppingList.append(item)

if item == 'quit':
    print('The shopping list is:')
    for x in range(len(shoppingList)):
        print(shoppingList[x])

    #finish here with indexes and changes


