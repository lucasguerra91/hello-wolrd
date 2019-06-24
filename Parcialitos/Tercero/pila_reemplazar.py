class Pila:
    """Representa una pila con operaciones de apilar, desapilar y
    verifica si esta vacia """

    def __init__(self):
        """ Crea una pila vacia """
        self.items = []

    def __str__(self):
        return str(self.items)

    def esta_vacia(self):
        """ Devuelve True si la lista esta vacia, False si no.. """
        return len(self.items) == 0

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila esta vacia levanta una excepcion """
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self.items.pop()


def reemplazar(pila, valor_nuevo, valor_viejo):
    """
    Recibe una pila, reemplaza en ella las apariciones de valor_viejo por valor_nuevo
    :param pila: instancia de Pila
    :param valor_nuevo: Que reemplaza a valor viejo, si el mismo esta en la Pila
    :param valor_viejo: No hace falta explicarlo tanto
    """
    if pila.esta_vacia():
        return

    p_aux = Pila()

    while not pila.esta_vacia():
        actual = pila.desapilar()
        if actual == valor_viejo:
            p_aux.apilar(valor_nuevo)
        else:
            p_aux.apilar(actual)

    while not p_aux.esta_vacia():
        pila.apilar(p_aux.desapilar())


# ejecucion
pila = Pila()
pila.apilar(1)
pila.apilar(3)
pila.apilar(4)
pila.apilar(1)
pila.apilar(3)

print(pila)
pila2 = Pila()
reemplazar(pila2, 7, 4)

print(pila)
