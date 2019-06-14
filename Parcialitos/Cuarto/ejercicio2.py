"""
2) Escribir una función recursiva que reciba una lista y un parámetro n, y devuelva otra
lista con los elementos de la lista replicados esa cantidad n de veces.
Por ejemplo, replicar ([1, 3, 3, 7], 2) debe devolver ([1, 1, 3, 3, 3, 3, 7, 7])
"""


def replicar(lista, n):
    """
    Recibe una lista y la cantidad de veces que debe replicarse cada elemento
    :param lista: lista de elementos iguales
    :param n: entero positivo
    :return: nueva lista con elementos replicados n veces
    """
    nueva_lista = []

    if len(lista) < 1:
        return nueva_lista

    for i in range(n):
        nueva_lista.append(lista[0])

    return nueva_lista + replicar(lista[1:], n)


# ejecucion
lista1 = [1, 3, 3, 7]
lista2 = replicar(lista1, 2)
print(lista1)
print(lista2)