def sumar(lista, suma=0):
    if len(lista) == 0:
        return suma
    return sumar(lista[1:], lista[0] + suma)


def sumar_w(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0
    while True:
        if len(lista) == 0:
            return suma
        lista, suma = lista[1:], lista[0] + suma


# ejecucion
lista1 = [1, 2, 3, 4, 5]
print(sumar(lista1))
print(sumar_w(lista1))
