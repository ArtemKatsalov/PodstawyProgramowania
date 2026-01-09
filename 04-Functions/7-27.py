def f(productCode):
    if len(productCode) != 4:           # check if code has exactly 4 digits
        return False
    
    firstThree = productCode[:3]        # extract the first three digits
    control = int(productCode[3])       # extract the fourth (control) digit
    
    digitSum = sum(int(d) for d in firstThree)  # sum of the first three digits
    
    return digitSum % 7 == control     # check if control digit is correct

# Test examples
print(f("1082"))  # True
print(f("2035"))  # True
print(f("1114"))  # False
print(f("7071"))  # False
