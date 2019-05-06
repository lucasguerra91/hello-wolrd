import logica_buscaminas as l
import os


def jugar():
    """ Funcion principal , ejecucion del juego"""
    # Creo un tablero para trabajar y otro para mostrar
    tablero_visible = l.crear_tablero()
    tablero_logico, minas = l.cargar_minas()
    descubiertas = []
    banderas = []
    mensaje_instruccion = "Ingrese fila y columna para indicar la casilla que desea desbloquear (ej: b1) \n" \
              "Para agregar una bandera agregue el simbolo '%' al final(ej: b1%) \n \n"
    turnos = 0
    # print('DEBBUG - TABLERO LOGICO \n')
    # mostrar_tablero(tablero_logico)

    print('\nBienvenido!\n' + mensaje_instruccion)
    l.mostrar_tablero(tablero_visible)
    # aca empieza el tema
    ingreso_usuario = input('Ingrese la casilla (Escriba "salir" para terminar): ')

    while ingreso_usuario != 'salir':

        ingreso_validado = l.verificar_ingreso(ingreso_usuario.lower(), mensaje_instruccion)
        casilla, bandera, mensaje = ingreso_validado
        turnos += 1

        if casilla:
            fila, columna = casilla
            casilla_actual = tablero_logico[fila][columna]

            # FIX - Bandera en mina , perdia partida
            if casilla in minas and not bandera:
                l.limpiar_pantalla()
                l.mostrar_tablero(tablero_logico)
                print('Perdiste!')
                os.system('pause')
                break

            if casilla in descubiertas:
                mensaje = 'Casilla ya ingresada.'

            if bandera:
                if casilla in banderas:
                    tablero_visible[fila][columna] = '.'
                    # tablero_logico[fila][columna] = '.'
                    banderas.remove(casilla)

                    mensaje = 'Bandera desactivada!'

                elif casilla_actual == '.' or casilla_actual == '*':
                    tablero_visible[fila][columna] = '%'
                    # tablero_logico[fila][columna] = '%' a la bandera no la pongo en el
                    banderas.append(casilla)
                    mensaje = 'Bandera activada!\n'

                else:
                    mensaje = 'No se puede poner la bandera en una casilla descubierta..'

            else:
                adyacentes = l.contar_adyacentes(casilla, tablero_logico)
                descubiertas.append(casilla)
                tablero_logico[fila][columna] = str(adyacentes)
                tablero_visible[fila][columna] = str(adyacentes)

        l.limpiar_pantalla()
        # Descomentar para visualizar el tablero logico
        # l.mostrar_tablero(tablero_logico)
        l.mostrar_tablero(tablero_visible)

        if l.verificar_restantes(tablero_logico):
            l.limpiar_pantalla()
            l.mostrar_tablero(tablero_logico)
            print('Felicitaciones! \nGanaste en {} turnos!'.format(turnos))
            break

        print(mensaje)
        ingreso_usuario = input('Ingrese la casilla ("salir" para terminar)')


# ciclo de ejecucion
jugar()

