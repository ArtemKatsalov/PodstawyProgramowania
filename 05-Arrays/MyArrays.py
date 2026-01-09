# Returns the second largest number in an array
def second_largest(arr):
    # Find largest and second largest manually
    largest = second = float('-inf')
    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x > second and x != largest:
            second = x
    return second

# Returns the difference between largest and smallest values
def range_diff(arr):
    smallest = largest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return largest - smallest

# Returns the median of an array
def median(arr):
    # First, sort the array manually using bubble sort
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    mid = n // 2
    if n % 2 == 1:
        return sorted_arr[mid]
    else:
        return (sorted_arr[mid-1] + sorted_arr[mid]) / 2

# Returns a two-element array [smallest, largest]
def min_max(arr):
    smallest = largest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return [smallest, largest]

# Returns array elements as a string separated by minus sign
def as_string(arr):
    s = ""
    for i in range(len(arr)):
        s += str(arr[i])
        if i != len(arr)-1:
            s += "-"
    return s
