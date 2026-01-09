###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Enter the SWIFT code: ')
#bank code = first 4 characters
#country code = characters 5 and 6
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
