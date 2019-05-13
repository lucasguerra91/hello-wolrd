import csv


def imprimir_notas_alumnos(alumnos, notas):
    """
    Procesa los archivos de alumnos y notas, por cada alumno imprime todas las notas
    que corresponden
    :param alumnos: archivo con lista de alumnos en csv
    :param notas: archivo con lista de notas en csv
    :return: imprime las notas de cada alumno
    """

    with open(notas) as f_notas, open(alumnos) as f_alumnos:
        notas_csv = csv.reader(f_notas)
        alumnos_csv = csv.reader(f_alumnos)

        # saltea los encabezados
        next(notas_csv)
        next(alumnos_csv)

        # Empieza a leer
        alumno = next(alumnos_csv, None)
        nota = next(notas_csv, None)

        while alumno:
            padron, apellido, nombre, carrera = alumno
            print("{}, {} ({})".format(apellido, nombre, padron))
            if not nota or nota[0] != padron:
                print('\tNo se registran notas..')
            while nota and nota[0] == padron:
                print("\t{}:{}".format(nota[1], nota[2]))
                nota = next(notas_csv, None)
            alumno = next(alumnos_csv, None)


# ejecucion
imprimir_notas_alumnos('alumnos.csv', 'notas.csv')