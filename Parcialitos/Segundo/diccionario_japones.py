
def traductor_japones(cadena):
    """

    :param cadena:
    :return:
    """
    diccionario_japones = {
        'hi': 'Dia',
        'arigatou': 'Gracias',
    }
    cadena_traducida = ''
    palabras = cadena.split()
    print(len(palabras))
    for i in range(0, len(palabras)):
        for clave in diccionario_japones:
            if diccionario_japones[clave] == palabras[i]:
                cadena_traducida += clave + ' '
    return cadena_traducida


def escribir_archivo(cadena, ruta, funcion):
    """

    :param ruta:
    :return:
    """
    traduccion = funcion(cadena)
    palabras_traduccion = traduccion.rstrip('\n').split()
    palabras = cadena.split()
    # print(palabras)
    # print(palabras_traduccion)
    print(len(palabras_traduccion))
    print(len(palabras))

    for i in range(len(palabras)):
        if len(palabras_traduccion[i]) < len(palabras[i]):
            with open(ruta, 'a') as f:
                f.write(palabras_traduccion[i]+'\n')
        else:
            continue


# ejecucion
escribir_archivo('Dia Gracias', 'traduccion.txt', traductor_japones)
