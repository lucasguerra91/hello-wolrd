from Parcialitos.Tercero import cola as col


def es_par(n):
    if n % 2 == 0:
        return True
    return False


def filtrar_cola(cola, funcion):
    """
    :param cola: de elementos
    :param funcion: funcion que devuelva true o false
    :return: una nueva cola con los elementos que aplican a la consigna de la funcion
    """

    nueva_cola = col.Cola()

    if cola.esta_vacia():
        return nueva_cola

    aux = col.Cola()

    while not cola.esta_vacia():
        elemento = cola.desencolar()

        aux.encolar(elemento)

        if funcion(elemento):
            nueva_cola.encolar(elemento)

    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

    return nueva_cola


# ejecucion
colita = col.Cola()
colita.encolar(1)
colita.encolar(3)
colita.encolar(4)
colita.encolar(5)
colita.encolar(7)
colita.encolar(9)
colita.encolar(10)
colita.encolar(15)
colita.encolar(17)
colita.encolar(18)
colita.encolar(19)
colita.encolar(30)

print(colita)

colita_pares = filtrar_cola(colita, es_par)
print(colita_pares)
