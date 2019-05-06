"""
    2.2 Escribir un programa que convierta una temperatura dada en F°  a C°
    2.3 Tabla de conversion de 0° a 120° de 10 en 10
"""


def convertir_a_celsius(f):
    celsius = (f - 32) * (5 / 9)
    return int(celsius)


def convertir_a_fahrenheit(c):
    fahrenheit = (c * (9 / 5)) + 32
    return int(fahrenheit)


# temperatura_f = float(input('Ingrese la temperatura en Fahrenheit '))
# print(convertir_a_celsius(temperatura_f))
#
# temperatura_c = float(input('Ingrese la temperatura en grados Celsius '))
# print(convertir_a_fahrenheit(temperatura_c))


print('\nTabla de conversion de Fahrenheit a Celsius ')
for i in range(0, 121, 10):
    print('{}°F \t-\t {}°C'.format(i, convertir_a_celsius(i)))


print('\nTabla de conversion de Celsius a Fahrenheit ')
for j in range(0, 121, 10):
    print('{}°C \t-\t {}°F'.format(j, convertir_a_fahrenheit(j)))


