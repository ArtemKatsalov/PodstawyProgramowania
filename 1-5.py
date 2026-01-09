###
# Modifies array values
#
arr = [1, 2, 3, 4, 5]

print('Array:', arr)

# subtract one from the first element
arr[0] -= 1
print('Array:', arr)

# increase the last element by 4
arr[len(arr) - 1] += 4
print('Array:', arr)

# multiply the middle element by 2
arr[len(arr) // 2] *= 2
print('Array:', arr)
