def leer_centinela():
    return input('\nIngrese la tarifa de la llamada (* para terminar) :')


def a_segundos(horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo indicada en horas
    , minutos y segundos"""
    return 3600 * horas + 60 * minutos + segundos


def main():
    """   se informa la tarifa por segundo y la duración de cada comunicación expresada en horas,
    minutos y segundos. Como resultado se informa la duración en segundos de cada llamado y su costo"""
    contador_llamadas = 0
    costo_total = 0
    centinela = leer_centinela()

    while centinela != '*':
        p = float(centinela)
        print('-----------------------------------  ')
        h = int(input('\nCuantas horas? : '))
        m = int(input('Cuantos minutos? : '))
        s = int(input('Cuantos segundos? : '))
        duracion = a_segundos(h, m, s)
        costo = duracion * p
        print('\nResumen de llamada')
        print('Duración :', duracion, 'segundos. Costo: $', costo)
        costo_total += costo
        contador_llamadas += 1
        centinela = leer_centinela()

    print('\n\n###################################')
    print('###### REPORTE DE LLAMADAS ########')
    print('###################################\n')
    print('Hubo un total de', contador_llamadas, 'llamada/s con un costo total de: $', costo_total, '\n')
    print('-----------------------------------  ')

main()


