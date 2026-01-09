###
# Converts a 2D array into 1D array
#
def flatten_2d(array2d):
    result = []
    for row in array2d:
        for value in row:
            result.append(value)
    return result

# Matrices
matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Flatten and print
print("Matrix 1 flattened:", flatten_2d(matrix1))
print("Matrix 2 flattened:", flatten_2d(matrix2))
print("Matrix 3 flattened:", flatten_2d(matrix3))
