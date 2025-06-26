# 04 Prove: Assignment - Meal Price Calculator
# Jaelee Hutchinson

# prompt user
childPrice = float(input("What is the price of a child's meal? "))
adultPrice = float(input("What is the price of an adult's meal? "))
drinkPrice = float(input('What is the price of a drink? '))
child = int(input('How many children are there? '))
adult = int(input('How many adults are there? '))
drink = int(input('How many drinks will be bought? '))
taxRate = float(input('What is the sales tax rate? '))
tip = float(input('How much percentage will you tip? '))

# calcuate
subtotal = (childPrice * child) + (adultPrice * adult) + (drinkPrice * drink)
salesTax = 0.01 * taxRate * subtotal
tipTotal = 0.01 * tip * subtotal
total = subtotal + salesTax + tipTotal

# print totals
print()
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${salesTax:.2f}')
print(f'Tip: ${tipTotal:.2f}')
print(f'Total: ${total:.2f}')

# calculate change based on payment amount
print()
payment = float(input('What is the payment amount? '))
change = payment - total
print(f'Change: ${change:.2f}')
