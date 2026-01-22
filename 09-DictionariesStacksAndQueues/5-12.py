import queue

# Function to reverse a string using a stack
def reverse_string(text):
    stack = queue.LifoQueue()  # create a stack

    # Push each character onto the stack
    for char in text:
        stack.put(char)

    reversed_text = ""
    # Pop characters from the stack to form reversed string
    while not stack.empty():
        reversed_text += stack.get()

    return reversed_text

# Program: read text from keyboard and reverse it
user_text = input("Enter text to reverse: ")
reversed_text = reverse_string(user_text)

print("Reversed text:", reversed_text)
