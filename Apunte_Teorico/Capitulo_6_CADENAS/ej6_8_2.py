"""
Ejercicio 6.8.2. Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
'X' debería devolver 'su clave es: XXXX'
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'
"""


def inserta_caracter():
    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    for letra in cadena:
        new_cadena += (letra + caracter)
    return new_cadena


def reemplaza_espacios():
    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    for letra in cadena:
        if letra == ' ':
            new_cadena += caracter
        else:
            new_cadena += letra
    return new_cadena


def reemplaza_digitos():
    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    for letra in cadena:
        if letra.isdigit():
            new_cadena += caracter
        else:
            new_cadena += letra
    return new_cadena


def inserta_en_digitos():
    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    contador = 0
    for letra in cadena:
        if letra.isdigit():
            if contador == 3:
                new_cadena += (caracter+letra)
                contador = 1
            else:
                new_cadena += letra
                contador += 1
        else:
            if contador == 3:
                new_cadena += (caracter + letra)
                contador = 0
            else:
                new_cadena += letra
    return new_cadena


print('Ejercicio 6.8.2')
seleccion = input('Que punto desea evaluar (a/b/c/d) ? * para terminar ')

while seleccion != '*':
    if seleccion.lower() == 'a':
        print(inserta_caracter())
    elif seleccion.lower() == 'b':
        print(reemplaza_espacios())
    elif seleccion.lower() == 'c':
        print(reemplaza_digitos())
    elif seleccion.lower() == 'd':
        print(inserta_en_digitos())

    seleccion = input('Que punto desea evaluar (a/b/c/d) ? * para terminar ')
