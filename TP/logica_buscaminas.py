import random
from string import ascii_lowercase
import re
import os

# Maximo 26
DIMENSION = 8
MINAS = 10


def limpiar_pantalla():
    """Limpia la pantalla, funciona desde cmd o terminal en Linux. Para Pycharm o la consola de git no.. """
    os.system('cls' if os.name == 'nt' else 'clear')


def crear_tablero():
    """ Recibe la dimension de la matriz cuadrada, y la crea (no agrega valores a la misma) """
    tablero = []

    for i in range(DIMENSION):
        tablero.append([])
        for j in range(DIMENSION):
            tablero[i].append('.')

    return tablero


def mostrar_tablero(tablero):
    """ Muestra el tablero al jugador"""
    cabecera = ' '
    # En la consola de PyCharm y en la GitBash se grafica bien, en la cmd de Guindous no
    if os.name == 'nt':
        separacion = (15 * len(tablero) * '-')
    else:
        separacion = (8 * len(tablero) * '-')

    for i in range(len(tablero)):
        cabecera += '\t' + str(i+1) + '\t'
    print(cabecera + '\n' + separacion)

    for indice, i in enumerate(tablero):
        fila = ascii_lowercase[indice] + '|'

        for j in i:
            fila = fila + '\t' + str(j) + '\t'

        print(fila)

    print(' ')


def cargar_minas():
    """ No recibe parametros, crea un tablero y lo carga con minas. Devuelve el tablero
    y una lista con las coordenadas de las minas"""
    tablero = crear_tablero()
    minas = []
    cantidad_minas = 1

    j = random.randint(0, DIMENSION - 1)
    k = random.randint(0, DIMENSION - 1)
    tablero[j][k] = '*'

    while cantidad_minas < MINAS:
        if tablero[j][k] == '.':
            tablero[j][k] = '*'
            minas.append((j, k))
            cantidad_minas += 1

        j = random.randint(0, DIMENSION - 1)
        k = random.randint(0, DIMENSION - 1)

    return tablero, minas


def verificar_ingreso(ingreso, mensaje_ins):
    """ Recibe el ingreso del usuario y el mensaje de instrucciones de juego.
        Verifica el formato de ingreso:
        - Si es correcto: devuelve el par fila-columna de la casilla como tupla, la bandera (True/False) y
        un mensaje vacio.
        - Si no es correcto , devuelve None None Mensaje (indicando que la casilla se ingreso mal)"""

    bandera = False
    casilla = ()
    fila = 0
    columna = 0
    mensaje = 'Casilla invalida..\n' + mensaje_ins

    if ingreso == 'salir':
        return 'Salir'

    patron_ingreso = r'([a-{}])([0-9]+)(%?$)'.format(ascii_lowercase[DIMENSION - 1])

    # search devuelve un grupo con los parametros si cumplen con la expresion regular
    entrada_valida = re.search(patron_ingreso, ingreso)

    if entrada_valida:
        fila = int(ascii_lowercase.index(entrada_valida.group(1)))
        columna = int(entrada_valida.group(2))-1
        # DEBUG - la regEx rompe si tomo dos digitos -
        # print(type(columna))
        # print(columna)
        bandera = bool(entrada_valida.group(3))

        if columna < DIMENSION:
            casilla = (fila, columna)
            mensaje = ''
        else:
            limpiar_pantalla()
            return None, None, mensaje
    # FIX - Luego de ingresar asdf dos veces marcaba que ya estaba ingresada
    else:
        limpiar_pantalla()
        return None, None, mensaje

    return casilla, bandera, mensaje


def contar_adyacentes(casilla, tablero):
    """ Recibe como parámetros: una tupla con los indices de la casilla y el tablero logico.
        Devuelve la cantidad de minas adyacentes a la casilla que recibió."""
    contador = 0
    fila, columna = casilla
    for i in range(max((fila - 1), 0), min((fila + 2), DIMENSION)):
        for j in range(max((columna - 1), 0), min((columna + 2), DIMENSION)):
            if tablero[i][j] == '*':
                contador += 1
    return contador


def verificar_restantes(tablero):
    """ Recibe el tablero logico actual, devuelve True si ya no hay casillas por revelar o False si todavia hay """
    contador_libres = 0
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if tablero[i][j] != '*' and tablero[i][j] != '.':
                contador_libres += 1
    # print(contador_libres)
    # print(DIMENSION ** 2 - MINAS)
    if contador_libres == (DIMENSION ** 2 - MINAS):
        return True
    return False
