class Punto:
    """
    Representacion de un punto en un plano de coordenadas cartesianas (x, y)
    """

    def __init__(self, x, y):
        """ Constructor del punto """
        self.x = validar_numero(x)
        self.y = validar_numero(y)

    def distancia(self, otro):
        return self.restar(otro).norma()

    def restar(self, otro):
        """Devuelve el Punto que resulta de la resta
        entre dos puntos."""
        return Punto(self.x - otro.x, self.y - otro.y)

    def norma(self):
        """Devuelve la norma del vector que va desde el origen
        hasta el punto. """
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        """Devuelve la representación formal del Punto como
        cadena de texto."""
        return "Punto({}, {})".format(self.x, self.y)

    def __add__(self, otro):
        """Devuelve la suma de ambos puntos."""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """Devuelve la resta de ambos puntos."""
        return Punto(self.x - otro.x, self.y - otro.y)


def validar_numero(valor):
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor} no es un valor numerico")
    return valor


# Ejecucion
punto = Punto(5, 7)
print(type(punto))

punto1 = Punto(10, 3)
print(type(punto1))

print(punto.distancia(punto1))
print(punto.norma())

print(punto)

print(repr(punto))