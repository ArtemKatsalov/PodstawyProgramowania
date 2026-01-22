import queue

number = int(input("Enter a natural number: "))
original_number = number

stack = queue.LifoQueue()

print("\nDivision\tRemainder")

# Convert to binary using division by 2
while number > 0:
    remainder = number % 2
    print(f"{number} / 2 = {number // 2}\t{remainder}")
    stack.put(remainder)
    number = number // 2

# Display results
print(f"\nNatural number: {original_number}")
print("Binary number:", end=" ")

# Pop from stack to get binary number
while not stack.empty():
    print(stack.get(), end="")

print()
