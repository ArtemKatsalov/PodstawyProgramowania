import queue

# Create a stack
stack = queue.LifoQueue()

# Put elements on the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Sum the last two numbers of the stack
if stack.qsize() >= 2:
    last = stack.get()    # removes 8
    second_last = stack.get()  # removes 9
    sum_last_two = last + second_last
    print("Sum of the last two numbers:", sum_last_two)

# Calculate the sum of the remaining elements
sum_remaining = 0
while not stack.empty():
    sum_remaining += stack.get()

print("Sum of the remaining stack elements:", sum_remaining)
