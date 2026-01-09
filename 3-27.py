###
# Prints values of a 2x4 two-dimensional array
#

array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# print rows and columns
for row in array:          # goes through each row
    for value in row:     # goes through each column in the row
        print(value, end=' ')
    print()               # new line after each row
