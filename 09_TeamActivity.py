# 09 Teach: Team Activity
# Jaelee 

# user input
numbers = []
print('Enter a list of numbers, type 0 when finished.')
num = -1
while num != 0:
    num = int(input('Enter number: '))
    if num != 0:
        numbers.append(num)

# sum numbers
sum = 0
ctr = 0
for x in numbers:
    sum += x
    ctr = ctr + 1

# average numbers using sum and ctr
avg = sum / ctr

# find largest number in list
largest = 0
for x in numbers:
    if x > largest:
        largest = x

# print output
print()
print(f'The sum is: {sum}')
print(f'The average is: {avg}')
print(f'The largest number is: {largest}')
