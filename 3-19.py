# Array of real numbers
numbers = [2.5, 4.1, 6.3, 1.8, 5.0, 3.2]

# Read value from keyboard
value = float(input("Enter a value: "))

# Counter of elements greater than the given value
count = 0

# Loop through the array
for num in numbers:
    if num > value:
        count += 1

# Print results
print("Array:", numbers)
print("Value:", value)
print("Number of elements greater than the value:", count)
