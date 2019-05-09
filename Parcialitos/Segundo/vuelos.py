import csv


def crear_diccionario_vuelos(nombre_archivo):

    vuelos = {}

    with open(nombre_archivo, 'r') as f:
        archivo_csv = csv.reader(f)

        for fecha, destino, precio in archivo_csv:
            print(f'Entro al for :{destino}')
            if destino in vuelos.keys():
                if int(precio) < int(vuelos[destino][1]):
                    vuelos[destino] = (fecha, precio)
                else:
                    continue
            else:
                vuelos[destino] = (fecha, precio)
            print(f'{destino}:{vuelos.get(destino)}\n')
    return vuelos


print(crear_diccionario_vuelos('vuelos.csv'))
