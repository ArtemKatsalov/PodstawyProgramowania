
def factorial(n):
    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1
    # n! = n * (n-1)!
    return n * factorial(n-1)

print(f"The factorial of 5 is {factorial(5)}")

