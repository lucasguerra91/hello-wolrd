# Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:
# a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
# tidad de coincidencias encontradas.
# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
# c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
# por parámetro y devuelva una lista con las posiciones


def buscar_elemento(lista, elemento):
    """
    :param lista: desordenada
    :param elemento: que se desea buscar
    :return: cantidad de apariciones
    """
    coincidencias = 0

    for i in range(len(lista)):
        if lista[i] == elemento:
            coincidencias += 1

    for i in range(len(lista)):
        if lista[i] == elemento:
            primer_aparicion = i+1
    
    return coincidencias, primer_aparicion


# ejecucion
lista_de_cosas = ['manzana', 1, 'pera', 'Roberto', -5, 'Otra cadena', 23, 0, True, 'pera']
elemento = 'pera'

# print(f"Apariciones de '{elemento}' en la lista : {buscar_elemento(lista_de_cosas, elemento)}")

