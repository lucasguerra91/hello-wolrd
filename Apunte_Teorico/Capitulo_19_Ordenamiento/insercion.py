def ord_insercion(lista):
    """
    ordena una lista de elementos segun el metodo de insercion
    :param lista: de elementos comparables
    :return: la lista esta ordenada
    """

    for i in range(len(lista) - 1):
        # Si el elemento de la posicion i+1 esta desordenado respecto
        # al de la aparicion i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        print(f"DEBUG: {lista}")


def reubicar(lista, p):
    """
    Reubica al elemento que esta en la posicion p de la lista dentro del segmento [0: p-1]
    :param p: tiene que ser una posicion valida de la lista
    """
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j]

    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar para
        # insertar el elemento donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


# ejecucion
lista1 = [12, 24, 33, 105, 1, 15, 44]
print(lista1)
ord_insercion(lista1)
print(lista1)
print('\n')

lista2 = [1, 2, 3, 4, 5, 6, 7]
print(lista2)
ord_insercion(lista2)
print(lista2)

