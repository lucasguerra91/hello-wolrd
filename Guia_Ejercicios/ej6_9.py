import os

""" Implementar la funcion pedir_entero(mensaje, min, max) que debe imprimir el mensaje y luego esperar
    a que el usuario ingrese un valor. SI el valor ingresado NO es un numero entero entre min y max (inclusive)
    se le debe avisar al usuario y pedir el ingreso de otro valor """


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_numero(mensaje, minimo, maximo):
    entrada = input(mensaje)
    paciencia = 1
    while not entrada.lstrip('-').isdigit():
        limpiar_pantalla()
        if paciencia <= 3:
            print('El valor ingresado no corresponde, intentémoslo otra vez ..')
            entrada = input(mensaje)
            paciencia += 1
        else:
            print('Vamos, solo tiene que ingresar un entero entre {} y {}'.format(minimo, maximo))
            entrada = input(mensaje)
            paciencia = 1

    if (int(entrada) > minimo) and (int(entrada) <= maximo):
        return int(entrada)
    limpiar_pantalla()
    print('Ok, al menos ahora ingresaste un entero.. volvamos a intentarlo..')
    return pedir_numero(mensaje, minimo, maximo)


edad = pedir_numero('Hola, cuantos años tenes [0 - 150]? ', 0, 150)
print('DEBUG >>> EDAD = {}'.format(edad))

numero = pedir_numero('Hola, pasame un entero entre -5 y 55 ', -5, 55)
print('DEBUG >>> numero = {}'.format(numero))

