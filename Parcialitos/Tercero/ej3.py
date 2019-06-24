class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class ListaEnlazadaOrdenada:
    """
    Modela el comportamiento de una lista enlazada
    ordenada.
    """

    def __init__(self):
        self.primero = None

    def insertar_ordenado(self, x):
        """
        Recibe un valor y lo introduce en la lista antes de su mayor.
        De no encontrarlo lo guarda al final
        :return:
        """

        nodo = Nodo(x)


        if not self.primero:
            self.primero = nodo
            return

        if nodo.dato < self.primero.dato:
            nodo.prox = self.primero
            self.primero = nodo
            return

        act = self.primero

        while act.prox and nodo.dato > act.prox.dato:
            act = act.prox

        nodo.prox = act.prox
        act.prox = nodo

        return

    def __str__(self):
        """ Genera una salida legible de lo que contiene la lista, similar a las listas de Python"""
        lista = []
        actual = self.primero
        while actual:
            lista.append(str(actual))
            actual = actual.prox
        return str(lista)


# ejecucion
lista_ordenada = ListaEnlazadaOrdenada()
lista_ordenada.insertar_ordenado(9)
lista_ordenada.insertar_ordenado(5)
lista_ordenada.insertar_ordenado(4)
lista_ordenada.insertar_ordenado(3)
lista_ordenada.insertar_ordenado(8)
lista_ordenada.insertar_ordenado(6)

print(lista_ordenada)