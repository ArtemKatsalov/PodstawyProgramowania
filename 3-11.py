def bubble_sort(arr):
    n = len(arr)
    # Outer loop controls number of passes
    for i in range(n):
        # Inner loop compares neighboring elements
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr1 = [28, 44, 56, 11, 2, 8, 11]
arr2 = [2, -3, 58, 4, 0]
arr3 = [48, -5, -1, 64, 1]


print(bubble_sort(arr1))
print(bubble_sort(arr2))
print(bubble_sort(arr3))