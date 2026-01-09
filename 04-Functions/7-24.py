def f(expression):
    total = 0               # the result of the calculation
    currentNum = ''         # stores the current digit
    operation = '+'         # current operation, default is '+'

    for char in expression:
        if char.isdigit():
            currentNum = char      # store the digit
        elif char in '+-':
            # apply the previous operation to total
            if operation == '+':
                total += int(currentNum)
            else:
                total -= int(currentNum)
            operation = char       # update the current operation

    # apply the last operation after the loop
    if operation == '+':
        total += int(currentNum)
    else:
        total -= int(currentNum)
        
    return total

# Test examples
print(f("2+3"))        # 5
print(f("3+8+1"))      # 12
print(f("2+3-4+5-0"))  # 6
