# 04 Teach: Team Activity
# Jaelee
import math

print('Welcome to the velocity calculator. Please enter the following:')
print()

# user input
mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
csa = float(input('Cross sectional area (in m^2): '))
drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# caulculate c
c = (1/2) * density * csa * drag
print()
print(f'The inner value of c is: {c:.3f}')

# calculate velocity
velocity = (math.sqrt(mass * gravity / c)) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))
print(f'The velocity after {time} seconds is: {velocity:.3f} m/s')
