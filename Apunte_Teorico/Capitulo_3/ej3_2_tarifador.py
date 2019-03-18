def main():
    """ El usuario ingresa la tarifa por segundo, cuantas comunicaciones
    se realizaron, y la duracion de cada comunicacion expresada en horas, minutos
    y segundos. Como resultado se informa la duracion en segundos de cada comunicacion y su costo """

    p = float(input('Tarifa por segundo de comunicación :'))
    n = int(input('Cuantas comunicaciones hubo? :'))
    costo_total = 0
    for x in range(n):
        h = int(input('\n\nCuantas horas? : '))
        m = int(input('Cuantos minutos? : '))
        s = int(input('Cuantos segundos? : '))
        duracion = a_segundos(h, m, s)
        costo = duracion * p
        print('Duración :', duracion, 'segundos. Costo: $', costo)
        costo_total += costo
    print('\nEl costo total de su factura es de: $', costo_total)


def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo indicada en horas
    , minutos y segundos"""
    return 3600 * horas + 60 * minutos + segundos

main()