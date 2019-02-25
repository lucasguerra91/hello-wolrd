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


print('\nDuracion en segundos a partir de hora/s , minuto/s y segundo/s ')
h = int(input('Ingrese la cantidad de hora/s :'))
m = int(input('Ingrese la cantidad de minuto/s :'))
s = int(input('Ingrese la cantidad de segundo/s :'))
print('\nLa duración en segundos es de :', a_segundos(h, m, s))

print('\nDuración en h/m/s de un intervalo dado en segundos..')
s = int(input('Indique el intervalo en segundos : '))
h, m, s = a_hms(s)
print('\nEl intervalo equivale a ', h, ':', m, ':', s, '.')

