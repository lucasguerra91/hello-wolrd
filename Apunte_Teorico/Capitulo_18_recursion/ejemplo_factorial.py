def factorial(n):
    """ factorial con recursion"""

    if n == 0:
        r = 1
        return r

    f = factorial(n - 1)
    r = n * f
    return r


# ejecucion
print(factorial(10))