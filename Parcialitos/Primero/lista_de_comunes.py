def listar_comunes(lista1, lista2):

    nueva_lista = []

    if len(lista1) * len(lista2) == 0:
        return nueva_lista

    for i in range(len(lista1)):
        if lista1[i] in lista2:
            if lista1[i] not in nueva_lista:
                nueva_lista.append(lista1[i])

    return nueva_lista


# ejecucion
l1 = [7, 9, 7, 1, 5, 10, 77, 8, 102, 44, 53]
l2 = [6, 9, 7, 7, 8, 23, 12]
l3 = listar_comunes(l1, l2)
print(f"{l1}\n{l2}\n{l3}")
