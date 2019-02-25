def leer_centinela():
    return input('\nIngrese un número (* para terminar) :')


def muchos_pcn():
    # more_data = 'Si'
    centinela = leer_centinela()
    # while more_data == 'Si' or more_data == 's':
    while centinela != '*':
        x = int(centinela)
        if x > 0:
            print('Numero positivo')
        elif x == 0:
            print('Es cero')
        else:
            print('El numero es negativo')

        # more_data = input('\nDesea continuar? <Si/s - No/n>')
        centinela = leer_centinela()


muchos_pcn()
