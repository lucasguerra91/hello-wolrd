"""
Ejercicio 13.3. Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n es
potencia de b.
Ejemplos:
es_potencia(8, 2) -> True
es_potencia(64, 4) -> True
es_potencia(70, 10) -> False
"""


def es_potencia(a, b):
    """

    :param a: supuesta potencia de b
    :param b: base
    :return: True or False
    """

    if b % a == 0:
        return True

    return es_potencia(a, b * b)


# ejecucion
print(es_potencia(6, 3))

