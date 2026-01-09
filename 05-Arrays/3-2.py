# Original array
numbers = [15, 8, 31, 47, 2, 19]

# Print original array
print("existed array:", end=" ")
for num in numbers:
    print(num, end=" ")
print() 

# Print reversed array
print("reverse array:", end=" ")
for i in range(len(numbers)-1, -1, -1): 
    # len(numbers) - 1 -> index of the last element
    # -1 -> stop before reaching -1 (so index 0 is included)
    # -1 -> step backwards
    print(numbers[i], end=" ")
print()
