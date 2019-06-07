""" Escribir un programa que pregunte al usuario:
     a) su nombre , y luego lo salude
     b) dos numeros y luego le muestre el producto
"""


def saludo(n):
    return 'Hola ' + n


def producto_dos_numeros(x, z):
    return x * z


print('Ejercicio 1.1 ')
nombre = input('\na)Saludo personal. \nIngrese su nombre ..')
print(saludo(nombre))

print('\nb) Multiplicación de dos términos')
a = float(input('Ingrese el primer término: '))
b = float(input('Ahora el segundo: '))
print('\nEl resultado de la multiplicación es: ' + str(producto_dos_numeros(a, b)) + '\n\n Fin.!')


