from Parcialitos.Tercero import nodo as n


class ListaEnlazada:
    """ Modela una lista enlazada"""

    def __init__(self):
        """ Crea una lista enlazada vacia"""
        # referencia al primer nodo (None si la lista esta vacia)
        self.prim = None
        # referencia al ultimo
        self.ultimo = None
        # cantidad de elementos de la lista
        self.len = 0

    def __len__(self):
        return self.len

    # Ejercicio 11.6
    def __str__(self):
        """ Genera una salida legible de lo que contiene la lista, similar a las listas de Python"""
        lista = []
        actual = self.prim
        while actual:
            lista.append(str(actual))
            actual = actual.prox
        return str(lista)

    def esta_vacia(self):
        if self.prim:
            return False
        return True

    def append(self, x):
        """ Agrega un elemento al final ; si la lista esta vacia se actualiza el primero y el ultimo"""
        # print(f"DEBUGG : ENTRO {x}")
        nuevo = n.Nodo(x)

        if self.esta_vacia():
            self.prim = self.ultimo = nuevo
        else:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        self.len += 1

    def suma_acumulativa(self):
        """ Devuelve una nueva lista con la suma acumulativa de cada nodo respecto a los anteriores """

        nueva_lista = ListaEnlazada()

        if self.esta_vacia():
            return nueva_lista

        suma_ac = self.prim.dato
        nodo = n.Nodo(suma_ac)
        nueva_lista.prim = nodo

        actual = self.prim
        actual_nueva = nueva_lista.prim

        while actual.prox:
            suma_ac += actual.prox.dato
            nodo = n.Nodo(suma_ac)
            actual_nueva.prox = nodo

            actual = actual.prox
            actual_nueva = actual_nueva.prox

        return nueva_lista


# test
lista1 = ListaEnlazada()
lista1.append(7)
lista1.append(8)
lista1.append(10)
lista1.append(1)
lista1.append(5)

print(lista1)

lista2 = lista1.suma_acumulativa()

print(lista2)
