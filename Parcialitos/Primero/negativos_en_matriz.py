def negativos_diag_superior(lista):
    contador = 0
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            if i >= j:
                if lista[i][j] < 0:
                    contador += 1
    return contador


# ciclo de ejecucion
test_lista = [[0, 1, -3], [0, -4, 5], [-9, 3, 5]]
print(negativos_diag_superior(test_lista))
