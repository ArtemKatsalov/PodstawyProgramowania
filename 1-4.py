###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value(not negative index)', arr[3])
print('Sum of the first and last value', arr[4] + arr[0])
print('Middle value',arr[len(arr) // 2])
print('All array values separated by a single space:', end = ' ') 
for value in arr:
      print(value, end=' ')