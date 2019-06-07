"""
Ejercicio 13.4. Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
devuelva una lista con las posiciones en donde se encuentra b dentro de a.
Ejemplo:
posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]
"""


def posiciones_de(a, b):
    """
    :param a: cadena
    :param b: sub-cadena
    :return: indices en los que subcadena aparece en cadena
    """

    aparicion = a.rfind(b)
    if aparicion == -1:
        return []

    return [aparicion] + posiciones_de(a[:aparicion], b)


# ejecucion
print(posiciones_de("Un tete a tete con Tete", "te"))
