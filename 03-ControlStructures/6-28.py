
a = 0
b = 1
count = 0

while count < 20:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b 
    count += 1
