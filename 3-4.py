# Original array
numbers = [-15, 8, -31, 47, -2, 19]

# Initialize max and min with the first element
max_num = numbers[0]
min_num = numbers[0]

# Loop through the array to find max and min
for num in numbers:
    if num > max_num:  # if current number is greater than max_num
        max_num = num  # update max_num
    if num < min_num:  # if current number is smaller than min_num
        min_num = num  # update min_num

# Print the results
print("Maximum number:", max_num)
print("Minimum number:", min_num)