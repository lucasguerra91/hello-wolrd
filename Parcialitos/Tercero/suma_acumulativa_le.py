import nodo as n
import iterador_lista_enlazada as iter_le


class ListaEnlazada:
    """ Modela una lista enlazada"""

    def __init__(self):
        """ Crea una lista enlazada vacia"""
        # referencia al primer nodo (None si la lista esta vacia)
        self.prim = None
        # referencia al ultimo
        # self.ultimo = None
        # cantidad de elementos de la lista
        self.len = 0

    def __len__(self):
        return self.len

    # Ejercicio 11.6
    def __str__(self):
        """ Genera una salida legible de lo que contiene la lista, similar a las listas de Python"""
        lista = []
        actual = self.prim
        while actual:
            lista.append(str(actual))
            actual = actual.prox
        return str(lista)

    def __iter__(self):
        return iter.iter_le.IteradorListaEnlazada(self.prim)

    def __index__(self, x):
        """ Busca el indice de la primer aparicion de x dentro de la lista, si no esta
        levanta ValueError"""

        if self.esta_vacia():
            raise ValueError("Lista vacía.")

        pos = 0
        actual = self.prim

        while actual:
            if actual.dato == x:
                return pos
            actual = actual.prox
            pos += 1

        raise ValueError(f"{x} no se encuentra dentro de la lista")

    def esta_vacia(self):
        if self.prim:
            return False
        return True

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
            n_ant.prox = n_act.prox

            dato = n_act.dato
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
            n_act = n_ant.prox

            while n_act is not None and n_act.dato != x:
                n_ant = n_ant.prox
                n_act = n_act.prox

            if not n_act.prox and n_act.dato != x:
                raise ValueError(f"El valor {n_act}no esta en la lista")

            n_ant.prox = n_act.prox

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

            anterior.prox = nuevo
            nuevo.prox = actual

        self.len += 1

    def append(self, x):
        """ Agrega un elemento al final ; si la lista esta vacia se actualiza el primero """
        # print(f"DEBUGG : ENTRO {x}")

        nuevo = n.Nodo(x)

        if self.esta_vacia():
            self.prim = nuevo
            return

        act = self.prim
        while act.prox:
            act = act.prox

        act.prox = nuevo
        self.len += 1

    def suma_acumulativa(self):
        """ Devuelve una lista enlazada con la suma acumulativa en cada nodo """

        if self.esta_vacia():
            print("Lista vacía..")
            return

        nueva = ListaEnlazada()
        act = self.prim
        suma_ac = 0

        while act:
            suma_ac += act.dato
            nodo = n.Nodo(suma_ac)

            nueva.append(nodo)
            act = act.prox

        return nueva


# Ejecucion
lista = ListaEnlazada()
lista.append(1)
lista.append(10)
lista.append(100)
lista.append(1000)
lista.append(10000)
lista.append(100000)

print(lista)

lista2 = lista.suma_acumulativa()
print(lista2)
