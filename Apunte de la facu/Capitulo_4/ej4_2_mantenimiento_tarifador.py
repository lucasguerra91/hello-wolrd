def main():
    """ El usuario ingresa la tarifa por segundo, cuantas comunicaciones
    se realizaron, y la duracion de cada comunicacion expresada en horas, minutos
    y segundos. Como resultado se informa la duracion en segundos de cada comunicacion y su costo """
    print('-----------------------------------  ')
    print('Configuración de las tarifas')
    print('-----------------------------------  ')
    p = float(input('Tarifa por segundo en llamadas cortas:'))
    p2 = float(input('Tarifa por segundo en llamadas largas:'))
    cortas = int(input('Limite en segundos de llamadas cortas: '))
    print('-----------------------------------  ')
    n = int(input('Cuantas comunicaciones hubo? :'))
    costo_total = 0
    costo_cortas = 0
    cantidad_cortas = 0
    cantidad_largas = 0
    costo_largas = 0

    for x in range(n):
        print('-----------------------------------  ')
        print('\nLlamada #', x+1)
        h = int(input('\nCuantas horas? : '))
        m = int(input('Cuantos minutos? : '))
        s = int(input('Cuantos segundos? : '))
        duracion = a_segundos(h, m, s)
        if duracion <= cortas:
            costo = duracion * p
            print('\nResumen de llamada')
            print('Duración :', duracion, 'segundos. Costo: $', costo)
            cantidad_cortas += 1
            costo_cortas += costo
        else:
            costo = duracion * p2
            print('\nResumen de llamada')
            print('Duración :', duracion, 'segundos. Costo: $', costo)
            cantidad_largas += 1
            costo_largas += costo

        costo_total += costo
    print('\n\n###################################')
    print('###### REPORTE DE LLAMADAS ########')
    print('###################################\n\n')
    print('Cantidad de llamadas cortas: ', cantidad_cortas)
    print('Costo de llamadas cortas: ', costo_cortas)
    print('\nCantidad de llamadas largas: ', cantidad_largas)
    print('Costo de llamadas largas: ', costo_largas)
    print('-----------------------------------  ')
    print('\n\nEl costo total de su factura es de: $', costo_total)


def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo indicada en horas
    , minutos y segundos"""
    return 3600 * horas + 60 * minutos + segundos

main()