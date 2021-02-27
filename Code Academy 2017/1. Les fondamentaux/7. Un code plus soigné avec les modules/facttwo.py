def factoriel(n):
    result = 1
    while n > 0:
        if n == 1:
            result *= 1
        else:
            result *= n
        n -= 1
    return result