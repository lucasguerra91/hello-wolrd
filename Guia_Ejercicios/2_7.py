""" Escribir un programa que imprima por pantalla todas las fichas del
    domino
"""


def imprimir_domino():
    for i in range(0, 7):
        for j in range(0, i+1):
            print('.' * j,  '.' * i, sep='|', end='\n')


imprimir_domino()
