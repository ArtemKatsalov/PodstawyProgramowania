###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    import math
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input('Enter the length of the first side: '))
b = int(input('Enter the length of the second side: '))
c = int(input('Enter the length of the third side: '))

print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}')
