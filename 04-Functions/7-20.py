def f(n):
    def is_prime(num):
        # check if num is prime
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0       # how many primes we have found
    candidate = 2   # current number to check
    while True:
        if is_prime(candidate):   # check if candidate is prime
            count += 1            # found a prime, increase count
            if count == n:        # if we reached the n-th prime
                return candidate  # return it
        candidate += 1            # check next number

# Test examples
print(f(1))  # 2
print(f(5))  # 11
print(f(5000))  # 48611
