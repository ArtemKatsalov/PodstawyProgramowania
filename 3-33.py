###
# Swaps the first and last column in a 2D array
#

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# print array before swap
print("Before swap:")
for row in array:
    for value in row:
        print(value, end=' ')
    print()

# swap first and last column
for i in range(len(array)):
    array[i][0], array[i][-1] = array[i][-1], array[i][0]

# print array after swap
print("\nAfter swap:")
for row in array:
    for value in row:
        print(value, end=' ')
    print()
