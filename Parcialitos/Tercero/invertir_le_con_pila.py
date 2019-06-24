from Parcialitos.Tercero import lista_enlazada as le
from Parcialitos.Tercero import pila as p
from Parcialitos.Tercero import nodo as n


def invertir_lista(lista):
    """

    :param lista:
    :return:
    """
    if lista.esta_vacia() or not lista.prim.prox :
        return

    pila = p.Pila()

    while not lista.esta_vacia():
        dato = lista.prim.dato
        pila.apilar(dato)
        lista.prim = lista.prim.prox

    while not pila.esta_vacia():
        nodo = n.Nodo(pila.desapilar())

        if lista.esta_vacia():
            lista.prim = nodo

        else:
            actual = lista.prim

            while actual.prox:
                actual = actual.prox

            actual.prox = nodo


# Ejecucion
le1 = le.ListaEnlazada()
le1.insertar_al_final(1)
le1.insertar_al_final(2)
le1.insertar_al_final(3)
le1.insertar_al_final(5)
le1.insertar_al_final(6)
le1.insertar_al_final(7)
le1.insertar_al_final(8)
le1.insertar_al_final(9)

print(le1)

invertir_lista(le1)

print(le1)

le2 = le.ListaEnlazada()
print(le2)