def es_positivo():
    x = int(input('Ingrese un numero'))
    if x > 0:
        print('El numero', x, 'es positivo')
    elif not x:
            print('El numero ingresado es cero')
    else:
        print('El numero', x, ' es negativo')


es_positivo()
