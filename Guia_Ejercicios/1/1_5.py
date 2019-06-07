""" Implementar algoritmos que resuelvan :
    a) dados dos numeros imprimir su : suma, resta , div, mult
        de ambos.
    b) Dado un numero entero n, imprimir su tabla de multiplicar
"""


def operaciones_dos_numeros(a, b):
    print('\nSuma: {} \nResta: {} \nMultiplicación: {} \nDivisión: {}'.format((a+b), (a-b), (a*b), (a/b)))


def tabla_multiplicar(n):
    for i in range(1, 11):
        print('{} a la {} : {}'.format(n, i, i*n))


print('\na) Operaciones con un par de enteros dados..')
numero1 = int(input('Ingrese el primer número:'))
numero2 = int(input('Ahora ingrese el segundo:'))
operaciones_dos_numeros(numero1, numero2)

print('\nb) Tabla de multiplicar de un entero dado.. \n')
numero_entero = int(input('Ingrese un numero entero :'))
tabla_multiplicar(numero_entero)
