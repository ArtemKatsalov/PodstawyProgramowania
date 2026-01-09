# Import our module
import MyArrays

# Sequence of numbers
numbers = [7, 3, 8, 5, 2]

# Print the numbers
print("Numbers:", ",".join(str(x) for x in numbers))

# Second largest
print("Second largest number:", MyArrays.second_largest(numbers))

# Median
print("Median:", MyArrays.median(numbers))

# Smallest and largest
min_max_values = MyArrays.min_max(numbers)
print("Smallest and largest number:", ",".join(str(x) for x in min_max_values))

# Numbers as a string separated by minus
print("Numbers as a string:", MyArrays.as_string(numbers))
