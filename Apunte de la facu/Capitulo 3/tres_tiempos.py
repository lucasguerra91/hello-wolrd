def a_segundos(horas, minutos, segundos):
    """ Transforma a segundos una medida de tiempo expresada en h, m y s"""
    return 3600 * horas + 60 * minutos + segundos


def main():
    """ Lee 3 tiempos con formato hh-mm-ss y los convierte a segundos """
    for x in range(3):
        print('\n\tTiempo', x+1, '.')
        h = int(input('Horas: '))
        m = int(input('Minutos: '))
        s = int(input('Segundos: '))
        print('\nSon ', a_segundos(h, m, s), 'segundos.')


main()
