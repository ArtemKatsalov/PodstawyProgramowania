###
# Returns an identity matrix of size n
#
def identity_matrix(n):
    matrix = []
    for i in range(n):              # rows
        row = []
        for j in range(n):          # columns
            if i == j:
                row.append(1)       # main diagonal
            else:
                row.append(0)
        matrix.append(row)
    return matrix


###
# Prints a 2D array in rows and columns
#
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print()


# print identity matrices
print("Identity matrix 3x3:")
print_matrix(identity_matrix(3))

print("\nIdentity matrix 5x5:")
print_matrix(identity_matrix(5))

print("\nIdentity matrix 8x8:")
print_matrix(identity_matrix(8))
