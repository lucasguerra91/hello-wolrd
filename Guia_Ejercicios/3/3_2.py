"""
    Con las funciones del 3.1 hacer un programa que dado dos intervalos en hh:mm:ss
    y devuelva su suma , tambien en hh:mm:ss
"""


def a_hms(segundos):
    """ Dada una duracion entera en segundos
    se la convierte a horas, minutos y segundos """
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s


def a_segundos(horas, minutos, segundos):
    """ Transforma a segundos una medida de tiempo expresada en h, m y s"""
    convertido = int(3600 * horas + 60 * minutos + segundos)
    return convertido


def suma_intervalos():
    print('Bienvenido.. \nPor favor, ingrese dos intervalos expresados en hh:mm:ss')
    h1 = int(input('\nPrimer intervalo \n\nHoras:'))
    m1 = int(input('Minutos:'))
    s1 = int(input('Segundos:'))

    h2 = int(input('\nSegundo intervalo \n\nHoras:'))
    m2 = int(input('Minutos:'))
    s2 = int(input('Segundos:'))

    suma = a_hms(a_segundos(h1, m1, s1) + a_segundos(h2, m2, s2))
    return suma


h, m, s = suma_intervalos()
print('\nLa suma de ambos intervalos es -> {}:{}:{}'.format(h, m, s))



