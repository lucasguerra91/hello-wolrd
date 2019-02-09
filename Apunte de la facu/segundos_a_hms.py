def a_hms(segundos):
    """ Dada una duracion entera en segundos
    se la convierte a horas, minutos y segundos """
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s


h, m, s = a_hms(3661)
print('Son', h, 'hora/s, ', m, 'minuto/s y ', s, 'segundo/s.')