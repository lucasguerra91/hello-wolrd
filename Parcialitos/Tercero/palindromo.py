from Parcialitos.Tercero import cola as c
from Parcialitos.Tercero import pila as p


def es_palindromo(cola, longitud):
    """
    :param cola: cola que contiene palabra o cadena
    :param longitud: cantidad de elementos de la cola
    :return: True or False si es o no palindromo
    """

    if cola.esta_vacia():
        return False

    aux = p.Pila()

    for i in range(longitud // 2):
        aux.apilar(cola.desencolar())

    # saco el del medio
    cola.desencolar()

    while not cola.esta_vacia():
        a = cola.desencolar()
        b = aux.desapilar()

        print(f"{a} {b}")

        if a != b:
            return False

    return True


# ejecucion

palabra = c.Cola()

palabra.encolar("n")
palabra.encolar("e")
palabra.encolar("u")
palabra.encolar("q")
palabra.encolar("u")
palabra.encolar("e")
palabra.encolar("n")

print(palabra)
print(es_palindromo(palabra, 7))
