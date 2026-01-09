# Program that finds N leading prime numbers

N = int(input("Enter how many prime numbers to find: "))

count = 0       # counts how many prime numbers have been found
num = 2         # number to check

print("Prime numbers:", end=" ")

while count < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
