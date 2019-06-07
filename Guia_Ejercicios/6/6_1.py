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
    """ Recibe una cadena y nos devuelve  los dos primeros caracteres de la misma"""
    new_c1 = c[0:2]
    return new_c1


def tres_ultimos(c2):
    """ Recibe una cadena y nos devuelve  los tres ultimos caracteres de la misma"""
    new_c2 = c2[len(c2)-3:]
    return new_c2


def salteando(c3):
    """ Recibe una cadena y nos devuelve una nueva cadena salteando la anterior de 2 en 2"""
    new_c3 = (c3[::2])
    return new_c3


def inverso(c4):
    """ Recibe una cadena y nos devuelve la misma invertida"""
    new_c4 = c4[::-1]
    return new_c4


def normal_inverso(c5):
    """ Recibe una cadena y nos devuelve la misma cadena concatenada a su inverso"""
    invertida = inverso(c5)
    new_c5 = c5 + invertida
    return new_c5


def inversa_clase(cadena):
    cr = ''
    for i in range(1, len(cadena)):
        cr += cadena[-i]
    print(cr)


cadena = input('Ingrese la cadena :')
print(dos_primeros(cadena))
print(tres_ultimos(cadena))
print(salteando(cadena))
print(inverso(cadena))
print(normal_inverso(cadena))
inversa_clase(cadena)