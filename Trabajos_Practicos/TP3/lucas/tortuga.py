import math
import pluma as p


class Tortuga:
    """
    Modela una clase Tortuga similar al modulo turtle de python
    """

    def __init__(self, x, y, orientacion, pluma, destino):
        self.x = x
        self.y = y
        self.pluma = p.Pluma()
        self.orientacion = orientacion
        self.destino = destino

    # Getters and setters

    def ubicacion(self):
        """ Devuelve las coordenadas de la ubicacion actual de la Tortuga ."""
        return self.x, self.y

    def orientacion(self):
        """ Devuelve el angulode la orientacion actual de la Tortuga ."""
        return self.orientacion

    # Metodos

    def girar_derecha(self, angulo):
        """ Gira la orientacion de la tortuga a la derecha en el angulo pasado por parametro """
        self.orientacion = (self.orientacion + angulo) % 360

    def girar_izquierda(self, angulo):
        """ Gira la orientacion de la tortuga a la izquierda en el angulo pasado por parametro """
        self.orientacion = (self.orientacion - angulo) % 360

    def avanzar(self, unidad):
        """Recibe una unidad (cuanto debe avanzar), y el nombre del archivo en
        el cual escribir.
        Actualiza la ubicacion de la tortuga y escribe en el archivo de destino
        si la pluma esta abajo-"""

        x, y = self.ubicacion()

        self.x = self.x + unidad * round(math.cos(math.radians(self.orientacion)), 2)
        self.y = self.y + unidad * round(math.sin(math.radians(self.orientacion)), 2)

        if self.pluma.esta_abajo:
            self.destino.write(f'\t<line x1="{x}" y1="{y}" x2="{self.x}" y2="{self.y}" '
                               f'stroke-width="{self.pluma.get_ancho()}" stroke="{self.pluma.get_color()}" />\n')

    def circulo(self, unidad):

        x, y = self.ubicacion()

        if self.pluma.esta_abajo:
            self.destino.write(f'\t<circle cx = "{x}" cy = "{y}" r = "{self.pluma.get_ancho()}" '
                               f'fill = "{self.pluma.get_color()}" />\n')

    def clonar(self):
        """Devuelve una nueva tortuga con la ubicacion, orientacion y estado de la tortuga actual. """
        return Tortuga(self.x, self.y, self.orientacion, self.pluma, self.destino)
