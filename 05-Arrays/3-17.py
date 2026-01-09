# Tuple with numbers
t = (50, 20, 40, 50, 30, 50)

# Value to count
value = int(input("Value: "))

# Count occurrences
count = 0
for item in t:
    if item == value:
        count += 1

# Print results
print("Tuple:", ",".join(str(item) for item in t))
print(f"Number of occurrences: {count}")
