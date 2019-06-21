def crear_matriz(a, b):

    matriz = [[0 for x in range(a)] for y in range(b)]

    for i in range(a):
        for j in range(b):
            matriz[i][j] = float(input("Ingrese un numero: "))

    return matriz


def imprimir_matriz(matriz, a, b):
    for i in matriz:
        print(i)


# ejecucion
matriz1 = crear_matriz(4, 4)
imprimir_matriz(matriz1, 4, 4)


