# Array with numbers
arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", *arr)
print("Unique elements:", end=" ")

# Check each element
for i in range(len(arr)):
    count = 0

    # Count how many times arr[i] appears in the array
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    # If element appears only once, print it
    if count == 1:
        print(arr[i], end=" ")
