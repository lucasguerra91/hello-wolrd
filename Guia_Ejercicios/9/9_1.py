# Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
# en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
# segundos.


def tuplas_a_diccionarios(lista):
    """
    Recibe una lista de tuplas y devuelve un diccionario utilizando los valores de las tuplas
    :param lista: de dos items (seran clave - valor en el diccionario)
    :return: un diccionario con los items de las tuplas
    """
    diccionario = {}

    for i in range(len(lista)):
        clave, valor = lista[i]
        if clave in diccionario.keys():
            diccionario[clave].append(valor)
        else:
            diccionario[clave] = [valor]
    return diccionario


def imprimir_diccionario(diccionario):
    for clave in diccionario.keys():
        print(f'{clave}:{diccionario.get(clave, None)}')


# ciclo de ejecucion
test_lista = [('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días'), ('Buenas', 'tardes'),
              ('Buenas', 'noches'), ('Hoy', 'me baño'), ('Buenos', 'hospitales')]
dic_1 = tuplas_a_diccionarios(test_lista)
imprimir_diccionario(dic_1)
