arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for number in arr1:
    found = False

  # Check if number exists in arr2
    for value in arr2:
        if number == value:
            found = True
            break
    
    # If not found in arr2, print it
    if not found:
        print(number)