def repite_hola(n):
    """ Lo unico que hace esta funcion es imprimir hola las veces que vos le digas """
    for x in range(n):
        print('Hola')


def repite_hola2(m):
    """ Esta funcion concatena n veces la palabra Hola . Parametros requeridos : cantidad"""
    cadena = 'Hola'
    # print(cadena) Debug like a boss haha
    for x in range(1, m):
        cadena += 'Hola'
        # print(cadena)
    # print(cadena)
    return cadena


def repite_saludo2(saludo, veces):
    """ Esta funcion concatena n veces el saludo. Parametros requeridos : saludo , veces """
    cadena = saludo
    for x in range(1, veces):
        cadena += saludo
    return cadena


def repite_saludo(saludo, veces):
    """ Esta funcion muestra un saludo ingresado por el legendario usuario , la cantidad de veces que este indique """
    for i in range(1, veces+1):
        print(saludo)


n = int(input('Ingrese la cantidad de veces que quiere repetir el jodido "Hola" :'))
repite_hola(n)
# Ejercicio 3.2
m = int(input('Ingrese la cantidad de veces que quiere concatenar el jodido "Hola" :'))
print(repite_hola2(m))

# Ejercicio 3.3
print('Aca lo que pide es que se entre por teclado un saludo y la cantidad de veces que lo vamos a repetir')
saludo = input('Ingrese el saludo que desea enviar al mundo')
veces = int(input('Ingrese cuantas veces le gustaria saludar al mundo'))
repite_saludo(saludo, veces)

# Ejercicio 3.4
saludo2 = input('Ingrese el saludo que desea enviar al mundo')
veces2 = int(input('Ingrese cuantas veces le gustaria concatenar este saludo'))
print(repite_saludo2(saludo2, veces2))