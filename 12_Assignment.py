# 12 Prove: Assignment
# Jaelee Hutchinson

# open the file
open('life-expectancy.csv')

# user input for year of interest
yearInterest = str(input('Enter the year of interest: '))

# declare max and min variables
maxAge = 0
maxEntity = ''
maxYear = ''
minAge = 1000
minEntity = ''
minYear = ''

# declare variables for interest year
interestMaxAge = 0
interestMaxEntity = ''
interestMinAge = 1000
interestMinEntity = ''
avg = 0
total = 0
ctr = 1

# read contents
with open('life-expectancy.csv') as life:
    # skip the first line
    next(life)
    for line in life:
        # split between entity, year, and life expectancy
        x = line.split(',')
        entity = x[0]
        year = x[2]
        expectancy = float(x[3])

        # find highest and lowest values
        if expectancy > maxAge:
            maxAge = expectancy
            maxEntity = entity
            maxYear = year
            
        if expectancy < minAge:
            minAge = expectancy
            minEntity = entity
            minYear = year

        for x in year:
            if year == yearInterest:
                ctr += 1
                total += expectancy
                if expectancy > interestMaxAge:
                    interestMaxAge = expectancy
                    interestMaxEntity = entity
            
                if expectancy < interestMinAge:
                    interestMinAge = expectancy
                    interestMinEntity = entity
        avg = total / ctr

# print output
print(f'The overall max life expectancy is: {maxAge} from {maxEntity} in {maxYear}')
print(f'The overall min life expectancy is: {minAge} from {minEntity} in {minYear}')
print()
print(f'For the year {yearInterest}:')
print(f'The average life expectancy across all countries was {avg:.2f}')
print(f'The max life expectancy was in {interestMaxEntity} with {interestMaxAge}')
print(f'The min life expectancy was in {interestMinEntity} with {interestMinAge}')
