"""
    Escribir una funcion que dada 4 numeros, devuelva el mayor multiplo de dos de ellos

"""


def calcular_maximo(a, b, c, d):
    return max(a*b, a*c, a*d, b*c, b*d, c*d)


a = int(input('\nIngrese cuatro valores. \n\nPrimer valor:'))
b = int(input('\nSegundo valor:'))
c = int(input('\nTercer valor:'))
d = int(input('\nCuarto valor:'))

print('El mayor multiplipo es {}'.format(calcular_maximo(a, b, c, d)))
