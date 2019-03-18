def cuadrado(n):
    return n * n


def cuadrados_de_intervalo(n1, n2):
    for x in range(n1, n2):
        print(x, 'su cuadrado es : ', cuadrado(x))


print('Bienvenido, bla bla bla')
n1 = int(input('Introduzca el primer numero entero..'))
n2 = int(input('Muy bien, ahora el segundo por favor.. '))
cuadrados_de_intervalo(n1, n2)
print('Eso es todo.. ')
