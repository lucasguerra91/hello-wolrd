def lista_rotaciones(palabra):
    """

    :param palabra: una palabra
    :return: lista de rotaciones (de caracteres) de la palabra
    """

    lista = [palabra]

    for i in range(len(palabra)-1):
        temp = palabra[i+1: len(palabra)] + palabra[:i+1]
        lista.append(temp)

    return lista


# ejecucion
print(lista_rotaciones("rotar"))
