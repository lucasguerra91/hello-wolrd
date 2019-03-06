import random

CANT_DIGITOS = 5
ME_DOY = "Me doy"


def generar_codigo():
    """ Genera un código aleatorio de CANT_DIGITOS dígitos"""
    digitos = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    codigo = ''
    for i in range(CANT_DIGITOS):
        numero = random.choice(digitos)
        # print('Codigo: {}. Numero: {} .'.format(codigo, numero)) Control de asignacion de los numeros
        while numero in codigo:
            numero = random.choice(digitos)
        codigo += numero
    print('[DEBUG] Codigo: {}.'.format(codigo))
    return codigo


def ingreso_codigo():
    """ Recibe el código del jugador """
    codigo_jugador = input('\nIngrese el código de {} dígitos..'.format(CANT_DIGITOS))
    if codigo_jugador == ME_DOY:
        return ME_DOY
    else:
        while len(codigo_jugador) != CANT_DIGITOS:
            codigo_jugador = input('Recuerde que código debe ser de  {} dígitos..'.format(CANT_DIGITOS))
    return codigo_jugador


def verifica_ingreso(ingreso, codigo):
    """ Verifica los aciertos y las coincidencias """
    cntc = 0
    cnta = 0
    for x in range(CANT_DIGITOS):
        if ingreso[x] == codigo[x]:
            cnta += 1
        elif ingreso[x] in codigo:
            cntc += 1
    return cntc, cnta


def master_mind():
    """ Función principal, genera el código, recibe la entrada del jugador y la evalúa
    devolviendo coincidencias y aciertos, en caso de acertar el código completo, lo informa """

    target = generar_codigo()
    ingreso = ingreso_codigo()
    intentos = 1

    while (ingreso != target) and (ingreso != ME_DOY):
        coincidencias, aciertos = verifica_ingreso(ingreso, target)

        print('\nEl número {} no concuerda con el código.'.format(ingreso))
        print('Aciertos: {} \nCoincidencias: {} \n'.format(aciertos, coincidencias))
        ingreso = ingreso_codigo()
        intentos += 1

    if ingreso == ME_DOY:
        print('\nSuerte en la próxima! El código era : {}'.format(target))
    else:
        print('\nLuego de {} intento(s).. \nHas acertado..!'.format(intentos))


print('Bienvenido a MasterMind')
print('Intente adivinar el código generado, para salir teclee "Me doy"')
master_mind()



