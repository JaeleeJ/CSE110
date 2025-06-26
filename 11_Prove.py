# 11 Prove: Assignment Milestone
# Jaelee 

# open the file
open('life-expectancy.csv')

# read contents
with open('life-expectancy.csv') as life:
    for line in life:
        # split between entity, year, and life expectancy
        x = line.split(',')
        entity = x[0]
        year = x[2]
        expectancy = float(x[3])

        # find highest and lowest values
        largest = 0
        smallest = 100
        for x in range(len(expectancy)): 
            if x > largest:
                largest = x
            
            if x < smallest:
                smallest = x

        
