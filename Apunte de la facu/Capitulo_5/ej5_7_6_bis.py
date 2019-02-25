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
    """ cls de windows """
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """ pausa de windows"""
    os.system('pause')


def es_potencia_de_dos(numero):
    """ Verifica si es potencia de dos, en primera instancia descartamos el 1 , que seria 2 a la 0
     luego vemos si podemos componer el numero que tenemos como potencia de dos y de paso devolvemos
     que potencia de dos es , en caso de serlo
    """
    if numero == 1:
        return True, 0

    r = 1
    for i in range(1, numero):
        r *= 2
        if r == numero:
            return True, i
        else:
            continue

    return False


def leer_numero():
    return input('\nIngrese el numero que desea verificar (* para salir) ')


x = leer_numero()
while x != '*':
    potencia, cual = es_potencia_de_dos(int(x))
    if potencia:
        print('Es potencia, 2 a la ', cual)
    else:
        print('No es potencia de dos')
    x = leer_numero()

clear()
print('Hasta luego..')
os.system('pause')
