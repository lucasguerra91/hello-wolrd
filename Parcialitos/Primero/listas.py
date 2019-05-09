# 1) Escribir una función que reciba por parámetro una lista de números y devuelva otra lista
# con los números de la ingresada que terminan en cero. Por ejemplo, si se recibe la lista:
#  [4, 23, 40, -7, 0, 14, 1000, -760]
# debe devolver [40, 0, 1000, -760].


def filtrar_lista_cero(lista):
    """ Recibe como parametro una lista de numeros, verifica los terminados en cero,
    los agrega a una nueva lista y por ultimo la devuelve"""

    nueva_lista = []

    for numero in lista:
        lista_auxiliar = list(str(numero))
        if lista_auxiliar[len(lista_auxiliar)-1] == '0':
            nueva_lista.append(numero)
    return nueva_lista


test_list = [4, 23, 40, -7, 0, 14, 1000, -760]
print(filtrar_lista_cero(test_list))