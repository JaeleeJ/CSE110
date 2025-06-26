# 08 Teach: Team Activity
# Jaelee Hutchinson

# user input
num = int(input('How many columns and rows do you want in your multiplication table? '))

# loop to output table
for x in range(1, num + 1):
    for y in range(1, num + 1):
        print(x * y, end=' ')
    print()
