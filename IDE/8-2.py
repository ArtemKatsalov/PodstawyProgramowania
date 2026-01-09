#
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = float(input("Enter radius: "))
PI = 3.14

# calculate area 
area = PI * r * r

# calculate circumference 
circumference = 2 * PI * r

# print results
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')
