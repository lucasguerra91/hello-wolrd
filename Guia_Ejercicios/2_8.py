"""
    Idem al anterior pero con n numeros
"""


def imprimir_domino(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('.' * j,  '.' * i, sep='|', end='\n')
        print('\n')


cantidad_fichas = int(input('\nIngrese el valor maximo de las fichas'))
imprimir_domino(cantidad_fichas)
