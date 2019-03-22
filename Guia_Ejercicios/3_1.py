"""
    a) que escriba la duracion en segundos de un intervalo dado en h m s
    b) al reves 
"""


def a_hms():
    """ Dada una duracion entera en segundos
    se la convierte a horas, minutos y segundos """

    segundos = int(input('\nIngrese el intervalo expresado en segundos:'))
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    print('\nSu equivalente es {}:{}:{}'.format(h, m, s))


def a_segundos():
    """ Transforma a segundos una medida de tiempo expresada en h, m y s"""
    print('\nIngrese el intervalos expresado en hh:mm:ss')
    horas = int(input('\nHoras:'))
    minutos = int(input('\nMinutos:'))
    segundos = int(input('\nSegundos:'))
    convertido = int(3600 * horas + 60 * minutos + segundos)
    print('\nSu equivalente es : {} segundos'.format(convertido))


a_hms()
a_segundos()

