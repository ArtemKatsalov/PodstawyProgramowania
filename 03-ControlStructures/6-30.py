# Program that prints a lottery coupon (numbers from 1 to 49) in 7x7 format

rows = 7
cols = 7

for i in range(1, rows + 1):
    for j in range(cols):
        print(i + j*rows, end=" ")
    print()
