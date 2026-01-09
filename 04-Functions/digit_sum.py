def f(number, even):
    total = 0
    for digit in str(number):
        d = int(digit)
        if even and d % 2 == 0:
            total += d
        if not even and d % 2 == 1:
            total += d
    return total
