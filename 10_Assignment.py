# 10 Prove: Assignment
# Jaelee 

choice = 0
# list for shopping cart
cart = []
price = []

print('Welcome to the Shopping Cart Program!')
# loop menu
while choice != 5:
    # print menu
    print()
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    #   user input from menu
    choice = int(input('Please enter an action: '))

    # print user choice
    if choice == 1:
        item = str(input('What item would you like to add? '))
        cost = float(input(f"What is the price of '{item}'? "))
        # add to cart list
        cart.append(item) 
        # add price to list
        price.append(cost)
        print(f"'{item}' has been added to the cart.")

    elif choice == 2:
        print('The contents of the shopping cart are:')
        ctr = 1
        for x in range(len(cart)): 
            print(f'{ctr}. {cart[x]} - ${price[x]:.2f}')
            ctr += 1
            

    elif choice == 3:
        remove = int(input('Which item would you like to remove? '))
        # remove item from both lists
        remove = remove - 1
        cart.pop(remove)
        price.pop(remove)
        print('Item removed.')

    elif choice == 4:
        total = 0
        # total prices in the cart
        for x in price:
            total += x

        print(f'The total price of the items in the shopping cart is ${total:.2f}')

    else:
        print('Thank you. Goodbye.')
