# 13 Teach: Team Activity
# Jaelee 

import math

# function for area of a square
def compute_area_square(side):
    return side * side

# function for area of a rectangle
def compute_area_rectangle(length, width):
    return length * width

# function for area of a circle
def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ''
while shape != 'quit':
    shape = str(input('What shape would you like? '))
    # area of square
    if shape == 'square':
        side = float(input('Enter side length: '))
        area = compute_area_square(side)
        print(f'The area of {shape} is {area}')
    # area of a rectangle
    elif shape == 'rectangle':
        length = float(input('Enter length: '))
        width = float(input('Enter width: '))
        area = compute_area_rectangle(length, width)
        print(f'The area of {shape} is {area}')
    elif shape == 'circle':
        radius = float(input('Enter radius: '))
        area = compute_area_circle(radius)
        print(f'The area of {shape} is {area}')
