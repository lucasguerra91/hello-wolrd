def ord_seleccion(lista):
    """
    Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables
    Post: la lista está ordenada
    """

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la ultima posicion del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print(f"DEBUG: {p} {n} {lista}")

        # reducir el segmento en 1
        n = n - 1


def buscar_max(lista, a, b):
    """
    Devuelve la posicion del maximo elemento en un segmento de lista de elementos comparables
    La lista no debe estar vacia
    a y b son las posiciones inicial y final del segmento
    :return: maximo
    """

    pos_max = a
    for i in range(a+1, b+1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


# ejecucion
lista = [12, 24, 33, 105, 1, 15, 44]
print(lista)
ord_seleccion(lista)
print(lista)