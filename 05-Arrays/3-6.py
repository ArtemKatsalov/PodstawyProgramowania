# Original array
numbers = [15, 8, 31, 47, 2, 19]

i = 0

print("Array:", end=" ")
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1
print()

sum = 0
i = 0
while i < len(numbers):
    sum += numbers[i]
    i += 1

print(f"Arithmetic mean: {sum/len(numbers)}")