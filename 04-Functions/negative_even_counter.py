def f(x, y):
    count = 0
    for n in range(x + 1, y):
        if n < 0 and n % 2 == 0:
            count += 1
    return count
