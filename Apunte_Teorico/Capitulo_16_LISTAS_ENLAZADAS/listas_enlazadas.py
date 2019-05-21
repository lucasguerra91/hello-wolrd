class _Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class ListaEnlazada:
    """ Modela una lista enlazada"""

    def __init__(self):
        """ Crea una lista enlazada vacia"""
        # referencia al primer nodo (None si la lista esta vacia)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        lista = []
        actual = self.prim

        while actual:
            lista.append(str(actual))
            # print(f"DEBUGG - se guardo {str(actual)} en la lista")
            actual = actual.prox
            # print(f"DEBUGG - el actual es {str(actual)}")

        return str(lista)

    def pop(self, i=None):
        """ Elimina el nodo en la posicion i, y devuelve el dato contenido.
        Si i esta fuera de rango, se levanta la excepcion IndexError
        Si no se recibe la posicion, devuelve el ultimo elemento"""

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError('Indice fuera de rango')

        if i == 0:
            # caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox 

            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox

            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox

        self.len -= 1
        return dato

    def remove(self, x):
        """Borra la primera aparicion del valor x en la lista.
        Si x no esta en la lista, levanta ValueError"""

        if self.len == 0:
            raise ValueError("Lista vacía")

        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Busca el nodo anterior al que contiene x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox

            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox

            if not n_act:
                raise ValueError("El valor no esta en la lista")

            # Descartar el nodo (nunca se borra en realidad)
            n_ant.prox = n_act.prox
        self.len -= 1

    def insertar(self, i, x):
        """ Inserta el elemento x en la posicion i.
        Si la posicion es invalida, levanta IndexError"""

        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')

        nuevo = _Nodo(x)

        if i == 0:
            # Caso particular, insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posicion deseada
            n_ant = self.prim

            for pos in range(1, i):
                n_ant = n_ant.prox

            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        self.len -= 1

    def append(self, x):
        """ Agrega un elemento al final """
        print(f"DEBUGG : ENTRO {x}")
        nuevo = _Nodo(x)
        if self.prim:
            n_act = self.prim

            while n_act.prox:
                n_ant = n_act
                n_act = n_ant.prox

            n_act.prox = nuevo

        else:
            self.prim = nuevo

        self.len += 1

    def existe_lista(self):
        if self.prim:
            return True
        return False

    def __index__(self, x):
        """ Busca el indice de la primer aparicion de x dentro de la lista, si no esta
        levanta ValueError"""
        if self.existe_lista():
            pos = 0
            actual = self.prim

            while actual:
                if actual.dato == x:
                    return pos
                actual = actual.prox
                pos += 1

            raise ValueError(f"{x} no se encuentra dentro de la lista")

        else:
            raise ValueError("Lista vacía.")


li = ListaEnlazada()

li.append('Hola')
li.append(5)
li.append('como')

print(li)
print(li.__index__('como'))
