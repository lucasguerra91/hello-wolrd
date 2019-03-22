"""
    Escribir un programa que imprima todos los numeros pares entre dos numeros que se le pidan al usuario
"""


def imprime_pares(x, y):
    print('Los numeros pares entre {} y {} son:'.format(x,y))
    for i in range(x, y):
        if i % 2 == 0:
            print(i)


a = int(input('\n Ingrese el primer valor'))
b = int(input('\n Ingrese el segundo valor'))
imprime_pares(a, b)
