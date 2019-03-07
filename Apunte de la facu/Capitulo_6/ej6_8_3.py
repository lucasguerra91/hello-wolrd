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

    Ejercicio 6.8.3. Modificar las funciones anteriores, para que reciban un parámetro que indique
        la cantidad máxima de reemplazos o inserciones a realizar.
"""
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def inserta_caracter(c):
    """ Inserta un caracter entre cada componente de la cadena. El caracter y la cadena son introducidos por el usuario
    una vez iniciada la función. La cantidad de interacciones se define antes de la llamada a función y la misma
    es pasada como parámetro """

    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    contador = 1
    for letra in cadena:
        if contador <= c:
            new_cadena += (letra + caracter)
            contador += 1
        else:
            new_cadena += letra
    return new_cadena


def reemplaza_espacios(c):
    """ Reemplaza los espacios presentes en la cadena por un caracter. El caracter y la cadena son introducidos por el
        usuario una vez iniciada la función. La cantidad de interacciones se define antes de la llamada a función y la
        misma es pasada como parámetro """

    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    contador = 1

    for letra in cadena:
        if contador <= c:
            if letra == ' ':
                new_cadena += caracter
                contador += 1
            else:
                new_cadena += letra
        else:
            new_cadena += letra
    return new_cadena


def reemplaza_digitos(c):
    """ Reemplaza con un caracter los digitos presentes en la cadena. El caracter y la cadena son introducidos por el
        usuario una vez iniciada la función. La cantidad de interacciones se define antes de la llamada a función y
        la misma es pasada como parámetro """

    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    contador = 1
    for letra in cadena:
        if contador <= c:
            if letra.isdigit():
                new_cadena += caracter
                contador += 1
            else:
                new_cadena += letra
        else:
            new_cadena += letra
    return new_cadena


def inserta_en_digitos(c):
    """ Inserta un caracter luego de cada dígito presente en la cadena. El caracter y la cadena son introducidos por
        el usuario una vez iniciada la función. La cantidad de interacciones se define antes de la llamada a función
        y la misma es pasada como parámetro """

    cadena = input('Ingrese la cadena:')
    caracter = input('Ingrese el caracter que desea añadir :')
    new_cadena = ''
    contador = 0
    interacciones = 1
    for letra in cadena:
        if interacciones <= c:
            if letra.isdigit():
                if contador == 3:
                    new_cadena += (caracter+letra)
                    contador = 1
                    interacciones += 1
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


print('Ejercicio 6.8.2 - Apunte Teórico')
# Usamos el legendario centinela (( 0___o ))
seleccion = input('Que punto desea evaluar (a/b/c/d) ? * para terminar ')
if seleccion != '*':
    cantidad = int(input('Ingrese el limite de interacciones que desea realizar'))

while seleccion != '*':
    # Simulacro de switch para acceder a las distintas funciones
    if seleccion.lower() == 'a':
        cls()
        print(inserta_caracter(cantidad))
    elif seleccion.lower() == 'b':
        cls()
        print(reemplaza_espacios(cantidad))
    elif seleccion.lower() == 'c':
        cls()
        print(reemplaza_digitos(cantidad))
    elif seleccion.lower() == 'd':
        print(inserta_en_digitos(cantidad))
    cls()

    seleccion = input('Que punto desea evaluar (a/b/c/d) ? * para terminar ')
    if seleccion != '*':
        cantidad = int(input('Ingrese el limite de interacciones que desea realizar'))
