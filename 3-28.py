###
# Calculates the sum of values in the last column
#

array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

last_column_sum = 0

# go through each row
for row in array:
    last_column_sum += row[-1]   # take last element from the row

print("Sum of the last column:", last_column_sum)
