###
# Creates and returns a two-dimensional array filled with zeros
#
def create_2d_arr(x, y):
    arr = []
    for i in range(x):          # number of rows
        row = []
        for j in range(y):      # number of columns
            row.append(0)
        arr.append(row)
    return arr

# create a 3x5 array
array_2d = create_2d_arr(3, 5)

# print the array
for row in array_2d:
    print(row)
