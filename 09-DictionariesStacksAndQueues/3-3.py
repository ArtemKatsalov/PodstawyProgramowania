import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {')':'(', '}':'{', ']':'['}

    for char in expression:
        if char in "({[":
            stack.put(char)
        elif char in ")}]":
            if stack.empty():
                return False
            top = stack.get()
            if top != pairs[char]:
                return False

    return stack.empty() #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
    print("Expression 1: brackets are correct")
else:
    print("Expression 1: brackets are NOT correct")

if brackets_ok(expression2):
    print("Expression 2: brackets are correct")
else:
    print("Expression 2: brackets are NOT correct")

if brackets_ok(expression3):
    print("Expression 3: brackets are correct")
else:
    print("Expression 3: brackets are NOT correct")