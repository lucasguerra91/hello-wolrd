def unidad_minima(numero):
    """asdf """

    u_m = sumar_unidades(numero)

    while len(str(u_m)) > 1:
        u_m = sumar_unidades(u_m)

    return u_m


def sumar_unidades(numero):
    """ asdf """
    suma_unidades = 0
    aux = str(numero)

    for i in range(0, len(aux)):
        suma_unidades += int(aux[i])

    return suma_unidades


# ciclo de ejecución
print(unidad_minima(546))
