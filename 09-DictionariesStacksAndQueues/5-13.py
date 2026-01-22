import queue

# create a stack
stack = queue.LifoQueue()

print("Enter RPN tokens one by one (numbers, +, -, *, /). Enter '=' to show result.")

while True:
    token = input("Enter number/operator/= : ")

    # if token is '=' → pop and show result
    if token == "=":
        if stack.empty():
            print("Stack is empty. No result to show.")
        else:
            result = stack.get()
            print("Result:", result)
        break

    # if token is an operator
    elif token in ["+", "-", "*", "/"]:
        # pop two values
        if stack.qsize() < 2:
            print("Not enough values in the stack to perform operation.")
            continue

        b = stack.get()
        a = stack.get()

        if token == "+":
            res = a + b
        elif token == "-":
            res = a - b
        elif token == "*":
            res = a * b
        elif token == "/":
            if b == 0:
                print("Error: Division by zero")
                stack.put(a)  # push back values
                stack.put(b)
                continue
            res = a / b

        stack.put(res)
        print("Stack after operation:", res)

    # otherwise assume number
    else:
        try:
            value = float(token)
            stack.put(value)
        except ValueError:
            print("Invalid input. Enter a number, operator, or '='.")
