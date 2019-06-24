from Parcialitos.Tercero import pila as pi


def es_piramidal(pila):
    """

    :param pila:
    :return:
    """
    piramidal = False

    if pila.esta_vacia():
        return piramidal

    aux = pi.Pila()

    # Cargo el primero en la pila auxiliar
    aux.apilar(pila.desapilar())

    while not pila.esta_vacia():

        elemento = pila.desapilar()

        if elemento > aux.ver_tope():
            aux.apilar(elemento)
            piramidal = True
        else:
            pila.apilar(elemento)
            piramidal = False
            break

    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return piramidal


# ejecucion
pila1 = pi.Pila()
pila1.apilar(5)
pila1.apilar(4)
pila1.apilar(3)
pila1.apilar(2)
pila1.apilar(1)
print(es_piramidal(pila1))
