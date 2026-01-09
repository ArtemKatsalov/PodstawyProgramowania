from range_check import in_range

number = int(input("A number: "))
x = 2
y = 15

result = in_range(number, x, y)

print(f"Number {number} in the range <{x},{y}>: {'yes' if result else 'no'}")
