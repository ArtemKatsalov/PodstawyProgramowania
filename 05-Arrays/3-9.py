# Compares two arrays element by element
def compare(array1, array2):
    # Check if arrays have the same length
    if len(array1) != len(array2):
        return False

    # Compare elements with the same index
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


# Test arrays
arrays = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

# Test comparisons
for arr1, arr2 in arrays:
    print("Array1:", *arr1)
    print("Array2:", *arr2)

    if compare(arr1, arr2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")

    print()
