def termina_en_cero(lista):
    """

    :param lista: de numeros, no deberia estar vacia
    :return: nueva lista con los numeros que finalizan en cero
    """

    if len(lista) == 0:
        return lista

    nueva_lista = []

    for i in range(len(lista)):
        if (lista[i]/10) % 2 == 0:
            nueva_lista.append(lista[i])

    return nueva_lista


# ejecucion
lista1 = [4, 23, 40, -7, 0, 14, 1000, -760]
print(lista1)
lista2 = termina_en_cero(lista1)
print(lista2)
