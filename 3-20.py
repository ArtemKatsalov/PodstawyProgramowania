# Given array
arr = [7, 9, 2, 4, 5, 6]

even = []  # list for even numbers
odd = []   # list for odd numbers

# Separate even and odd numbers
for number in arr:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

# Put even numbers first, then odd numbers
arr = even + odd

# Print result
print("arr =", arr)
