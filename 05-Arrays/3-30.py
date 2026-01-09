###
# Creates a multiplication table
#

table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# fill the table using loops
for i in range(5):          # rows
    for j in range(5):      # columns
        table[i][j] = (i + 1) * (j + 1)

# print the table
for row in table:
    for value in row:
        print(value, end=' ')
    print()
