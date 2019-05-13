class Perchero:
    """
    Describe un perchero de atributos : inventario, espacio total,
    espacio disponible.
    Metodos: colgar prenda, sacar prenda, mostrar inventario
    """

    def __init__(self, espacio):
        self.espacio_total = validar_numero(espacio)
        self.espacio_disponible = validar_numero(espacio)
        self.inventario = {}

    def colgar(self, prenda, espacio):

        try:
            if espacio <= self.espacio_disponible:
                self.espacio_disponible -= espacio

                if prenda in self.inventario.keys():
                    self.inventario[prenda][0] += 1
                    self.inventario[prenda][2] += espacio
                else:
                    self.inventario[prenda] = [1, espacio, espacio]
                print(f'LOGG:{prenda} colgada con exito')
            else:
                raise Exception
        except:
            print(f'No hay espacio para colgar {prenda}')

    def sacar(self, prenda):
        try:
            if prenda.lower() in self.inventario.keys():
                self.inventario[prenda][0] -= 1
                self.inventario[prenda][2] -= self.inventario[prenda][1]
                self.espacio_disponible += self.inventario[prenda][1]

                if self.inventario[prenda][0] == 0:
                    self.inventario.pop(prenda, None)
                    print(f"LOGG: Se sacó {prenda} del inventario..")
            else:
                raise Exception
        except:
            print(f"La prenda no se encuentra en el inventario")

    def imprimir_disponible(self):
        return f"El perchero tiene {self.espacio_disponible} espacios disponible/s"

    def imprimir_inventario(self):
        print(f"\n\t\tINVENTARIO PERCHERO")
        for clave in self.inventario.keys():
            print(f'\n{clave.upper()} \n\tCantidad : {self.inventario[clave][0]}'
                  f'\n\tEspacio Unitario : {self.inventario[clave][1]}'
                  f'\n\tEspacio Total : {self.inventario[clave][2]}')


class Prenda:
    """Modela una prenda, nombre y espacio que ocupa"""

    def __init__(self, nombre, espacio):
        self.nombre = validar_cadena(nombre)
        self.espacio = validar_numero(espacio)

    def __str__(self):
        return f"({self.nombre},{self.espacio})"


def validar_numero(valor):
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor} no es un valor numerico")
    return valor


def validar_cadena(valor):
    if not isinstance(valor, str):
        raise TypeError(f"{valor} no es una cadena")
    return valor


# Ejecucion
p = Perchero(4)

remera = Prenda('remera', 1)
campera = Prenda('campera', 2)

p.colgar(remera.nombre, remera.espacio)
p.colgar(campera.nombre, campera.espacio)
p.colgar(remera.nombre, remera.espacio)
p.colgar(remera.nombre, remera.espacio)
p.colgar(campera.nombre, campera.espacio)

p.sacar('remera')
p.sacar('remera')
p.sacar('remera')

p.imprimir_inventario()
