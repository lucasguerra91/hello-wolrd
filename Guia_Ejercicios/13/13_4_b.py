"""
Ejercicio 13.4. Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
devuelva una lista con las posiciones en donde se encuentra b dentro de a.
Ejemplo:
posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]
"""


def _posiciones_de(a, b, lista=[], indice=0):

    aparicion = a.find(b)

    if aparicion == -1:
        return lista

    lista.append(aparicion + indice)

    indice += aparicion + len(b)

    return _posiciones_de(a[aparicion + len(b):], b, lista, indice)


def posiciones_de(a, b):
    return _posiciones_de(a, b)


# ejecucion
print(posiciones_de("Un tete a tete con Tete", "te"))
