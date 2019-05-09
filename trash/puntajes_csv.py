import csv


def guardar_puntajes(nombre_archivo, puntajes):

    with open(nombre_archivo, 'w') as f:
        archivo_csv = csv.writer(f)
        archivo_csv.writerows(puntajes)


def recuperar_puntajes(nombre_archivo):
    puntajes = []

    with open(nombre_archivo, 'r') as f:
        archivo_csv = csv.reader(f)
        for nombre, puntaje, tiempo in archivo_csv:
            puntajes.append((nombre, int(puntaje), tiempo))
    return puntajes
