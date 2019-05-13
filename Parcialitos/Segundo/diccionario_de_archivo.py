def crear_diccionario(archivo):
    """

    :param archivo:
    :return:
    """

    diccionario = {}

    try:
        with open(archivo, 'r') as file:
            for linea in file:
                linea = linea.rstrip("\n")
                cadena = linea.split('-')
                departamento, materia = cadena[0].split('.')
                # print(departamento, materia)

                if departamento in diccionario.keys():
                    diccionario[departamento].append(materia)
                else:
                    diccionario[departamento] = [materia]
            return diccionario
    except:
        print('Error')


# ejecucion
print(crear_diccionario('notas.txt'))