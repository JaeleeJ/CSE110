# 07 Prepare: Checkpoint
# Jaelee Hutchinson

# positive number
num = int(input('Please type a positive number: '))
while num < 0:
    print('Sorry, that is a negative number. Please try again.')
    num = int(input('Please type a positive number: '))

if num >= 0:
    print('The number is:', num)

# candies
print()
candy = str(input('May I have a piece of candy? '))
while candy.lower() != 'yes':
    candy = str(input('May I have a piece of candy? '))

if candy.lower() == 'yes':
    print('Thank you.')