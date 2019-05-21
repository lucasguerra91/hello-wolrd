import nodo as n


class ListaEnlazada:
    """ Modela una lista enlazada"""

    def __init__(self):
        """ Crea una lista enlazada vacia"""
        # referencia al primer nodo (None si la lista esta vacia)
        self.prim = None
        # referencia al ultimo
        self.ultimo = None
        # cantidad de elementos de la lista
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        lista = []
        actual = self.prim
        while actual:
            lista.append(str(actual))
            actual = actual.prox
        return str(lista)

    def no_vacia(self):
        if self.prim:
            return True
        return False

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

    def remueve_por_valor(self, x):
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
            # n_act = n_ant.prox

            while n_ant.prox is not None and n_ant.prox.dato != x:
                n_ant = n_ant.prox

            if not n_ant.prox:
                raise ValueError("El valor no esta en la lista")

            # Descartar el nodo (nunca se borra en realidad)
            n_ant.prox = n_ant.prox.prox
        self.len -= 1

    def insertar_en_pos(self, i, x):
        """ Inserta el elemento x en la posicion i.
        Si la posicion es invalida, levanta IndexError"""

        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')

        nuevo = n.Nodo(x)

        if i == 0:
            # Caso particular, insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo

        else:
            # Buscar el nodo anterior a la posicion deseada

            anterior = self.prim
            actual = anterior.prox

            for pos in range(1, i):
                anterior = anterior.prox
                actual = actual.prox

            # Intercalar el nuevo nodo
            if anterior == self.ultimo:
                print(f"{anterior}es ultimo")
                anterior.prox = nuevo
                self.ultimo = nuevo
            else:
        self.len += 1

    def insertar_al_final(self, x):
        """ Agrega un elemento al final ; si la lista esta vacia se actualiza el primero y el ultimo"""
        # print(f"DEBUGG : ENTRO {x}")
        nuevo = n.Nodo(x)

        if self.no_vacia():
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        else:
            self.prim = self.ultimo = nuevo
        self.len += 1

    def __index__(self, x):
        """ Busca el indice de la primer aparicion de x dentro de la lista, si no esta
        levanta ValueError"""
        if self.no_vacia():
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

li.insertar_al_final('Hola')
li.insertar_al_final('Hola2')
li.insertar_al_final('Hola3')
li.insertar_en_pos(3, 'test')
print(li)
print(li.prim)
print(li.ultimo)
