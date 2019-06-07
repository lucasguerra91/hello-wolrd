""" Imprimir los numeros triangulares correspondientes al
    numero que ingrese el usuario por consola """


def imprime_triangulares(x):
    suma = 0
    cont = 0
    for i in range(x+1):
        suma += i
        cont += 1
    print(x, ' - ', suma, '\n Cantidad de operaciones: {} \n'.format(cont))


def triangulares_formula(m):
    i = m * (m + 1) / 2
    print(m, ' - ', int(i), '\n Cantidad de operaciones: 1')


numero = int(input('\nIngrese el numero que desea evaluar: '))
imprime_triangulares(numero)
triangulares_formula(numero)