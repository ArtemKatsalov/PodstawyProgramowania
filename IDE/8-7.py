#
# A program that reads an integer number from the keyboard
# and prints that value as a binary and hexadecimal number.
#
# read integer from keyboard
decimal_num = int(input('Enter the decimal number: '))
# convert to binary
binary_num = bin(decimal_num)
# convert to hexadecimal
hexadecimal_num = hex(decimal_num)
print(f'Binary number: {binary_num}')  
print(f'Hexadecimal number: {hexadecimal_num}')  