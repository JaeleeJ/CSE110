# 05 Teach: Team Activity
# Jaelee 

# user input
gradeNum = int(input('Enter a grade percentage: '))

# conditional statements for letter grade
if gradeNum >= 90:
    gradeLetter = 'A'
elif gradeNum >= 80:
    gradeLetter = 'B'
elif gradeNum >= 70:
    gradeLetter = 'C'
elif gradeNum >= 60:
    gradeLetter = 'D'
else:
    gradeLetter = 'F'

# get + or -
gradeMod = gradeNum % 10

if gradeMod >= 7:
    gradeSymbol = '+'
    if gradeLetter == 'A' or gradeLetter == 'F':
        gradeSymbol = ''
elif gradeMod < 3:
    gradeSymbol = '-'
    if gradeLetter == 'F':
        gradeSymbol = ''
else:
    gradeSymbol = ''

#print letter grade
print()
print(f'Your letter grade is {gradeLetter + gradeSymbol}')

# conditional if passed the course
if gradeNum >= 70:
    print('Congratulations! You passed the course!')
else:
    print('Sorry, you did not pass... Study harder!')


