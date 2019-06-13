def quick_sort(lista):
    """
    Ordena la lista de forma recursiva
    :param lista: los elementos de la lista deben ser comparables
    :return: una nueva lista con los elementos ordenados
    """

    if len(lista) < 2:
        return lista

    menores, medio, mayores = _partition(lista)

    return quick_sort(menores) + medio + quick_sort(mayores)


def _partition(lista):
    """
    :param lista: no vacia
    :return: tres listas: menores, [medio] y mayores
    """

    pivote = lista[0]
    menores = []
    mayores = []

    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])

    return menores, [pivote], mayores


# ejecucion
# lista1 = [12, 24, 33, 105, 1, 15, 44, 106, 23, 45, 89, 3, 45, 77, 56, 4]
# print(lista1)
# lista2 = quick_sort(lista1)
# print(lista2)

lista3 = [1, 3, 4, 12, 15, 23, 24, 33, 44, 45, 45, 56, 77, 89, 105, 106]
print(lista3)
lista4 = quick_sort(lista3)
print(lista4)