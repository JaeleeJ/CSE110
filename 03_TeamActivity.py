# 03 Teach: Team Activity
# Jaelee 
import math

# area of square
squareSide = float(input('What is the length of a side of the square? '))
areaSq = squareSide ** 2
print('The area of the square is: ' + str(areaSq))
print()

# area of rectangle
rectLength = float(input('What is the length of the rectangle? '))
rectWidth = float(input('What is the width of the rectangle? '))
areaRect = rectLength * rectWidth
print('The area of the rectangle is: ' + str(areaRect))
print()

# area of circle
radius = float(input('What is the radius of the circle? '))
areaCirc = math.pi * (radius ** 2)
print('The area of the circle is: ' + str(areaCirc))
print()

# single length value
value = float(input('Enter a value: '))
areaSq2 = value ** 2
areaCirc2 = math.pi * (value ** 2)
volCube = value ** 3
volSph = (4/3) * math.pi * (value ** 3)
print('The area of a square is ' + str(areaSq2))
print('The area of a circle is ' + str(areaCirc2))
print('The volume of a cube is ' + str(volCube))
print('The volume of a sphere is ' + str(volSph))
