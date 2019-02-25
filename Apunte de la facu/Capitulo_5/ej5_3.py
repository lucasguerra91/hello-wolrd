""" Nos piden que escribamos una función que le pida al usuario que ingrese un número positivo.
    Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar
    de su error mediante un mensaje y volverle a pedir el número.
    Resolver este problema usando
    1. Un ciclo interactivo.
    2. Un ciclo con centinela.
    3. Un ciclo “infinito” que se corta."""
# ---- Imports ----
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---- Funciones de input ----
def leer_ingreso():
    return float(input('\nIngrese un numero positivo:  '))


def leer_centinela():
    return input('Ingrese un numero positivo o "*" para terminar..  ')

# ---- Funciones de input ----


def ciclo_interactivo():
    """ En este ciclo se pregunta si se quiere seguir y se evalúa la respuesta
    después se insiste en caso de no ingresar un numero positivo"""

    mas_datos = 'Si'
    while mas_datos == 'Si':
        i = float(leer_ingreso())
        while i <= 0:
            print('\nEl numero ingresado no es positivo.')
            i = float(leer_ingreso())
        cls()
        mas_datos = input('\nDesea continuar ? Si / No  ')
        cls()
# Fin de la función ciclo_interactivo


def ciclo_centinela():
    """ Leemos el primer valor, si no es * lo pasamos a float y lo evaluamos
     Si no es positivo pedimos que se ingresen nuevamente, en cuanto meten un +
     volvemos a preguntar si desean continuar """
    cls()
    centinela = leer_centinela()
    # se captura el valor y se evalúa si no es *

    while centinela != '*':
        c = float(centinela)
        # se convierte a float para evaluar

        while c <= 0:
            # si no es positivo se pide que se vuelva a ingresar
            c = float(input('\nEl numero no es positivo, vuelva a ingresarlo  '))

        # por ultimo se vuelve a preguntar si se quiere cortar
        cls()
        centinela = leer_centinela()
# Fin de la función ciclo_centinela


def ciclo_infinito():
    """ Si bien el while True supone que sea infinito, se puede cortar la ejecución con el break
    que esta dentro del if """
    cls()
    while True:
        cls()
        centinela = leer_centinela()

        if centinela == '*':
            break
        else:
            f = float(centinela)
            while f <= 0:
                f = float(input('El numero no es positivo, vuelva a ingresarlo .. '))
# Fin de la función ciclo_infinito


print('\nElija como desea ejecutar el programa..\n')
x = int(input('1- Ciclo interactivo \n2- Ciclo centinela \n3- Ciclo infinito c/corte \n'))
if x == 1:
    ciclo_interactivo()
elif x == 2:
    ciclo_centinela()
else:
    ciclo_infinito()

os.system('pause')
