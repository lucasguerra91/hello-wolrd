from Parcialitos.Tercero import pila as p


def remove_dupl_consec(pila):
    """

    :param pila:
    :return:
    """

    if pila.esta_vacia():
        return

    aux = p.Pila()

    # Apilo los no-repetidos en una pila auxiliar
    while not pila.esta_vacia():

        dato = pila.desapilar()

        if dato != aux.ver_tope():
            aux.apilar(dato)

    # Devuelvo los elementos a la pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())


# testing
pila_1 = p.Pila()
pila_1.apilar(2)
pila_1.apilar(8)
pila_1.apilar(8)
pila_1.apilar(8)
pila_1.apilar(3)
pila_1.apilar(3)
pila_1.apilar(2)
pila_1.apilar(3)
pila_1.apilar(3)
pila_1.apilar(3)
pila_1.apilar(3)
pila_1.apilar(1)
pila_1.apilar(7)

print(pila_1)

remove_dupl_consec(pila_1)

print(pila_1)