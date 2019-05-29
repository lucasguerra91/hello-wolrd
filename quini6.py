import random
import os
from _datetime import datetime


def random_choice(d):
    """ A partir de un diccionario , genera una clave utilizando sus valores como referencia
    para el calculo de probabilidad de ser elegida, devuelve la clave """
    clave_random = random.choices(list(d), weights=d.values())
    clave = clave_random[0]
    return clave


def lista_printable(lista):
    """Recibe una lista y devuelve una cadena con los items de la lista
    separados por guiones """
    cadena = ''
    for i in range(6):
        if i == 5:
            cadena += str(lista[5])
        else:
            cadena += str(lista[i]) + '\t-\t'
    return cadena


def sorteo():
    """ Simula un solo sorteo aleatorio (sin desquite, sale o sale o esas cosas.)
    No recibe parametros, devuelve la jugada generada. """
    jugada = sorted(random.sample(range(1, 46), 6))
    return jugada


def base_mil_jugadas():
    """ En base a mil sorteos genera un diccionario con las apariciones de cada numero.
    Devuelve el diccionario creado y genera apariciones.txt , con la misma data"""
    lista_jugadas = []
    apariciones = {}
    primeros = {}
    proximos = {}
    finales = {}

    for x in range(0, 2675):
        lista_jugadas.append(sorteo())

    for jugada in lista_jugadas:
        primeros[jugada[0]] = primeros.get(jugada[0], 0) + 1
        for i in range(len(jugada)):
            apariciones[jugada[i]] = apariciones.get(jugada[i], 0) + 1
            if i + 1 < len(jugada):
                if jugada[i] in proximos:
                    if jugada[i + 1] in proximos[jugada[i]]:
                        proximos[jugada[i]][jugada[i + 1]] += 1
                    else:
                        proximos.setdefault(jugada[i], {}).setdefault(jugada[i + 1], 1)
                else:
                    proximos.setdefault(jugada[i], {}).setdefault(jugada[i + 1], 1) + 1
            else:
                finales[jugada[i]] = finales.get(jugada[i], 0) + 1

    # with open('apariciones.txt', 'w', encoding='utf-8') as f:
    #     for clave in apariciones:
    #         f.write(f"{clave}:\t{apariciones[clave]} \n")
    #
    # with open('primeros.txt', 'w', encoding='utf-8') as f:
    #     for clave in primeros:
    #         f.write(f"{clave}:\t{primeros[clave]} \n")
    #
    # with open('proximos.txt', 'w', encoding='utf-8') as f:
    #     for clave in proximos:
    #         f.write(f"{clave}:\t{proximos[clave]} \n")
    #
    # with open('finales.txt', 'w', encoding='utf-8') as f:
    #     for clave in finales:
    #         f.write(f"{clave}:\t{finales[clave]} \n")

    return primeros, proximos, finales


def generar_boleto():
    """
    Genera un boleto de 6 numeros basado en los numeros mas salidores al principio, seguido por los
    proximos al primero con mas apariciones y asi sucesivamente hasta completarse.
    :return: boleto de 6 numeros con la opcion de guardarlo en un archivo
    """
    primeros, proximos, finales = base_mil_jugadas()
    primer_numero = random_choice(primeros)
    boleto = []

    boleto.append(primer_numero)
    sgte_numero = random_choice(proximos[primer_numero])

    boleto.append(sgte_numero)

    while len(boleto) < 6:

        if sgte_numero in proximos:
            sgte_numero = random_choice(proximos[sgte_numero])
            boleto.append(sgte_numero)
        else:
            sgte_numero = random_choice(proximos[primer_numero])

    return boleto


def generar_jugada(cantidad):
    """ Genera una jugada con la cantidad de boletos que se pasa por parametro
    devuelve una lista de boletos y permite guardarlos """

    lista_boletos = []

    for i in range(cantidad):
        lista_boletos.append(generar_boleto())
        print(lista_boletos[i])

    guardar = input('\nDesea guardar la jugada? [s/n] ')

    if guardar == 's':
        hora_actual = str(datetime.now())

        with open('boletos.txt', 'a', encoding='utf-8') as f:
            f.write(f"Jugada generada el {hora_actual}:\n")
            for boleto in lista_boletos:
                f.write(f"\t\t{lista_printable(boleto)} \n")
        return f"\nJugada guardada con éxito.!"

    elif guardar == 'n':
        return f"\nHasta luego.."


# ejecucion
cant = int(input('Cuantos boletos desea generar?'))
generar_jugada(cant)
os.system('pause')	