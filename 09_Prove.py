# 09 Prove: Assignment Milestone
# Jaelee 

choice = 0
# list for shopping cart
cart = []

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
        price = int(input(f"What is the price of '{item}'? "))
        print(f"'{item}' has been added to the cart.")
        # add to cart list
        cart.append(item) # add price to append

    elif choice == 2:
        print('The contents of the shopping cart are:')
        ctr = 1
        for item in cart: # add price too #look up cse 111?!
            print(ctr + '.')
            print(item)
            ctr = ctr + 1

    elif choice == 3:
        remove = int(input('Which item would you like to remove? '))
        # add code to remove item

    elif choice == 4:
        # total the prices
        total = 0
        print(f'The total price of the items in the shopping cart is ${total}')

    else:
        print('Thank you. Goodbye.')
