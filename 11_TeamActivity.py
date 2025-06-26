# 11 Teach: Team Activity
# Jaelee

# open file
open('hr_system.txt')

# read contents
with open('hr_system.txt') as hr_file:
    for line in hr_file:
        # split line for name and job
        clean_line = line.strip()
        x = line.split(' ')
        name = x[0]
        id = x[1]
        job = x[2]
        salary = float(x[3])
        print(f'{name} (ID: {id}), {job} - ${salary:.2f}')
