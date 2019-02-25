def a_hms(segundos):
    """ Dada una duracion entera en segundos
    se la convierte a horas, minutos y segundos """
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s


def a_segundos(horas, minutos, segundos):
    """ Transforma a segundos una medida de tiempo expresada en h, m y s"""
    return 3600 * horas + 60 * minutos + segundos


def suma_intervalos(n):
    suma = 0
    for x in range(n):
        print('\nIngrese el intervalo ', x+1, ':')
        h = int(input('Hora/s'))
        m = int(input('Minuto/s'))
        s = int(input('Segundo/s'))
        temp = a_segundos(h, m, s)
        suma += temp
    return a_hms(suma)


n = int(input('Cuantos intervalos desea sumar?'))
h, m, s = suma_intervalos(n)
print('\nLa suma de los intervalos es ', h, ':', m, ':', s)

