"""
    Ejercicio 6.8.4. Escribir una función que reciba una cadena que contiene un largo número en-
    tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
    '1234567890' , debe devolver '1.234.567.890'
"""


def separa_millar(c):
    new_c = ''
    contador = 1
    for index in range(len(c), 0, -1):
        if contador == 3:
            new_c += (c[len(c)-index]) + '.'
            contador = 1
        else:
            new_c += c[len(c) - index]
            contador += 1
    return new_c


cadena = input('Ingrese la cadena de numeros ')
print(separa_millar(cadena))

