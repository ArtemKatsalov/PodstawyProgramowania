def occurs(number, array):
    for item in array:
        if item == number:
            return True
    return False            

num = int(input("Enter a number to check is this number appears in the array: "))

arr = [15, 38, 7, 23, 14]

print(f"Number: {num}")
print("Array:",*arr)
if occurs(num, arr):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does not appear in the array")