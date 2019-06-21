def pedir_cadena():
    """Pide una cadena al usuario
    Return: la cadena que ingreso el usuario"""
    return input("Ingrese una cadena")


def crear_lista():
    """


    :return:
    """
    cadena = ""
    temp = pedir_cadena()

    while temp:
        cadena += temp
        temp = pedir_cadena()

    lista = cadena.split()

    return lista


#
lista1 = crear_lista()
print(lista1)


