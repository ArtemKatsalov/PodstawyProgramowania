# Two arrays
array1 = [2, 4, 6]
array2 = [1, 2, 3, 4, 5, 6, 7]

# Assume array1 is a subset of array2
is_subset = True

# Check each element from array1
for element in array1:
    found = False
    for value in array2:
        if element == value:
            found = True
            break
    if not found:
        is_subset = False
        break

# Print result
print("Array1:", array1)
print("Array2:", array2)

if is_subset:
    print("Result: Array1 is a subset of Array2")
else:
    print("Result: Array1 is NOT a subset of Array2")
