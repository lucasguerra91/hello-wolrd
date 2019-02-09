import saludos


def main():
    nombre = input('Cual es tu nombre?')
    print(saludos.hola(nombre))
    print(saludos.adios(nombre))


main()

