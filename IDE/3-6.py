###
# a program that calculates the distance to the horizon
#  from a height given in meters from the keyboard.
#
import math
h = float(input("Enter the height of the observer in meters: "))#h is the height of the observer in meters
h = h/1000
d = 3.57 * math.sqrt(h) #d is the distance to the horizon in kilometers
print(d, "km")