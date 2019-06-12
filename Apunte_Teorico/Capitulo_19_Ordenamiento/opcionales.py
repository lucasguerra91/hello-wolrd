def insercion(lista):

    n = len(lista)

    for i in range(1, n):
        temp = lista[i]
        j = i - 1

        while lista[j] > temp and j >= 0:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j+1] = temp


# ejecucion
lista = [5, 8, 2, 3, 6, 9]
insercion(lista)
print(lista)

