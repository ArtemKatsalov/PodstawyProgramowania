# Original tuple
t = (10, 20, 30, 40, 50)

# Print the original tuple
print("Tuple:", end=" ")
for i in range(len(t)):
    if i < len(t)-1:
        print(t[i], end=",")
    else:
        print(t[i])

# Print the tuple in reverse order
print("Reverse order:", end=" ")
for i in range(len(t)-1, -1, -1):  # start from last index to 0
    if i > 0:
        print(t[i], end=",")
    else:
        print(t[i])
