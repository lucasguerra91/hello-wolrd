"""
    Ejercicio 5.7.6. Potencias de dos.
    a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
     y devuelva True si el número es una potencia de 2, y False en caso contrario.
    b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la
     suma de todas las potencias de 2 que hay en el rango formado por esos números
     (0sinohayningunapotenciade2entrelosdos).Utilizarlafunción es_potencia_de_dos ,
     descripta en el punto anterior.
"""
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def es_potencia_de_dos(numero):

    if numero == 1:
        return True

    r = 1
    for i in range(1, numero):
        r *= 2
        if r == numero:
            return True
        else:
            continue

    return False


def leer_numero():
    return input('\nIngrese el numero que desea verificar (* para salir) ')


x = leer_numero()
while x != '*':
    z = int(x)
    if es_potencia_de_dos(z):
        print('Es potencia de dos')
    else:
        print('No es potencia de dos')
    x = leer_numero()

os.system('pause')


