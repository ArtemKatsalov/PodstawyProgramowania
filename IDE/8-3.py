#
# A program that reads temperature in degrees Celsius from the keyboard.
# Then it calculates and prints the temperature in Kelvin and Fahrenheit.
#

# read temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# calculate temperature in Kelvin
kelvin = celsius + 273.15

# calculate temperature in Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# print results
print(f"Temperature in Kelvin: {kelvin:.2f}")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
