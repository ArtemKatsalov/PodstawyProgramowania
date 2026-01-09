def f(number):
    num_str = str(number)
    total = 0
    
    for digit in set(num_str): # iterate over unique digits
        count = num_str.count(digit) # count how many times this digit appears
        if count > 1:
            total += int(digit) * count
    
    return total

print(f(1027))       # 0
print(f(230335))     # 9
print(f(513553007))  # 21
