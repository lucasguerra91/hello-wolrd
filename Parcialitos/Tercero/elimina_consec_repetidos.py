class Pila:
    """Representa una pila con operaciones de apilar, desapilar y
    verifica si esta vacia """

    def __init__(self):
        """ Crea una pila vacia """
        self.items = []

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

    def __str__(self):
        return str(self.items)


def elimina_consecutivos_repetidos(pila):
    """ Elimina los consecutivos repetidos de la pila, actualizandola.  """
    if pila.esta_vacia():
        print("La pila está vacía.")
        return

    pila_aux = Pila()
    ultimo_agregado = pila.desapilar()
    pila_aux.apilar(ultimo_agregado)

    while not pila.esta_vacia():
        dato = pila.desapilar()

        if dato != ultimo_agregado:
            pila_aux.apilar(dato)
            ultimo_agregado = dato

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())


# ciclo ejecucion
pila = Pila()
pila.apilar(2)
pila.apilar(8)
pila.apilar(8)
pila.apilar(8)
pila.apilar(3)
pila.apilar(3)
pila.apilar(2)
pila.apilar(3)
pila.apilar(3)
pila.apilar(3)
pila.apilar(1)
pila.apilar(7)

print(pila)
elimina_consecutivos_repetidos(pila)
print(pila)

