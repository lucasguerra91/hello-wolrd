def verificar_lista(lista):
    if len(lista) > 0:
        return lista
    else:
        raise ValueError(f"No se  puede crear un vector vacio")


class Vector:
    """

    """
    def __init__(self, lista_coordenadas):
        self.coordenadas = verificar_lista(lista_coordenadas)

    def __str__(self):
        vector = '('

        for i in range(len(self.coordenadas)):
            if i == len(self.coordenadas) - 1:
                vector += str(self.coordenadas[i])
            else:
                vector += str(self.coordenadas[i]) + ','
        vector += ')'
        return vector

    def __add__(self, other):

        if len(self.coordenadas) != len(other.coordenadas):
            raise ValueError(f"No se pueden sumar vectores de diferentes dimensiones")
        vector = '('
        for i in range(len(self.coordenadas)):
            if i == len(self.coordenadas) - 1:
                vector += str(self.coordenadas[i] + other.coordenadas[i])
            else:
                vector += str(self.coordenadas[i] + other.coordenadas[i]) + ','
        vector += ')'
        return vector


# ejecucion
vector1 = Vector([3, 4])
print(vector1)
# vector2 = Vector([])
vector2 = Vector([5, 5])

vector_suma = vector1 + vector2
print(vector_suma)
print(vector1 + Vector([1, 2, 3]))