# 07 Teach: Team Activity
# Jaelee Hutchinson

import random

num = random.randint(1,100)

print('What is the magic number?')
guess = 0
ctr = 0

while guess != num:
    guess = int(input('What is your guess? '))
    ctr += 1
    if guess > num:
        print('Lower')
    elif guess < num:
        print('Higher')
    else:
        print('You guessed it!')

print(f'You guessed {ctr} times.')