# 06 Teach: Team Activity
# Jaelee

# user input
age = int(input('What is the age of the first rider? '))
if age > 12 and age < 17:
    goldenPassport = str(input('Do you have a golden passport (yes/no)? '))
height = int(input('What s the height of the first rider (inches)? '))
second = str(input('Is there a second rider (yes/no)? '))
if second.lower() == 'yes':
    age2 = int(input('What is the age of the second rider? '))
    height2 = int(input('What is the height of the second rider (inches)? '))
else:
    age2 = 0
    height2 = 0

canRide = True
# check if they can ride
if height < 36 or height2 < 36:
    canRide == False
elif age < 18:
    if second.lower() == 'yes':
        if age2 > 18:
            canRide == True
        elif age2 < 18 and age2 > 12 and age > 12 and height >= 52 and height2 >= 52:
            canRide == True
        elif (age >= 14 and age2 >= 16) or (age >= 16 and age2 >= 14):
            canRide == True
        else:
            canRide == False
elif goldenPassport.lower() == 'yes':
        canRide == True
elif age > 18:
    if height < 62 and (second.lower() == 'no'): 
        canRide = False
    else: 
        canRide == True

# print if they can ride
if canRide == True:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')
