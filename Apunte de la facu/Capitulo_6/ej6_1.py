c = 'Empieza el ritual'

# Primero lo imprimo desde el inicio al final seria lo mismo que print(cadena)
print(c[:len(c)])
# print(cadena)
# Ahora lo imprimo leyendo de atras para adelante, pero se visualiza igual
print(c[- len(c):len(c)])
# Por ultimo la imprimo al reves con la funcion [start:stop:step]
print(c[::-1])


def contar_apariciones(s, l):
    """ Recibe como parametro la cadena y la letra que se desea buscar,
    devuelve la cantidad de apariciones de la misma discrimina A de a"""
    contador = 0
    for letra in s:
        if letra == l:
            contador += 1
    return contador


def contar_apariciones_2(s, l):
    """ Recibe como parametro la cadena y la letra que se desea buscar,
    devuelve la cantidad de apariciones de la misma sea A o a"""
    contador = 0
    for letra in s:
        if letra == l.upper() or letra == l.lower():
            contador += 1
    return contador


def compara_apariciones(c1, l1, l2):
    cantidad1 = contar_apariciones(c1, l1)
    cantidad2 = contar_apariciones(c1, l2)
    if cantidad1 > cantidad2:
        print('Hay mas apariciones de la letra ', l1)
    elif cantidad2 > cantidad1:
        print('Hay mas apariciones de la letra ', l2)
    else:
        print('Aparecen la misma cantidad de veces')


cadena = 'lA viejA DE a la vueltA se sAbe todasj'
print(contar_apariciones(cadena, 'a'))
print(contar_apariciones_2(cadena, 'a'))
print(compara_apariciones(cadena, 'v', 'j'))
