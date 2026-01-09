def f(n,m=0):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return f(n - 1, m + 1) + f(n - 2, m + 1)
    
print(f(5)) # 3
print(f(9)) # 21