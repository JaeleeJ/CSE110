# 05 Prepare: Checkpoint
# Jaelee Hutchinson

# user input
firstNum = int(input('What is the first number? '))
secondNum = int(input('What is the second number? '))

# conditional statements
if firstNum > secondNum:
    print('The first number is greater')
else:
    print('The first number is not greater')

if firstNum == secondNum:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if firstNum < secondNum:
    print('The second number is greater')
else:
    print('The second number is not greater')

# conditional for animal
print()
animal = str(input('What is your favorite animal? '))

if animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')
