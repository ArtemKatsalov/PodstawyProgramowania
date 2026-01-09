###
# Finds the smallest and largest values in a 2D array
# and their row and column positions
#

array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# initialize min and max with the first element
min_value = array[0][0]
max_value = array[0][0]
min_row = min_col = 0
max_row = max_col = 0

# go through rows and columns
for i in range(len(array)):           # rows
    for j in range(len(array[i])):    # columns
        value = array[i][j]

        if value < min_value:
            min_value = value
            min_row = i
            min_col = j

        if value > max_value:
            max_value = value
            max_row = i
            max_col = j

# print results
print("Array:")
for row in array:
    print(row)

print("Smallest value:", min_value, "at row", min_row, "column", min_col)
print("Largest value:", max_value, "at row", max_row, "column", max_col)
