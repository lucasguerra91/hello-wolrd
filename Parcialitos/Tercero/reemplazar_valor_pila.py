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


def reemplazar_valor(pila, valor_nuevo, valor_viejo):
    """ Recibe una pila, un valor nuevo que debera reemplazar en cada ocurrencia del valor viejo
        Devuelve la pila con los reemplazos, en caso de no encontrarse, devuelve la pila original"""

    if pila.esta_vacia():
        print('La pila esta vacía.')
        return

    pila_aux = Pila()

    for i in range(len(pila.items)):
        valor = pila.desapilar()

        if valor == valor_viejo:
            valor = valor_nuevo

        pila_aux.apilar(valor)

    for i in range(len(pila_aux.items)):
        pila.apilar(pila_aux.desapilar())

    return pila


pila1 = Pila()
pila1.apilar(1)
pila1.apilar(5)
pila1.apilar(9)
pila1.apilar(10)
pila1.apilar(6)
pila1.apilar(1)
pila1.apilar(1)
pila1.apilar(8)

print(pila1.items)

pila2 = reemplazar_valor(pila1, 7, 1)
print(pila2.items)