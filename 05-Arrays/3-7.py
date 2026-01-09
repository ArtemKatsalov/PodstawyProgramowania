arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

print("Names: ", end=" ")
for name in arr:
    print(name, end=" ")
print()

longest_name = arr[0]

for name in arr:
    if len(name) > len(longest_name):
        longest_name = name

print("Longest name:", longest_name)