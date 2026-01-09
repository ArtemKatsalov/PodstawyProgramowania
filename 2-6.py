matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

# Replace main diagonal with 1
for i in range(len(matrix)):
    matrix[i][i] = 1   # main diagonal: row index == column index

# Print modified matrix
for row in matrix:
    print(" ".join(str(x) for x in row))
