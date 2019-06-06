def potencia(b, n):
    """ Pre-condicion: n>=0
    Devuelve b^n . """

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b


# ejecucion
print(potencia(3, 3))
print(potencia(5, 5))

