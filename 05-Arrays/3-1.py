array = [34,7,19,4,21,8]

even_count = 0

i = 0

while i < len(array):
    if array[i] % 2 == 0:
        even_count += 1
    i += 1

print("Number of even values:", even_count)