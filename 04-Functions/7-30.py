def sum_natural(n):
    if n == 1:
        return 1
     #sum from 1 to n = n + sum from 1 to (n-1)
    return n + sum_natural(n-1) 

print(f"Sum of natural numbers from 1 to {10} is {sum_natural(10)}")