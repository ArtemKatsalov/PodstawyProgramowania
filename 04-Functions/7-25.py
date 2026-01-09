def f(x, y):
    total = 0  # initialize sum
    for num in range(x, y + 1):  # iterate through all numbers in the range [x, y]
        # check the conditions:
        # divisible by 2 and 3, but NOT divisible by 4
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num  # add the number to the total
    return total

# Test examples
print(f(1, 20))   # 24
print(f(10, 30))  # 48
