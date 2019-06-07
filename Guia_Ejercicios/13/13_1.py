"""
Ejercicio 13.1. Escribir una función recursiva que reciba un número positivo 𝑛 y devuelva la
cantidad de dígitos que tiene.
"""


def contar_digitos(n):

    if n < 10:
        return 1

    return 1 + contar_digitos(n / 10)


# ejecucion
print(contar_digitos(12345))