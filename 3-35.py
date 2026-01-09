###
# Returns the transposed matrix of m
#
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []

    # create transposed matrix
    for j in range(cols):         # new rows
        new_row = []
        for i in range(rows):     # new columns
            new_row.append(m[i][j])
        transposed.append(new_row)
    
    return transposed

###
# Prints a 2D array in rows and columns
#
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()
    print()  # empty line after matrix

# Matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

# Transpose and print matrices
print("Matrix 1 transposed:")
print_matrix(transpose_matrix(matrix1))

print("Matrix 2 transposed:")
print_matrix(transpose_matrix(matrix2))

print("Matrix 3 transposed:")
print_matrix(transpose_matrix(matrix3))
