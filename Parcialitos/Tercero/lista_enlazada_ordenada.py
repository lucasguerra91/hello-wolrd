from Parcialitos.Tercero import nodo as n


class ListaEnlazadaOrdenada:

    def __init__(self):
        self.primero = None

    def __str__(self):
        """ Genera una salida legible de lo que contiene la lista, similar a las listas de Python"""
        lista = []
        actual = self.primero
        while actual:
            lista.append(str(actual))
            actual = actual.prox
        return str(lista)

    def insertar_ordenado(self, x):

        nodo = n.Nodo(x)

        if not self.primero:
            self.primero = nodo
            return

        if nodo.dato < self.primero.dato:
            nodo.prox = self.primero
            self.primero = nodo
            return

        ant = self.primero
        act = self.primero.prox

        while act:
            if nodo.dato < act.dato:
                ant.prox = nodo
                nodo.prox = act
                return

            ant = act
            act = act.prox

        ant.prox = nodo


# ejecucion
leo = ListaEnlazadaOrdenada()

leo.insertar_ordenado(4)
leo.insertar_ordenado(1)
leo.insertar_ordenado(5)
leo.insertar_ordenado(1)
leo.insertar_ordenado(6)
leo.insertar_ordenado(3)
leo.insertar_ordenado(9)
leo.insertar_ordenado(7)
leo.insertar_ordenado(8)
leo.insertar_ordenado(10)
leo.insertar_ordenado(0)

print(leo)



