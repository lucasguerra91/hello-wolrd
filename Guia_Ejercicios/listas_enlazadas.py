import nodo as n
import iterador_lista_enlazada as iter


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):  # int(n ** 0.5)
        if (n % i) == 0:
            return False
    return True


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
        return iter.IteradorListaEnlazada(self.prim)

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
            if n_act == self.ultimo:
                n_ant.prox = None
                self.ultimo = n_ant
            else:
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

            if n_act == self.ultimo:
                n_ant.prox = None
                self.ultimo = n_ant
            else:
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
            if anterior == self.ultimo:
                # print(f"{anterior}es ultimo")
                anterior.prox = nuevo
                self.ultimo = nuevo
            else:
                anterior.prox = nuevo
                nuevo.prox = actual

        self.len += 1

    def insertar_al_final(self, x):
        """ Agrega un elemento al final ; si la lista esta vacia se actualiza el primero y el ultimo"""
        # print(f"DEBUGG : ENTRO {x}")
        nuevo = n.Nodo(x)

        if self.esta_vacia():
            self.prim = self.ultimo = nuevo
        else:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        self.len += 1

    # Ej 11.7
    def extend(self, otra):
        """ Se extiende la lista con otra que se recibe como parametro """

        if self.esta_vacia() or  otra.esta_vacia():
            raise ValueError("Una de las listas esta vacia")

        self.ultimo.prox = otra.prim
        self.ultimo = otra.ultimo
        self.len += otra.len

    # Ej 11.8
    def remover_todos(self, elemento):
        """ Remueve todas las apariciones del elemento en la lista y devuelve la cantidad removida.
        Si esta vacia levanta error, si el elemento no esta levanta error """

        if self.esta_vacia():
            return 0

        borrados = 0
        ant = None
        act = self.prim

        while act:
            if act.dato == elemento:
                # evalua el primero
                if act == self.prim:
                    self.prim = self.prim.prox
                # en caso de que sea el último
                elif act == self.ultimo:
                    self.ultimo = ant
                    ant.prox = None
                # en caso de que sea un don nadie
                else:
                    ant.prox = act.prox
                borrados += 1
            ant = act
            act = ant.prox

        self.len -= borrados
        return borrados

    # Ej 11.9
    def duplicar_elemento(self, elemento):
        """Recibe un elemento y duplica todas sus apariciones dentro de la lista """

        if self.esta_vacia():
            raise ValueError("Lista vacía.")

        act = self.prim

        while act:
            if act.dato == elemento:
                # Ojo con crearlo afuera del while, puede ser mas de uno
                nuevo = n.Nodo(elemento)
                if act == self.ultimo:
                    act.prox = nuevo
                    nuevo.prox = None
                    self.ultimo = nuevo
                else:
                    nuevo.prox = act.prox
                    act.prox = nuevo

                self.len += 1
                # Si lo agrego no lo evalúo en la sgte vuelta
                act = act.prox.prox
            else:
                act = act.prox

    # Ej 11.10
    def filter(self, funcion):
        """ recibe: una funcion
            devuelve: una nueva lista enlazada con los elementos (de la lista actual) que cumplieron
            con el criterio de la funcion """

        if self.esta_vacia():
            raise ValueError("La lista esta vacía.")

        nueva = ListaEnlazada()
        act = self.prim

        while act:
            dato = funcion(act.dato)

            if not dato:
                act = act.prox
                continue

            nuevo_nodo = n.Nodo(act.dato)

            if nueva.esta_vacia():
                nueva.prim = nuevo_nodo
                nueva.ultimo = nuevo_nodo
            else:
                nueva.ultimo.prox = nuevo_nodo
                nueva.ultimo = nuevo_nodo

            nueva.len += 1
            act = act.prox
        return nueva

    # Ej 11.11
    def invertir_lista(self):
        """ Invierte la lista """

        if self.esta_vacia():
            raise ValueError("La lista esta vacia")

        act = self.prim.prox
        self.prim.prox = None

        while act:
            sig = act.prox
            self.ultimo = self.prim
            act.prox = self.prim
            self.prim = act
            act = sig




li = ListaEnlazada()

li.insertar_al_final('Hola')
li.insertar_al_final('Hola2')
li.insertar_al_final('Hola3')

# Instertar en posicion
li.insertar_en_pos(3, 'test')
li.insertar_en_pos(3, 'test2')
li.insertar_en_pos(3, 'test3')

li.insertar_al_final('Hola4')

# Remueve por valor el primero
# li.remueve_por_valor('Hola')

# Remueve por valor cualquier
# li.remueve_por_valor('Hola2')

# Remueve por valor el ultimo
# li.remueve_por_valor('test')

# pop , borra el ultimo
li.pop()
li.pop(2)

print(li)
# for valor in li:
#     print(valor)
#
# print('\n')
# print(f"Primero : {li.prim}")
# print(f"Ultimo: {li.ultimo}")
# print(f"Longitud: {li.len}")

li2 = ListaEnlazada()
li2.insertar_al_final('Hola4')
li2.insertar_al_final('Hola5')
li2.insertar_al_final('Hola6')

print(li2)
li.extend(li2)
print(li)
print(f"\nPrimero : {li.prim}")
print(f"Ultimo: {li.ultimo}")
print(f"Longitud: {li.len}")

# li3 = ListaEnlazada()
# li.extend(li3)

li.insertar_al_final('test')
print(li)
# print(f"Se removieron {li.remover_todos('test')} apariciones de 'test'")
print(f"\nSe removieron {li.remover_todos('Hola')} apariciones de 'Hola'")
print(li)
print(f"Primero : {li.prim}")
print(f"Ultimo: {li.ultimo}")
print(f"Longitud: {li.len}")

li3 = ListaEnlazada()
li3.insertar_al_final(8)
li3.insertar_al_final(5)
li3.insertar_al_final(8)
li3.insertar_al_final(8)
li3.insertar_al_final(1)
li3.insertar_al_final(8)

print(li3)
li3.duplicar_elemento(8)

print(li3)
print(f"Primero : {li3.prim}")
print(f"Ultimo: {li3.ultimo}")
print(f"Longitud: {li3.len}")


li4 = ListaEnlazada()
li4.insertar_al_final(1)
li4.insertar_al_final(5)
li4.insertar_al_final(8)
li4.insertar_al_final(8)
li4.insertar_al_final(2)
li4.insertar_al_final(8)

print(f"Lista original \n {li4}")
nueva = li4.filter(es_primo)
print(nueva)
li4.invertir_lista()
print(li4)