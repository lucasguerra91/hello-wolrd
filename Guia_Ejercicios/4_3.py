""" Dada una dimension n, imprimir la matriz identidad correspondiente  a esa dimension """
import numpy as np


def crear_matriz_cuadrada(n):
    """ Recibe la dimension de la matriz cuadrada, y la crea (no agrega valores a la misma) """
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append([])
    return m


def llenar_identidad(matriz):
    """ Recibe como parametro una matriz cuadrada y la devuelve como matriz identidad"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    return matriz


def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        print(*matriz[i], sep='\t')


def imprimir_matriz2(matriz):
    for i in range(len(matriz)):
        print(i, sep='\t')

    for i in range(len(matriz)):
        print(*matriz[i], sep='\t')


# ciclo de ejecución
matriz = crear_matriz_cuadrada(4)
llenar_identidad(matriz)
imprimir_matriz2(matriz)


lista=[25, 12, 15, 66, 12.5]
vector=np.array(lista)
print(vector)