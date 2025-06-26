# 13 Prove: Assignment
# Jaelee 

# caluclate wind speed
def calculate_wind(temperature):
    v = 5
    while v != 65:
        wind = 35.74 + (0.6215 * temperature) - (35.75 * (v ** 0.16)) + (0.4275 * temperature) * (v ** 0.16)
        print(f'At a temperature {temperature}F, and wind speed {v} mph, the windchill is: {wind:.2f}F')
        v += 5

# convert fahrenheit to celcius
def convert_celcius(temperature):
    return ((temperature * (9/5)) + 32)


temperature = float(input('What is the temperature? '))
degree = str(input('Fahrenheit or Celcius (F/C)? '))
# call function to convert if in celcuis
if degree.lower() == 'c':
    temperature = convert_celcius(temperature)

# call function to calculate wind
calculate_wind(temperature)





