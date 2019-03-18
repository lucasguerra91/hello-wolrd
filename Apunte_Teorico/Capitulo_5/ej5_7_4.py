""" Utilizando la función randrange del módulo random , escribir un programa que
    obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
    si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
    correcto.   """

import random
import os


def genera_aleatorio():
    """ Genera un numero aleatorio entre 0 y 10"""
    return random.randrange(0, 10)


def ingreso_numero():
    """ Recibe el input del susuario"""
    return input('\nIngrese un numero (* para terminar)  ')


def compara_numeros():
    """ Genera un numero aleatorio y lo compara con el ingreso del usuario indicando si es mayor
    menor, o si el usuario acerto. Se corta el ciclo si se ingresa * """
    aleatorio = genera_aleatorio()
    entrada = ingreso_numero()
    while entrada != '*':
        numero = float(entrada)
        if numero == aleatorio:
            print('\nAcertaste!')
            break
        elif numero > aleatorio:
            print('El número ingresado es mayor al objetivo')
        else:
            print('El número ingresado es menor al objetivo')
        entrada = ingreso_numero()


compara_numeros()
os.system('pause')
