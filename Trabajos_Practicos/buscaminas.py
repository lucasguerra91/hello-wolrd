import random
from string import ascii_lowercase
import re
import os

# Maximo 26
DIMENSION = 8
MINAS = 10


def limpiar_pantalla():
    """Limpia la pantalla"""
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
    separacion = (15 * len(tablero) * '-')
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
    """ Verifica la entrada del usuario y devuelve el casillero y el estado
    de la bandera"""

    bandera = False
    casilla = ()
    fila = 0
    columna = 0
    mensaje = 'Casilla invalida..\n' + mensaje_ins

    patron_ingreso = r'([a-{}])([0-9]+)(%?)'.format(ascii_lowercase[DIMENSION - 1])
    # search devuelve un grupo con los parametros si cumplen con la expresion regular
    entrada_valida = re.search(patron_ingreso, ingreso)

    if ingreso == 'salir':
        return 'Salir'

    elif entrada_valida:
        fila = int(ascii_lowercase.index(entrada_valida.group(1)))
        columna = int(entrada_valida.group(2))-1
        bandera = bool(entrada_valida.group(3))
        mensaje = ''

    casilla = (fila, columna)
    # print('DEBUGG - FILA Y COLUMNA {} {}'.format(fila, columna))

    return casilla, bandera, mensaje


def contar_minas_cercanas(casilla, tablero):
    """Recibe como parametro la casilla en la que se encuentra el jugador y devuelve la cantidad
    de minas adyacentes"""
    fila, columna = casilla
    contador_adyacentes = 0

    if fila == 0:
        if columna == DIMENSION - 1:
            for i in range(fila, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna - 1, columna):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1
        elif columna == 0:
            for i in range(fila, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna, columna + 2):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1
        else:
            for i in range(fila, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna -1, columna + 2):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1

    elif fila == DIMENSION - 1:
        if columna == 0:
            for i in range(fila - 1, fila + 1):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna , columna + 2):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1
        elif columna == DIMENSION-1:
            for i in range(fila - 1, fila):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna - 1, columna + 1):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1

    else:
        if columna == 0:
            for i in range(fila - 1, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna + 1, columna + 2):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                            contador_adyacentes += 1
        elif columna == DIMENSION-1:
            for i in range(fila - 1, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna - 1, columna +1):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1
        else:
            for i in range(fila - 1, fila + 2):
                # print('DEBBUG - I:{}'.format(i))
                for j in range(columna - 1, columna + 2):
                    # print('DEBBUG - J:{}'.format(j))
                    if tablero[i][j] == '*':
                        contador_adyacentes += 1

    return contador_adyacentes


def verificar_restantes(tablero):
    """ Recibe el tablero logico actual, devuelve True si ya no hay casillas por revelar o False si todavia hay"""
    contador_libres = 1

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if tablero[i][j] != '*' and tablero[i][j] != '.':
                contador_libres += 1
    # print(contador_libres)
    # print(DIMENSION ** 2 - MINAS)
    if contador_libres == (DIMENSION ** 2 - MINAS):
        return True

    return False


def jugar():
    """ Funcion principal , ejecucion del juego"""
    # Creo un tablero para trabajar y otro para mostrar
    tablero_visible = crear_tablero()
    tablero_logico, minas = cargar_minas()
    descubiertas = []
    mensaje_instruccion = "Ingrese fila y columna para indicar la casilla que desea desbloquear (ej: b1) \n" \
              "Para agregar una bandera agregue el simbolo '%' al final(ej: b1%) \n \n"
    turnos = 0
    # print('DEBBUG - TABLERO LOGICO \n')
    # mostrar_tablero(tablero_logico)

    print('\nBienvenido!\n'+ mensaje_instruccion)
    mostrar_tablero(tablero_visible)
    # aca empieza el tema
    ingreso_usuario = input('Ingrese la casilla (Escriba "salir" para terminar): ')

    while ingreso_usuario != 'salir':

        ingreso_validado = verificar_ingreso(ingreso_usuario.lower(), mensaje_instruccion)
        casilla, bandera, mensaje = ingreso_validado
        turnos += 1

        if verificar_restantes(tablero_logico):
            print('Felicitaciones! \nGanaste en {} turnos!'.format(turnos))
            break

        if casilla:
            fila, columna = casilla
            casilla_actual = tablero_logico[fila][columna]

            if casilla in minas:
                mostrar_tablero(tablero_logico)
                print('Perdiste!')
                break

            if casilla in descubiertas:
                mensaje = 'Casilla ya ingresada.'

            if bandera:
                if casilla_actual == '.':
                    tablero_visible[fila][columna] = '%'
                    tablero_logico[fila][columna] = '%'
                    mensaje = 'Bandera activada!'

                elif casilla_actual == '%':
                    tablero_visible[fila][columna] = '.'
                    tablero_logico[fila][columna] = '.'
                    mensaje = 'Bandera desactivada!'
                else:
                    mensaje = 'No se puede poner la bandera'
            else:
                minas_cercanas = contar_minas_cercanas(casilla, tablero_logico)
                descubiertas.append(casilla)
                tablero_logico[fila][columna] = str(minas_cercanas)
                tablero_visible[fila][columna] = str(minas_cercanas)

        limpiar_pantalla()
        #mostrar_tablero(tablero_logico)
        mostrar_tablero(tablero_visible)
        print(mensaje)
        ingreso_usuario = input('Ingrese la casilla ("salir" para terminar)')



# ciclo de ejecucion
jugar()
