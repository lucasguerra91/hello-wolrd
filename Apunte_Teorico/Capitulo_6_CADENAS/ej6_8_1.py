"""
Ejercicio 6.8.1. Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
    'reflejoojelfer'
"""


def dos_primeros(c):
    new_c1 = c[0:2]
    return new_c1


def tres_ultimos(c2):
    new_c2 = c2[len(c2)-3:]
    return new_c2


def salteando(c3):
    new_c3 = (c3[::2])
    return new_c3


def inverso(c4):
    new_c4 = c4[::-1]
    return new_c4


def normal_inverso(c5):
    invertida = inverso(c5)
    new_c5 = c5 + invertida
    return new_c5


cadena = input('Ingrese la cadena :')
print(dos_primeros(cadena))
print(tres_ultimos(cadena))
print(salteando(cadena))
print(inverso(cadena))
print(normal_inverso(cadena))
