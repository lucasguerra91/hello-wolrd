class Cola:
    """Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado."""

    def __init__(self):
        """ Crea una cola vacia """
        self.items = []

    def encolar(self, x):
        """ Encola el elemento x """
        self.items.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su valor,
        Si la cola esta vacía, levanta ValueError """

        if self.esta_vacia():
            raise ValueError("La cola esta vacía.")
        return self.items.pop(0)

    def esta_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no """
        return len(self.items) == 0


