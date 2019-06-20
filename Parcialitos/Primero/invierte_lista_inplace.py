def invertir_lista(lista):
    i = 0
    j = len(lista) - 1

    while j > i:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1


# ejecucion
lista1 = [1, 2, 3, 4, 5]
print(lista1)
invertir_lista(lista1)
print(lista1)