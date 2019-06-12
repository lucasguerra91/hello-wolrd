cont_ms = 0
cont_m = 0


def merge_sort(lista):
    """ ordena una lista mediante el método merge sort
    Pre: la lista debe tener elementos comparables
    Devuelve: una nueva lista ordenada
    """
    global cont_ms
    cont_ms += 1

    if len(lista) < 2:
        return lista

    medio = len(lista) // 2

    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])

    return merge(izq, der)


def merge(lista1, lista2):
    """ Intercala los elementos de lista1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 y lista2 """

    global cont_m
    cont_m += 1

    i, j = 0, 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


# ejecucion
lista1 = [12, 24, 33, 105, 1, 15, 44]
print(lista1)
nl = merge_sort(lista1)
print(nl)
print('\n')


print(f"Llamadas a merge_sort :{cont_ms}")
print(f"Llamadas a merge :{cont_m}")

# lista2 = [1, 2, 3, 4, 5, 6, 7]
# print(lista2)
# nl = merge_sort(lista2)
# print(nl)