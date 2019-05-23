from nodo import Nodo


class Cola:
    def __init__(self):
        """ Crea una cola vacia """
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        """ Encola el elemento x """
        nuevo = Nodo(x)

        if self.ultimo is not None:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.primero = nuevo
            self.ultimo = nuevo
    