# Original array
numbers = [15, 8, 31, 47, 2, 19]

print("Array:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

sum = 0
for num in numbers:
    sum += num

print(f"Arithmetic mean: {sum/len(numbers)}")